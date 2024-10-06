# Real-time Cyber Attacks FastAPI DB

This project is a FastAPI-based web application designed to scrape real-time cyber attack data from an external source, parse the data, and store it in a database using Tortoise ORM.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Complexities](#complexities)
- [Solutions](#solutions)
- [Challenges](#challenges)
- [License](#license)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/faisal-fida/Real-time-Cyber-Attacks-FastAPI-DB.git
cd Real-time-Cyber-Attacks-FastAPI-DB
```

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file with the following content:

```
DB_URL=<your_database_url>
```

4. Run the application:

```sh
uvicorn main:app --reload
```

## Usage

The application provides the following endpoints:

1. `GET /` - Returns the status of the API.
2. `GET /attacks/{limit}` - Fetches a limited number of real-time cyber attack data and stores it in the database.
3. `GET /attacks` - Retrieves all stored cyber attack data from the database.

## Features

- **Asynchronous Data Scraping**: The project uses asynchronous programming to efficiently scrape data from an external API. This ensures non-blocking operations and better performance.
- **Database Integration**: Utilizes Tortoise ORM to interact with the database, including initializing the database and defining data models.
- **Data Parsing and Validation**: Uses Pydantic models to parse and validate the scraped data before storing it in the database.
- **Efficient Scraping**: Implemented an asynchronous data scraper using the `httpx` library to handle multiple requests concurrently, reducing the time taken to fetch data.
- **Database Initialization**: The `init_db` function in `database.py` sets up the database connection and registers the models, ensuring a seamless integration with the FastAPI application.
- **Data Model Definition**: Defined a `DataModel` class in `models.py` using Tortoise ORM to represent the structure of the data being stored, ensuring data integrity and consistency.
- **Error Handling**: Managing errors during data scraping, such as handling non-200 HTTP responses and network issues, required robust error handling mechanisms.
- **Concurrency Management**: Ensuring that multiple asynchronous operations do not lead to race conditions or data corruption was a key challenge.
- **Data Consistency**: Maintaining data consistency when parsing and storing large volumes of real-time data required careful design and validation.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
