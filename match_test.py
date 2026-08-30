import os
import requests

API_KEY = os.getenv("RIOT_TEST_KEY")
PUUID = "X18LwbIDFk4xJJx_9tsR54GaARyEjQLmc7o1ZL1o-yFSuX9Z_9dl8I1NzpIjs4wWILeqB6Ev14390Q"

if not API_KEY:
    print("RIOT_TEST_KEY bulunamadı.")
    input("Enter'a bas...")
    exit()

url = f"https://europe.api.riotgames.com/val/match/v1/matchlists/by-puuid/{PUUID}"

response = requests.get(
    url,
    headers={"X-Riot-Token": API_KEY}
)

print("HTTP durum kodu:", response.status_code)
print("Sunucu cevabı:", response.text)

input("\nKapatmak için Enter'a bas...")