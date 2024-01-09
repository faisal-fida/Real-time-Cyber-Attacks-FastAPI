from fastapi import FastAPI
from pydantic import BaseModel

from database import init_db
from models import DataModel

from typing import Optional, Union
import requests as req
import uvicorn
import logging
import json

logging.basicConfig(level=logging.INFO)
app = FastAPI()
init_db(app)


class Data(BaseModel):
    sourceCountry: Union[str, None] = (None,)
    destinationCountry: Union[str, None] = (None,)
    millisecond: Union[int, None] = (None,)
    type: Union[str, None] = (None,)
    weight: Union[int, None] = (None,)
    attackTime: Union[str, None] = None


async def data_scraper(url: str, headers: dict) -> Union[list, dict]:
    logging.info(f"Scraping data from {url}")
    response = req.get(url, headers=headers)
    if response.status_code == 200:
        logging.info(f"Data scraped successfully: {response.json()[0][0]}")
        return response.json()[0]
    else:
        return response.status_code


async def data_parser(data: dict) -> list:
    parsed_data = []
    for item in data:
        parsed_data.append(
            Data(
                sourceCountry=item["sourceCountry"],
                destinationCountry=item["destinationCountry"],
                millisecond=item["millisecond"],
                type=item["type"],
                weight=item["weight"],
                attackTime=item["attackTime"],
            )
        )
    return parsed_data


@app.get("/")
async def index():
    return {f"{app.title}": "Working"}


@app.get("/attacks/{limit}")
async def get_data(limit: int) -> list:
    url = f"https://livethreatmap.radware.com/api/map/attacks?limit={limit}"
    headers = {"Accept": "application/json"}
    data = await data_scraper(url, headers)
    parsed_data = await data_parser(data)
    DataModel.create(**parsed_data.dict())
    return parsed_data


@app.get("/attacks")
async def get_data() -> list:
    attacks = await DataModel.get_or_none()
    return attacks


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
