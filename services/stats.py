from database import pool

async def add_goal(player_name):

    async with pool.acquire() as conn:

        exists = await conn.fetchrow("""

        SELECT *
        FROM players
        WHERE player_name=$1

        """, player_name)

        if not exists:

            await conn.execute("""

            INSERT INTO players (
                player_name,
                goals
            )

            VALUES ($1,1)

            """,

            player_name
            )

        else:

            await conn.execute("""

            UPDATE players

            SET goals = goals + 1

            WHERE player_name=$1

            """,

            player_name
            )

async def add_assist(player_name):

    async with pool.acquire() as conn:

        exists = await conn.fetchrow("""

        SELECT *
        FROM players
        WHERE player_name=$1

        """, player_name)

        if not exists:

            await conn.execute("""

            INSERT INTO players (
                player_name,
                assists
            )

            VALUES ($1,1)

            """,

            player_name
            )

        else:

            await conn.execute("""

            UPDATE players

            SET assists = assists + 1

            WHERE player_name=$1

            """,

            player_name
            )
