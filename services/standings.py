from database import pool

async def create_club_if_not_exists(
    league,
    club_name
):

    async with pool.acquire() as conn:

        exists = await conn.fetchrow("""

        SELECT *
        FROM clubs
        WHERE league=$1
        AND name=$2

        """, league, club_name)

        if not exists:

            await conn.execute("""

            INSERT INTO clubs (
                league,
                name
            )

            VALUES ($1,$2)

            """,

            league,
            club_name
            )

async def update_standings(
    league,
    home_team,
    away_team,
    home_score,
    away_score
):

    await create_club_if_not_exists(
        league,
        home_team
    )

    await create_club_if_not_exists(
        league,
        away_team
    )

    async with pool.acquire() as conn:

        # goals

        await conn.execute("""

        UPDATE clubs

        SET
        goals_scored = goals_scored + $1,
        goals_conceded = goals_conceded + $2

        WHERE league=$3
        AND name=$4

        """,

        home_score,
        away_score,
        league,
        home_team
        )

        await conn.execute("""

        UPDATE clubs

        SET
        goals_scored = goals_scored + $1,
        goals_conceded = goals_conceded + $2

        WHERE league=$3
        AND name=$4

        """,

        away_score,
        home_score,
        league,
        away_team
        )

        # win / lose / draw

        if home_score > away_score:

            await conn.execute("""

            UPDATE clubs

            SET
            points = points + 3,
            wins = wins + 1

            WHERE league=$1
            AND name=$2

            """,

            league,
            home_team
            )

            await conn.execute("""

            UPDATE clubs

            SET
            losses = losses + 1

            WHERE league=$1
            AND name=$2

            """,

            league,
            away_team
            )

        elif away_score > home_score:

            await conn.execute("""

            UPDATE clubs

            SET
            points = points + 3,
            wins = wins + 1

            WHERE league=$1
            AND name=$2

            """,

            league,
            away_team
            )

            await conn.execute("""

            UPDATE clubs

            SET
            losses = losses + 1

            WHERE league=$1
            AND name=$2

            """,

            league,
            home_team
            )

        else:

            await conn.execute("""

            UPDATE clubs

            SET
            points = points + 1,
            draws = draws + 1

            WHERE league=$1
            AND name=$2

            """,

            league,
            home_team
            )

            await conn.execute("""

            UPDATE clubs

            SET
            points = points + 1,
            draws = draws + 1

            WHERE league=$1
            AND name=$2

            """,

            league,
            away_team
            )
