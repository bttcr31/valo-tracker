import os
import requests

API_KEY = os.getenv("RIOT_TEST_KEY")

if not API_KEY:
    print("RIOT_TEST_KEY bulunamadı.")
    input("Enter'a bas...")
    exit()

RIOT_ID = "S A S K E"
TAGLINE = "9904"

url = (
    "https://europe.api.riotgames.com/"
    f"riot/account/v1/accounts/by-riot-id/{RIOT_ID.replace(' ', '%20')}/{TAGLINE}"
)

response = requests.get(
    url,
    headers={"X-Riot-Token": API_KEY}
)

print("HTTP durum kodu:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print()
    print("========== HESAP ==========")
    print("Riot ID :", data.get("gameName"))
    print("Tagline :", data.get("tagLine"))
    print("PUUID   :", data.get("puuid"))
    print("============================")
else:
    print("Sunucu cevabı:", response.text)

input("\nKapatmak için Enter'a bas...")