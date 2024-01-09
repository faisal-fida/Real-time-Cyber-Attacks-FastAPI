from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "datamodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "sourceCountry" VARCHAR(255) NOT NULL,
    "destinationCountry" VARCHAR(255) NOT NULL,
    "millisecond" INT NOT NULL,
    "type" VARCHAR(255) NOT NULL,
    "weight" INT NOT NULL,
    "attackTime" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
