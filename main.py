from fastapi import FastAPI
from routers import predict_rh

app = FastAPI()
app.include_router(predict_rh.router)