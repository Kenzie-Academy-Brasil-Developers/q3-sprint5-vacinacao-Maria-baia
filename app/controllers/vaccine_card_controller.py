from flask import request, current_app, jsonify
from app.models.vaccine_card_model import VaccineCardModel
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError

def create_vaccine_card():
    try:
        data = request.get_json()

        new_data = {
                "cpf": data["cpf"].title(),
                "name": data["name"].title(), 
                "vaccine_name": data["vaccine_name"].title(),
                "health_unit_name": data["health_unit_name"].title(),
                "first_shot_date": str(datetime.now().strftime("%d/%m/%Y %H:%M")).title(),
                "second_shot_date": datetime.today() + timedelta(days=+90)
            }

        for key, value in data.items():
            if type(value) != str:
                return jsonify({"msg": "fields must be strings"}), 400
            if key != "cpf" and key != "name" and key != "vaccine_name" and key != "health_unit_name":
                return jsonify({"msg": "wrong fields"}), 400

        if len(data["cpf"]) == 11 and data["cpf"].isnumeric():
            new_data["cpf"] = data["cpf"]
        else:
            return jsonify({"msg": "CPF is invalid"}), 400

        new_vaccine_card = VaccineCardModel(**new_data)

        current_app.db.session.add(new_vaccine_card)
        current_app.db.session.commit()

        return jsonify(new_vaccine_card), 201
    
    except KeyError:
        return jsonify({"msg": "missing fields"}), 400
    
    except IntegrityError:
        return jsonify({"msg": "CPF has already been registered"}), 409

def get_vaccined_cards():
    data = (VaccineCardModel.query.all())
   
    data = [
        { 
            "cpf":person.cpf,
            "name":person.name,
            "first_shot_date":person.first_shot_date,
            "second_shot_date":person.second_shot_date,
            "vaccine_name": person.vaccine_name,
            "health_unit_name":person.health_unit_name
        } for person in data
    ]

    return jsonify(data), 200