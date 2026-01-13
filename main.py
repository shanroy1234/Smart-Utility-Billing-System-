from fastapi import FastAPI
from app.routers import users, meters, billing, payments

app = FastAPI(title="Smart Utility Billing System")
app.include_router(users.router)
app.include_router(meters.router)
app.include_router(billing.router)
app.include_router(payments.router)
