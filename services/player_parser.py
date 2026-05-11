import re

def extract_player_ratings(text):

    players = []

    pattern = r"\*\s(.+?)\s\(.+?\)\s\|\sОценка:\s([\d.]+)"

    matches = re.finditer(pattern, text)

    for match in matches:

        player_name = match.group(1)
        rating = float(match.group(2))

        players.append({
            "player_name": player_name,
            "rating": rating
        })

    return players

def extract_goalscorers(text):

    scorers = []

    pattern = r"\*\s(.+?)\s\(.+?\)\s\|\sОценка:.*?1 Гол"

    matches = re.finditer(
        pattern,
        text
    )

    for match in matches:

        scorers.append(
            match.group(1)
        )

    return scorers

def extract_assisters(text):

    assisters = []

    pattern = r"\*\s(.+?)\s\(.+?\)\s\|\sОценка:.*?1 Ассист"

    matches = re.finditer(
        pattern,
        text
    )

    for match in matches:

        assisters.append(
            match.group(1)
        )

    return assisters
