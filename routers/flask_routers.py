from flask import Blueprint, request, jsonify
from services.predict_rh import PredictRH

account_api = Blueprint('account_apu', __name__)


@account_api.route('/account', methods=["POST"])
def predict_ibm():
    dados = request.get_json()
    t = PredictRH().predict([dados])
    return {"response":str(t[0])}
