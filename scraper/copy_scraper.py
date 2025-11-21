import google_play_scraper as gps
from scraper.verified_apps import ver_apps
import json


def scraper():
    scraped_pkgs = [
        [
            list(set(gps.app(app_obj["appId"] or ver_apps[0].package_name)["appId"] 
            for app_obj in gps.search(str(app.metadata["title"]), n_hits=30)))[5:]
        ]
        for app in ver_apps
    ]

    return scraped_pkgs

def cache_data():
    with open("scraped_packages.json", "w") as f:
        dat = {}
        for cmp, app_pkgs in zip(ver_apps, scraper()):
           dat.update({cmp.metadata["title"]: app_pkgs})
        json.dump(dat, f, indent=4)
                
cache_data()
