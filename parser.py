import re

def parse_match(text):

    score_pattern = r"Счет:\s(.+?)\s(\d)\s:\s(\d)\s(.+)"

    score_match = re.search(
        score_pattern,
        text
    )

    if not score_match:
        return None

    home_team = score_match.group(1)
    home_score = int(score_match.group(2))
    away_score = int(score_match.group(3))
    away_team = score_match.group(4)

    motm_pattern = r"🌟 Игрок матча \(MOTM\).*?([А-Яа-яA-Za-z]+)"

    motm_match = re.search(
        motm_pattern,
        text
    )

    motm = None

    if motm_match:
        motm = motm_match.group(1)

    goals = []

    goal_pattern = r"(\d+)' ⚽ ГОЛ!.*?— «(.+?)»:"

    for goal in re.finditer(goal_pattern, text):

        minute = goal.group(1)
        club = goal.group(2)

        goals.append({
            "minute": minute,
            "club": club
        })

    return {
        "home_team": home_team,
        "away_team": away_team,
        "home_score": home_score,
        "away_score": away_score,
        "motm": motm,
        "goals": goals
    }
