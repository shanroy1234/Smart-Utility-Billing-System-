from fastapi import APIRouter
from app.billing_engine import calculate
from app.anomaly_service import detect

router=APIRouter(prefix='/billing')
@router.post('/generate')
def gen(d:dict):
    u=d['units']
    return {'units':u,'amount':calculate(u),'anomaly':detect(u)}
