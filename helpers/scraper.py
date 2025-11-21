import google_play_scraper as gps

class App:
    def __init__(self, package_name):
        self.package_name = package_name
        self.data = gps.app(package_name)
        self.metadata = {
            "title": self.data.get("title"),
            "dev": self.data.get("developer"),
            "icon": self.data.get("icon"),
            "installs": self.data.get("realInstalls"),
        }

    def get_data(self, key):
        return self.data.get(key, None)