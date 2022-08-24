# from fastapi import FastAPI
# from routers import predict_rh

from flask import Flask
from routers.flask_routers import account_api

# app = FastAPI()
# app.include_router(predict_rh.router)

app = Flask(__name__)
app.register_blueprint(account_api)

if __name__ == '__main__':
    app.run(debug=True)
