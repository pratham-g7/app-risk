import risk
import json
from helpers.name_similarity import name_similarity as name_sim
from helpers.icon_similarity import icon_similarity as icon_sim
from helpers.scraper import App 
from scraper.verified_apps import ver_apps  

def assess_risk():
    with open("data/scraped_packages.json", "r") as f:
        scraped_data = json.load(f)
    for ver_app, (app_title, packages) in zip(ver_apps, scraped_data.items()):
        print(f"Assessing Risk for App: {app_title}")

        for pkg_lst in packages:
            for pkg in pkg_lst:
                pkg_obj = App(pkg)
                score = risk.risk_score(
    title_distance=name_sim(app_title, str(pkg_obj.metadata.get("title", ""))),
    icon_similarity=icon_sim(ver_app.metadata.get("icon", ""), pkg_obj.metadata.get("icon", "")),
    dev_mismatch=(0 if ver_app.metadata.get("dev") == pkg_obj.metadata.get("dev") else 1),
    install_factor=min(1.0, (ver_app.metadata.get("installs") or 1) / (pkg_obj.metadata.get("installs") or 1))
)

                print(f"- Package: {pkg}, Risk Score: {round(100-(score*100), 2)}%")
        print("\n")


assess_risk()