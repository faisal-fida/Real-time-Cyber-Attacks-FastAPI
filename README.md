# Real-time-Cyber-Attacks-FastAPI-DB

## Overview

This project aims to provide a real-time monitoring and analysis tool for cyber-attacks using FastAPI and a database. By leveraging a combination of libraries and tools, it offers a robust and efficient system to detect and analyze potential threats.

## Features

- Real-time monitoring of cyber-attacks.
- FastAPI framework for high-performance API endpoints.
- Integration with a database using Tortoise-ORM.
- Configuration management using Python-Dotenv.
- HTTP client for external data retrieval with Requests.

## Requirements

Ensure you have the following dependencies installed:

- aerich==0.7.2
- fastapi==0.108.0
- pydantic==2.5.3
- python-dotenv==1.0.0
- requests==2.31.0
- tortoise-orm==0.20.0
- uvicorn==0.25.0

You can install them using pip:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/faisal-fida/Real-time-Cyber-Attacks-FastAPI-DB.git
```

2. Navigate to the project directory:

```bash
cd Real-time-Cyber-Attacks-FastAPI-DB
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your configuration variables in the `.env` file. For example:

```
DATABASE_URL=sqlite://db.postgre
API_KEY=your_api_key
```

## Usage

1. Run the FastAPI application using Uvicorn:

```bash
python main.py
```

2. Access the FastAPI application by navigating to:

```
http://localhost:8000
```

## Database Migrations

To manage database migrations, use Aerich:

1. Initialize Aerich:

```bash
aerich init -t database.TORTOISE_ORM
```

2. Create a migration:

```bash
aerich migrate
```

3. Apply migrations:

```bash
aerich upgrade
```
