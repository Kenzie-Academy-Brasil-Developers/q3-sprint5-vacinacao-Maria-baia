from flask import Blueprint

from app.controllers.vaccine_card_controller import create_vaccine_card, get_vaccined_cards

bp_vaccine_card = Blueprint("bp_vaccine_card", __name__, url_prefix="/vaccinations")

bp_vaccine_card.post("")(create_vaccine_card)
bp_vaccine_card.get("")(get_vaccined_cards)