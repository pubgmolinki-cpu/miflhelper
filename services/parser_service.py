import re

def extract_goals(text):

    goals = []

    pattern = r"(\d+)' ⚽ ГОЛ!"

    for goal in re.finditer(pattern, text):

        minute = goal.group(1)

        goals.append({
            "minute": minute
        })

    return goals

def extract_motm(text):

    pattern = r"🌟 Игрок матча \(MOTM\)"

    found = re.search(pattern, text)

    if found:
        return True

    return False

def extract_score(text):

    pattern = r"Счет:\s(.+?)\s(\d)\s:\s(\d)\s(.+)"

    result = re.search(pattern, text)

    if not result:
        return None

    return {

        "home_team": result.group(1),
        "home_score": int(result.group(2)),
        "away_score": int(result.group(3)),
        "away_team": result.group(4)

    }
