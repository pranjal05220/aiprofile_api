from flask import Blueprint, request, jsonify
from aiprofile_api.utils import api_checker
from check_numbers.find_prime import check_prime
from dictionary_controller.dict_app import translate
from simple_interest_controller.simple_and_compund_interest import compound_find_interest, simple_find_interest

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

@aiTest.route('/calc_simple_interest', methods=['POST'], strict_slashes=False)
def simple_interest():
    payload = request.get_json()
    print(payload)
    principal_amount = payload["principal_amount"]
    rate_of_interest = payload["rate_of_interest"]
    time_period = payload["time_period"]
    if payload["operation"] == "simple_interest":

        simple_interest, total_amount = simple_find_interest(principal_amount, rate_of_interest, time_period)

        #simple_interest=(principal_amount*rate_of_interest*time_period)/100
        #total_amount=principal_amount+simple_interest

        return jsonify({"simple_interest":simple_interest,"total_amount": total_amount})
    elif payload["operation"] == "compound_interest":
        compound_interest, total_amount = compound_find_interest(principal_amount, rate_of_interest, time_period)

        #compound_interest = principal_amount * (pow((1 + rate_of_interest / 100), time_period))
        #total_amount=principal_amount+compound_interest

        return jsonify({"compound_interest":compound_interest,"total_amount": total_amount})


@aiTest.route('/check_prime', methods=['POST'], strict_slashes=False)
def prime():
    payload=request.get_json()
    num=payload["num"]
    num, status=check_prime(num)
    return jsonify({"number":num,"status": status})







