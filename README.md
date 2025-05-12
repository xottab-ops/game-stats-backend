# Game Statistic (Backend)

## Project Description

This project is a REST API for managing video game information. The API provides functionality to work with games, developers, publishers, categories, and platforms. CRUD operations are implemented for games, along with aggregated data for developers and publishers.

## Key Technologies

- **Flask**: Web framework for building REST APIs.
- **PostgreSQL**: Relational database for data storage.
- **SQLAlchemy**: ORM for database interaction.
- **Marshmallow**: For data serialization and validation.
- **Docker**: For containerizing the application and database.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd game-stats-backend
```

### 2. Configure Environment Variables

Ensure the `.env` file in the project root is configured as follows:

```dotenv
# Flask
FLASK_APP=app.py
FLASK_ENV=development
FLASK_INNER_PORT=5000
FLASK_OUTER_PORT=5000

# Database
POSTGRES_DB=flask_db
POSTGRES_USER=flask_user
POSTGRES_PASSWORD=flask_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Database URI for application
DATABASE_URI=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```

### 3. Run with Docker

Ensure Docker is installed and running. Then execute:

```bash
docker-compose up --build
```

This will create and start two containers:
- `backend`: Flask application.
- `db`: PostgreSQL database.

### 4. Import Data

To load data from the `steam.csv` file, run the following command:

```bash
docker exec -it flask_app python import_data.py
```

### 5. Access the API

Once running, the application will be accessible at: [http://localhost:5000](http://localhost:5000).

## API Endpoints

### Games

- `GET /api/v1/games` — Retrieve a list of games.
- `GET /api/v1/games/<id>` — Retrieve game details by ID.
- `POST /api/v1/games` — Create a new game.
- `PUT /api/v1/games/<id>` — Update game details.
- `DELETE /api/v1/games/<id>` — Delete a game.

### Statistics

- `GET /api/v1/stats/developers` — Retrieve aggregated data for developers.
- `GET /api/v1/stats/publishers` — Retrieve aggregated data for publishers.

## Project Structure

```
game-stats-backend/
├── app/
│   ├── dto/            # Data Transfer Objects (DTOs) for structured data handling
│   ├── models/         # Database models
│   ├── routes/         # API routes
│   ├── schemas/        # Data serialization schemas
│   ├── seeds/          # Scripts for seeding the database
│   ├── services/       # Business logic and data handling
│   ├── config.py       # Application configuration
│   ├── extensions.py   # Flask extensions initialization
│   ├── __init__.py     # Application initialization
├── static/             # Static files (e.g., steam.csv)
├── import_data.py      # Script to import data into the database
├── requirements.txt    # Python dependencies
├── docker-compose.yml  # Docker Compose configuration
├── .env                # Environment variables
├── README.md           # Project documentation
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
