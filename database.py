import asyncpg
from config import DATABASE_URL

pool = None

async def connect_db():
    global pool

    pool = await asyncpg.create_pool(
        DATABASE_URL
    )

async def create_tables():

    async with pool.acquire() as conn:

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS clubs (
            id SERIAL PRIMARY KEY,
            league TEXT,
            name TEXT,
            points INTEGER DEFAULT 0,
            wins INTEGER DEFAULT 0,
            draws INTEGER DEFAULT 0,
            losses INTEGER DEFAULT 0,
            goals_scored INTEGER DEFAULT 0,
            goals_conceded INTEGER DEFAULT 0
        );

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS matches (
            id SERIAL PRIMARY KEY,
            league TEXT,
            tour INTEGER,
            home_team TEXT,
            away_team TEXT,
            home_score INTEGER,
            away_score INTEGER,
            raw_text TEXT
        );

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            club TEXT,
            player_name TEXT,
            goals INTEGER DEFAULT 0,
            assists INTEGER DEFAULT 0,
            motm INTEGER DEFAULT 0,
            average_rating FLOAT DEFAULT 0
        );

        """)

async def add_match(
    league,
    tour,
    home_team,
    away_team,
    home_score,
    away_score,
    raw_text
):

    async with pool.acquire() as conn:

        await conn.execute("""

        INSERT INTO matches (
            league,
            tour,
            home_team,
            away_team,
            home_score,
            away_score,
            raw_text
        )

        VALUES ($1,$2,$3,$4,$5,$6,$7)

        """,

        league,
        tour,
        home_team,
        away_team,
        home_score,
        away_score,
        raw_text
        )

async def get_matches(league, tour):

    async with pool.acquire() as conn:

        rows = await conn.fetch("""

        SELECT *
        FROM matches
        WHERE league=$1
        AND tour=$2

        """, league, tour)

        return rows

async def get_table(league):

    async with pool.acquire() as conn:

        rows = await conn.fetch("""

        SELECT *
        FROM clubs
        WHERE league=$1
        ORDER BY points DESC,
        goals_scored - goals_conceded DESC

        """, league)

        return rows
