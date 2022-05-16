from re import T

from lib2to3.fixer_util import p2, p1

from flask import Blueprint, request, jsonify
from aiprofile_api.utils import api_checker
from dictionary_controller.dict_app import translate

aiTest = Blueprint("aiTest", __name__, url_prefix="/aiTest")


@aiTest.route('/', methods=["OPTIONS", "GET"])
@api_checker
def home():
    return "Home of aiprofile ", 200
@aiTest.route('/dictionary', methods=['POST'], strict_slashes=False)
def customers():
    payload = request.get_json()
    print(payload)
    word=payload["word"]
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    return jsonify({"output": output})
@aiTest.route('/calc', methods=['POST'], strict_slashes=False)
def rohit():
    payload = request.get_json()
    print(payload)
    if payload["operation"]=="add":
        return jsonify({"result":payload["num1"]+payload["num2"]})
    elif payload["operation"]=="sub":
        return jsonify({"result":payload["num1"]-payload["num2"]})
    elif payload["operation"]=="mul":
        return jsonify({"result":payload["num1"]*payload["num2"]})
    elif payload["operation"] == "div":
        return jsonify({"result": payload["num1"] / payload["num2"]})
@aiTest.route('/interest', methods=['POST'], strict_slashes=False)
def simple():
    payload = request.get_json()
    print(payload)
    p=payload["principle_amount"]
    r=payload["rate_of_interest"]
    t=payload["time"]
    if payload["operation"]=="simple_interest":

        simple_interest=(p*r*t)/100
        total_amount=p+simple_interest
        return jsonify({"simple_interest": simple_interest,"total_amount":total_amount})
    elif payload["operation"]=="compound_interest":
        compound_interest=00
        total_amount=p+compound_interest
        return jsonify({"compound_interest": compound_interest, "total_amount": total_amount})










