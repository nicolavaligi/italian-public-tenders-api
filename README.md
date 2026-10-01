# Italian Public Tenders & PNRR Contracts Feed (REST API)

[![RapidAPI Hub](https://img.shields.io/badge/RapidAPI-Houdinick%20Tenders%20API-blueviolet.svg)](https://rapidapi.com/nvaligi/api/houdinick-tenders-api)
[![Status](https://img.shields.io/badge/Status-Operational%20(200%20OK)-brightgreen.svg)](https://houdinick-data-api-production.up.railway.app/health)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Feed programmatico in tempo reale per l'intercettazione e il monitoraggio di **Gare d'Appalto, Bandi Pubblici e Lavori PNRR** in Italia per oltre **€3,48 Miliardi**.

Progettato per **General Contractor, Uffici Gare, Società di Ingegneria, Broker Assicurativi (Fideiussioni) e Banche (Anticipo Contratti PA)**.

---

## Dati Chiave Disponibili nel Feed

- **Codici Identificativi:** CIG (`codice_cig`), CUP (`codice_cup`).
- **Valore Economico:** Importo a base d'asta in Euro (`value_num`), ribasso e criteri di aggiudicazione (OEPV / minor prezzo).
- **Stazioni Appaltanti:** Rete Ferroviaria Italiana (RFI), ANAS, Consorzi di Bonifica, Acquedotti Regionali, Grandi Comuni.
- **Missioni PNRR:** M1 (Digitalizzazione), M2 (Transizione Ecologica), M3 (Infrastrutture Mobilità), M4 (Istruzione), M5 (Inclusione), M6 (Salute).
- **Coordinate Geografiche:** Latitudine e Longitudine per ciascun cantiere.
- **Cursore Incrementale Monotono (`since_seq`):** Scarica solo ciò che è cambiato dall'ultima interrogazione, senza duplicati.

---

## Quickstart Python (5 righe)

```python
import urllib.request
import json

# Richiedi la tua chiave su RapidAPI Hub: https://rapidapi.com/nvaligi/api/houdinick-tenders-api
API_KEY = "TUA_CHIAVE_RAPIDAPI"

url = "https://houdinick-data-api-production.up.railway.app/api/v1/tenders?category=pnrr_appalto&location=Lombardia&value_min=5000000"
req = urllib.request.Request(url, headers={"X-API-Key": API_KEY})

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    for tender in data["items"]:
        p = tender["payload"]
        print(f"[{p['codice_cig']}] {tender['title']}")
        print(f"  Ente: {p['stazione_appaltante']} | Base d'asta: €{tender['value_num']:,.2f}")
```

---

## cURL

```bash
curl -X GET "https://houdinick-data-api-production.up.railway.app/api/v1/tenders?category=pnrr_appalto&limit=5" \
  -H "X-API-Key: TUA_CHIAVE_RAPIDAPI"
```

---

## Piani Tariffari & Accesso Self-Serve

Il servizio è monetizzato e distribuito tramite **RapidAPI Hub**:

| Piano | Prezzo | Quota Inclusa | Costo Chiamata Extra | Accesso |
|---|---|---|---|---|
| **Basic (Free)** | **$0.00 / mese** | 50 chiamate / mese | $0.10 / chiamata | [👉 Attiva su RapidAPI](https://rapidapi.com/nvaligi/api/houdinick-tenders-api) |
| **Pro** | **$49.00 / mese** | 2,000 chiamate / mese | $0.05 / chiamata | [👉 Attiva su RapidAPI](https://rapidapi.com/nvaligi/api/houdinick-tenders-api) |

---

## SDK Ufficiale & Documentazione Completa

Visita il repository principale Houdinick con il client Python e le altre API (Bonifiche e Fotovoltaico):  
👉 **[github.com/nicolavaligi/houdinick-data-feeds](https://github.com/nicolavaligi/houdinick-data-feeds)**  
👉 **[Landing Page Ufficiale](https://nicolavaligi.github.io/houdinick-data-feeds/)**

---

## Licenza

Distribuito sotto licenza [MIT](LICENSE). Copyright © 2026 Houdinick.
