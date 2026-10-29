
import requests
from datetime import datetime

pseudo = "ZipZap38"
URL = "https://topmoddedservers.com/api/servers/create-france/vote"
PAGE_URL = "https://topmoddedservers.com/serveur/create-france/vote"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Referer": PAGE_URL,
})

print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] Trying voting...")

try:
    session.get(PAGE_URL, timeout=20)

    reponse = session.post(
        URL,
        json={
            "username": pseudo,
            "website": "",
        },
        timeout=20,
    )

    print("HTTP :", reponse.status_code)
    print("Answer :", reponse.text[:500])

    if reponse.status_code == 429:
        print("Vote not available yet; rate limit reached.")

    reponse.raise_for_status()

except requests.RequestException as erreur:
    print("ERROR :", erreur)
    raise
