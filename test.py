import google_play_scraper as gps
import json

with open("scraped_packages.json", "r") as f:
    data = json.load(f)
    for app_title, packages in data.items():
        print(f"App: {app_title}")
        print("Scraped Packages:")
        for pkg_lst in packages:
            for pkg in pkg_lst:
                p = gps.app(pkg) 
                print(f"- {p["title"]}: ({p["appId"]})\n")