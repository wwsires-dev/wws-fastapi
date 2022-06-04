from app.models.proof import ProofRequest
from fastapi import APIRouter
from app.services.proof import ProofService

router = APIRouter()
ps = ProofService()

@router.post("/proof", tags=["proof"])
async def get_proof_data(body: ProofRequest):
    proof_period_id = ps.get_proof_period_id(date=body.ProofDate)
    proof_data = ps.get_proof_data(proof_period_id=proof_period_id, traits=body.Traits, animals=body.Animals)

    return proof_data