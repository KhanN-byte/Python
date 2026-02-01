import os
import requests
from pync import Notifier

API_KEY = os.getenv("CRICKETDATA_API_KEY")
if not API_KEY:
    raise SystemExit("Set CRICKETDATA_API_KEY in your environment (your GUID API key).")

URL = "https://api.cricapi.com/v1/currentMatches"
WATCH_TEAMS = {"India", "Pakistan"}


def fetch_current_matches():
    r = requests.get(URL, params={"apikey": API_KEY, "offset": 0}, timeout=20)

    if r.status_code != 200:
        raise SystemExit(
            f"HTTP {r.status_code}\nBody (first 500 chars):\n{r.text[:500]}"
        )

    text = r.text.strip()
    if not text.startswith("{"):
        raise SystemExit(
            f"Non-JSON response received.\nBody (first 500 chars):\n{text[:500]}"
        )

    payload = r.json()

    if payload.get("status") != "success":
        raise SystemExit(f"API returned failure: {payload}")

    return payload.get("data", [])


def involves_watch_team(match: dict) -> bool:
    teams = match.get("teams") or []
    teams_set = {t.strip() for t in teams if isinstance(t, str)}
    return len(teams_set & WATCH_TEAMS) > 0


def format_score(match: dict) -> str:
    score_list = match.get("score") or []
    if not score_list:
        return "Score not available yet."

    parts = []
    for s in score_list:
        inning = str(s.get("inning") or "").strip()
        r = s.get("r")
        w = s.get("w")
        o = s.get("o")

        if r is None or w is None or o is None:
            continue

        parts.append(f"{inning}: {r}/{w} ({o})" if inning else f"{r}/{w} ({o})")

    return " | ".join(parts) if parts else "Score not available yet."


def summarize_match(match: dict) -> str:
    name = match.get("name") or "Match"
    status = match.get("status") or "Status unavailable"
    score = format_score(match)
    return f"{name}\n{score}\n{status}"


def main():
    matches = fetch_current_matches()
    filtered = [m for m in matches if involves_watch_team(m)]

    if not filtered:
        print("No current matches found for India or Pakistan.")
        return

    print(f"Found {len(filtered)} match(es) involving India or Pakistan:\n")

    # Print all matches to terminal
    for i, m in enumerate(filtered, start=1):
        print(f"{i}. {summarize_match(m)}")
        print("-" * 60)

    # Notification: show the first match (or a compact rollup if multiple)
    if len(filtered) == 1:
        title = "Cricket Update"
        body = summarize_match(filtered[0])
    else:
        title = "Cricket Updates"
        lines = []
        for m in filtered[:3]:  # keep notification short
            name = m.get("name") or "Match"
            status = m.get("status") or ""
            lines.append(f"- {name} ({status})")
        body = "\n".join(lines)
        if len(filtered) > 3:
            body += f"\n+ {len(filtered) - 3} more"

    Notifier.notify(body, title=title, app_name="Cric Notify")


if __name__ == "__main__":
    main()