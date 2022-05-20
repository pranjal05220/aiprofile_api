from flask import Blueprint, request, jsonify
from aiprofile_api.utils import api_checker
from check_numbers.find_prime import check_prime
from dictionary_controller.dict_app import translate
from simple_interest_controller.simple_and_compund_interest import compound_find_interest, simple_find_interest, \
    find_prime_number

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


@aiTest.route('/check_prime_numbers', methods=['POST'], strict_slashes=False)
def prime_number():
    payload=request.get_json()
    prime_lst=find_prime_number(payload)
    return jsonify({"num":prime_lst})





@aiTest.route('/check_bigest_number', methods=['POST'], strict_slashes=False)
def bigest_number():
    payload = request.get_json()
    num1=payload["num1"]
    num2=payload["num2"]
    num3=payload["num3"]

    num1 = 10
    num2 = 20
    num3 = 30

    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    print("The largest number is", largest)
    return jsonify(({"largest_num": largest}))


@aiTest.route('/add_muliply_largest', methods=['POST'], strict_slashes=False)
def add():

    payload = request.get_json()

    num1 = payload["num1"]
    num2 = payload["num2"]
    num3 = payload["num3"]
    num4 = payload["num4"]

    sum = num1+num2+num3+num4

    print("The sum of given numbers is: ", sum)

    multiply = num1*num2*num3*num4

    print("The multiply of given numbers is: ", multiply)

    if (num1 >= num2) and (num1 >= num3) and(num1>=num4):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3)and(num2>=num4):
        largest = num2
    elif (num3 >= num1) and (num3 >= num2) and (num3>=num4):
        largest = num3
    else:
        largest = num4


    print("The largest number is", largest)
    return jsonify(({"largest_num": largest,"sum":sum,"multiply":multiply}))












@aiTest.route('/calc_simple_interest', methods=['POST'], strict_slashes=False)
def simple_interest():
    payload = request.get_json()
    print(payload)
    principal_amount=payload["principal_amount"]
    rate_of_interest=payload["rate_of_interest"]
    time_period=payload["time_period"]
    if payload["operation"]=="simple_interest":

        simple_interest=(principal_amount*rate_of_interest*time_period)/100
        total_amount=principal_amount+simple_interest

        return jsonify({"simple_interest":simple_interest,"total_amount":total_amount})
    elif payload["operation"]=="compound_interest":

        compound_interest=principal_amount* (pow((1 + rate_of_interest / 100), time_period))
        total_amount=principal_amount+compound_interest

        return jsonify({"compound_interest":compound_interest,"total_amount":total_amount})







