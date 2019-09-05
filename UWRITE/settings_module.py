import yaml

class GetSettings(object):
    """
        Класс для чтения конфигов с yaml
    """

    def __init__(self):
        self.settings = ""
        self.get_settings()

    def get_settings(self):
        with open("./yaml/settings.yml", 'r') as stream:
            self.settings = yaml.safe_load(stream)

class GetCookies(object):
    """
    Класс для чтения cookies из yaml
    """
    
    def __init__(self):
        self.cookies = ""
        self.get_cookies()

    def get_cookies(self):
        with open("./yaml/cookies.yml", 'r') as stream:
            self.cookies = yaml.safe_load(stream)

class SetCookies(object):
    """
    Класс для записи cookies в yaml
    """
    
    def __init__(self, cookies_dict):
        self.cookies_dict = cookies_dict
        self.set_cookies()

    def set_cookies(self):
        with open('./yaml/cookies.yml', 'w') as outfile:
            yaml.dump(self.cookies_dict, outfile)