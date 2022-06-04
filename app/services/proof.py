from app.services.database import Database
from typing import Optional

class ProofService():

    def __init__(self) -> None:
        self.db = Database("TheRing")

    def get_proof_period_id(self, date: str):
        query = self.db.cursor.execute("SELECT Proof.GetOfficialEvalPeriodId('" + date + "',DEFAULT);")
        proof_period_id = [row[0] for row in query]

        return proof_period_id[0]

    def get_proof_data(self, proof_period_id: str, traits: str, animals: str):
        query = self.db.cursor.execute("SELECT * FROM Api.AnimalProof('" + proof_period_id + "','" + traits + "','" + animals + "');")
        columns = [column[0] for column in query.description]
        proof_data = [dict(zip(columns, row)) for row in query]

        return proof_data

    def get_trait_meta(self, country: str):
        query = self.db.cursor.execute("")
        columns = [column[0] for column in query.description]
        trait_meta = [dict(zip(columns, row)) for row in query]

        return trait_meta