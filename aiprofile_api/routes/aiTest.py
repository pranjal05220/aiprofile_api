from flask import Blueprint, request, jsonify
from aiprofile_api.utils import api_checker
from check_numbers.find_prime import check_prime, prime_no_btw, num_add_mul_large, fib_series
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
    word = payload["word"]
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
    if payload["operation"] == "add":
        return jsonify({"result": payload["num1"] + payload["num2"]})
    elif payload["operation"] == "sub":
        return jsonify({"result": payload["num1"] - payload["num2"]})
    elif payload["operation"] == "mul":
        return jsonify({"result": payload["num1"] * payload["num2"]})
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

        # simple_interest=(principal_amount*rate_of_interest*time_period)/100
        # total_amount=principal_amount+simple_interest

        return jsonify({"simple_interest": simple_interest, "total_amount": total_amount})
    elif payload["operation"] == "compound_interest":
        compound_interest, total_amount = compound_find_interest(principal_amount, rate_of_interest, time_period)

        # compound_interest = principal_amount * (pow((1 + rate_of_interest / 100), time_period))
        # total_amount=principal_amount+compound_interest

        return jsonify({"a": compound_interest, "b": total_amount})


@aiTest.route('/check_prime', methods=['POST'], strict_slashes=False)
def prime():
    payload = request.get_json()
    num = payload["num"]
    num, status = check_prime(num)
    return jsonify({"number": num, "status": status})


@aiTest.route('/check_prime_no', methods=['POST'], strict_slashes=False)
def find_prime_no():
    payload = request.get_json()
    prime_lst = prime_no_btw(payload)
    return jsonify({"result": prime_lst})


@aiTest.route('/largest_no', methods=['POST'], strict_slashes=False)
def find_largest():
    payload = request.get_json()
    num1 = payload["num1"]
    num2 = payload["num2"]
    num3 = payload["num3"]
    if (num1 >= num2) and (num1 >= num3):
        return jsonify({"result": num1})
    elif (num2 >= num1) and (num2 >= num3):
        return jsonify({"result": num2})
    else:
        return jsonify({"result": num3})


@aiTest.route('/add_mul_large', methods=['POST'], strict_slashes=False)
def addition_mul_large():
    payload = request.get_json()
    addition, multiple, largest = num_add_mul_large(payload)
    return jsonify({"Addition": addition, "Multiply": multiple, "Largest": largest})


@aiTest.route('/find_factorial', methods=['POST'], strict_slashes=False)
def find_fact():
    payload = request.get_json()
    num = payload["num1"]
    fact = 1
    for i in range(fact, num + 1):
        fact = fact * i
    return jsonify({"factorial": fact})


@aiTest.route('/fibonacci', methods=['POST'], strict_slashes=False)
def fibo_number():
    payload = request.get_json()
    lst = fib_series(payload)
    return jsonify({"fibonacci": lst})


