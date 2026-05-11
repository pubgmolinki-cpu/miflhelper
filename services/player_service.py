from database import pool

async def create_player_if_not_exists(
    player_name
):

    async with pool.acquire() as conn:

        exists = await conn.fetchrow("""

        SELECT *
        FROM players
        WHERE player_name=$1

        """, player_name)

        if not exists:

            await conn.execute("""

            INSERT INTO players (
                player_name
            )

            VALUES ($1)

            """,

            player_name
            )

async def add_goal(player_name):

    await create_player_if_not_exists(
        player_name
    )

    async with pool.acquire() as conn:

        await conn.execute("""

        UPDATE players

        SET goals = goals + 1

        WHERE player_name=$1

        """,

        player_name
        )

async def add_assist(player_name):

    await create_player_if_not_exists(
        player_name
    )

    async with pool.acquire() as conn:

        await conn.execute("""

        UPDATE players

        SET assists = assists + 1

        WHERE player_name=$1

        """,

        player_name
        )

async def add_motm(player_name):

    await create_player_if_not_exists(
        player_name
    )

    async with pool.acquire() as conn:

        await conn.execute("""

        UPDATE players

        SET motm = motm + 1

        WHERE player_name=$1

        """,

        player_name
        )
