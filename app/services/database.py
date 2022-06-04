import pyodbc as odbc
import os
import json

class Database():
    def __init__(self, database: str) -> None:
        ROOT_DIR = os.path.dirname(__file__)
        CONFIG_PATH = os.path.join(ROOT_DIR, "config.json")
        config_file = open(CONFIG_PATH)
        config = json.load(config_file)

        c = [item for item in config if item.get(database)]
        config = c[0][database]
        
        self.connection = None
        self.connection = odbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + config["server"] + ';DATABASE=' + config["database"] + ';UID='+ config["username"] + ';PWD=' + config["password"] + ';TrustServerCertificate=yes')
        self.cursor = self.connection.cursor()