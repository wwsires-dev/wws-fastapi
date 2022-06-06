from distutils.archive_util import make_archive
from app.services.database import Database

class BullService():

    def __init__(self) -> None:
        self.db = Database("TheRing")
        self.dmz = Database("DMZ")

    def get_global_id(self, id: str) -> str:
        global_id: str = None
        query = self.db.cursor.execute("SELECT dbo.GetGlobalId('" + id + "','M');")
        global_id = [row[0] for row in query]

        return global_id[0]

    def get_bull(self, global_id: str) -> dict:
        query = self.db.cursor.execute("SELECT * FROM dbo.GetAnimalBase('" + global_id + "', DEFAULT);")
        columns = [column[0] for column in query.description]
        bull = [dict(zip(columns, row)) for row in query]

        return bull[0]

    def get_marketed_bulls(self, breed_group: str, marketing_groups: str) -> list[dict]:
        
        query = self.db.cursor.execute("SELECT * FROM Api.BaseAnimal('" + breed_group + "', DEFAULT, '" + marketing_groups + "');")
        columns = [column[0] for column in query.description]
        bulls = [dict(zip(columns, row)) for row in query]

        bulls = list({value["Id"]:value for value in bulls}.values())
        
        return bulls

    def GetNewBulls(self):
        pass
        # sql: str = """
        #     SELECT DISTINCT
        #         RegId,
        #         CountryCode,
        #         BirthDate,
        #         Gender,
        #         Breed,
        #         ShortName,
        #         RegName,
        #         NaabCode,
        #         MarketingNaabCode
        #     FROM [DMZ].[Fenix].[Bull]
        #     WHERE AnimalSourceSystemId = 12
        #         AND GlobalId IS NULL 
        #         AND ShortName IS NOT NULL
        #         AND NaabCode IS NOT NULL
        # """
        # query = self.dmz.cursor.execute(sql)
        # columns = [column[0] for column in query.description]
        # bulls = [dict(zip(columns, row)) for row in query]

        # bulls = list({value["Id"]:value for value in bulls}.values())
        
        # return bulls
