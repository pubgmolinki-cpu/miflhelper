import re

def parse_match(text):

    score_pattern = r"\*\sСчет:\s(.+?)\s(\d+)\s:\s(\d+)\s(.+)"

    score_match = re.search(
        score_pattern,
        text
    )

    if not score_match:

        score_pattern_alt = r"Счет:\s(.+?)\s(\d+)\s:\s(\d+)\s(.+)"

        score_match = re.search(
            score_pattern_alt,
            text
        )

    if not score_match:
        return None

    home_team = score_match.group(1).strip()
    home_score = int(score_match.group(2))
    away_score = int(score_match.group(3))
    away_team = score_match.group(4).strip()

    motm_pattern = r"🌟 Игрок матча \(MOTM\).*?\*\s(.+?)\s\("

    motm_match = re.search(
        motm_pattern,
        text,
        re.DOTALL
    )

    motm = None

    if motm_match:
        motm = motm_match.group(1)

    return {

        "home_team": home_team,
        "away_team": away_team,
        "home_score": home_score,
        "away_score": away_score,
        "motm": motm

    }
