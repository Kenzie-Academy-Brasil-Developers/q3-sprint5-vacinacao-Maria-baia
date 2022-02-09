from flask import Blueprint

from app.routes.vaccine_card_blueprint import bp_vaccine_card

bp_api = Blueprint("bp_api", __name__)

bp_api.register_blueprint(bp_vaccine_card)