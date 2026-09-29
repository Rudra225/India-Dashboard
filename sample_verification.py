import json
import random
import os

print("--- DATA VERIFICATION SAMPLE ---")
print("Here is a random sample of MPs and MLAs pulled directly from your dashboard's database.")
print("Click the provided MyNeta links to cross-verify the numbers directly on the official source.\n")

# LOK SABHA
try:
    with open("data/lok_sabha.json", "r", encoding="utf-8") as f:
        ls_data = json.load(f)
        all_mps = [mp for mps in ls_data.values() for mp in mps]
        sample_mps = random.sample(all_mps, 3)
        print("LOK SABHA MPs (2024)")
        for mp in sample_mps:
            name = mp.get("name", "Unknown")
            assets = mp.get("total_assets_cr", 0)
            liab = mp.get("total_liabilities_cr", 0)
            url = mp.get("affidavit_url", "No URL")
            print(f"- {name}")
            print(f"  Assets: Rs.{assets} Cr | Liabilities: Rs.{liab} Cr")
            print(f"  Verify: {url}\n")
except Exception as e:
    print("Error LS:", e)

# MLAs
try:
    with open("data/winners.json", "r", encoding="utf-8") as f:
        mla_data = json.load(f)
        all_mlas = []
        for state, data in mla_data.items():
            all_mlas.extend(data.get("winners", []))
        sample_mlas = random.sample(all_mlas, 3)
        print("STATE MLAs")
        for mla in sample_mlas:
            name = mla.get("name", "Unknown")
            assets = mla.get("total_assets_cr", 0)
            liab = mla.get("total_liabilities_cr", 0)
            url = mla.get("affidavit_url", "No URL")
            print(f"- {name}")
            print(f"  Assets: Rs.{assets} Cr | Liabilities: Rs.{liab} Cr")
            print(f"  Verify: {url}\n")
except Exception as e:
    print("Error MLAs:", e)
