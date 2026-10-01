#!/usr/bin/env python3
"""
Example script for querying the Houdinick Italian Public Tenders API.
Get your production API key at: https://rapidapi.com/nvaligi/api/houdinick-tenders-api
"""
import os
import json
import urllib.request
import urllib.parse

# Default to test demo key if RAPIDAPI_KEY is not set in environment
API_KEY = os.environ.get("RAPIDAPI_KEY", "hn_tenders_test_key_001")
BASE_URL = "https://houdinick-data-api-production.up.railway.app/api/v1/tenders"

def fetch_tenders(category="pnrr_appalto", location="Lombardia", value_min=5000000, limit=5):
    params = {
        "category": category,
        "location": location,
        "value_min": str(value_min),
        "limit": str(limit),
    }
    query_string = urllib.parse.urlencode({k: v for k, v in params.items() if v})
    full_url = f"{BASE_URL}?{query_string}"
    
    headers = {
        "User-Agent": "Houdinick-Tenders-Client/1.0",
        "X-API-Key": API_KEY,
    }
    
    print(f"Fetching from Houdinick Tenders API...")
    print(f"URL: {full_url}\n")
    req = urllib.request.Request(full_url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            items = data.get("items", [])
            print(f"✅ Success! Retrieved {len(items)} public contracts (Total matching in DB: {data.get('count', 0)}):\n")
            for item in items:
                p = item.get("payload", {})
                cig = p.get("codice_cig", "N/A")
                title = item.get("title", "")
                val = item.get("value_num", 0)
                buyer = p.get("stazione_appaltante", "N/A")
                loc = item.get("location", "N/A")
                mission = p.get("missione_pnrr", "N/A")
                deadline = p.get("scadenza_offerte", "N/A")
                
                print(f"📌 [CIG: {cig}] {title}")
                print(f"   Stazione Appaltante : {buyer}")
                print(f"   Importo Base Asta   : €{val:,.2f}")
                print(f"   Localizzazione      : {loc}")
                print(f"   Missione PNRR       : {mission}")
                print(f"   Scadenza Offerte    : {deadline}")
                print("-" * 65)
                
            print(f"\nNext cursor for delta updates: since_seq={data.get('next_seq')}")
            print("Get full high-concurrency access at: https://rapidapi.com/nvaligi/api/houdinick-tenders-api")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_tenders()
