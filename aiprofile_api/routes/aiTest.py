import re
import datetime
from calendar import weekday, calendar
from datetime import date, datetime
from flask import Blueprint, request, jsonify
from sympy.concrete import delta

from aiprofile_api.utils import api_checker
from check_numbers.find_prime import check_prime, prime_no_btw, num_add_mul_large, fib_series
from dictionary_controller.dict_app import translate
from simple_interest_controller.simple_and_compund_interest import compound_find_interest, simple_find_interest
import math

from trignometry_controller.trig_controller import calc_trig_function

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
        return jsonify({"simple_interest": simple_interest, "total_amount": total_amount})
    elif payload["operation"] == "compound_interest":
        compound_interest, total_amount = compound_find_interest(principal_amount, rate_of_interest, time_period)
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


@aiTest.route('/inter_section1', methods=['POST'], strict_slashes=False)
def intersection():
    payload = request.get_json()
    lst1 = payload["lst1"]
    lst2 = payload["lst2"]
    inter_s = [value for value in lst1 if value in lst2]
    return jsonify({"Common_No": inter_s})


@aiTest.route('/tri_function', methods=['POST'], strict_slashes=False)
def trignometry():
    payload = request.get_json()
    result = calc_trig_function(payload)

    return jsonify({"result": result})

@aiTest.route('/f_sum', methods=['POST'], strict_slashes=False)
def sum_lst():
    payload=request.get_json()
    lst=payload["lst"]
    result=math.fsum(lst)
    return jsonify({"result":result})


@aiTest.route('/power_number', methods=['POST'], strict_slashes=False)
def power_fun():
    payload=request.get_json()
    num1=payload["num1"]
    num2=payload["num2"]
    result=math.pow(num1,num2)
    return jsonify({"result":result})



@aiTest.route('/square_root', methods=['POST'], strict_slashes=False)
def sqrt_fun():
    payload=request.get_json()
    x=payload["x"]
    result=math.sqrt(x)
    return jsonify({"result":result})


@aiTest.route('/prod_element', methods=['POST'], strict_slashes=False)
def product_fun():
    payload=request.get_json()
    ele=payload["ele"]
    result=math.prod(ele)
    return jsonify({"result":result})



@aiTest.route('/log_base_ten', methods=['POST'], strict_slashes=False)
def log_bten():
    payload=request.get_json()
    value=payload["value"]
    result=math.log10(value)
    return jsonify({"result":result})

@aiTest.route('/get_mod_fun', methods=['POST'], strict_slashes=False)
def mod_fun():
    payload=request.get_json()
    num1=payload["num1"]
    num2=payload["num2"]
    result=math.fmod(num1,num2)
    return jsonify({"result":result})


@aiTest.route('/get_factorial_fun', methods=['POST'], strict_slashes=False)
def facto_fun():
    payload=request.get_json()
    num=payload["num"]
    result=math.factorial(num)
    return jsonify({"result":result})


@aiTest.route('/get_exponential_fun', methods=['POST'], strict_slashes=False)
def exponential():
    payload=request.get_json()
    x=payload["x"]
    result=math.exp(x)
    return jsonify({"result":result})


@aiTest.route('/get_absolute', methods=['POST'], strict_slashes=False)
def absolute():
    payload=request.get_json()
    num=payload["num"]
    result=math.fabs(num)
    return jsonify({"result":result})


@aiTest.route('/get_floor', methods=['POST'], strict_slashes=False)
def floor_fun():
    payload=request.get_json()
    num=payload["num"]
    result=math.floor(num)
    return jsonify({"result":result})


@aiTest.route('/get_isclose_fun', methods=['POST'], strict_slashes=False)
def isclose_fun():
    payload=request.get_json()
    num1=payload["num1"]
    num2=payload["num2"]

    result=math.isclose(num1,num2)
    return jsonify({"result":result})



@aiTest.route('/find_latters', methods=['POST'], strict_slashes=False)
def find():
    payload = request.get_json()
    text=payload["txt"]
    x = re.findall("[a-m]", text)
    return jsonify({"result": x })


@aiTest.route('/find_moblie_num', methods=['POST'], strict_slashes=False)
def find_num():
    payload = request.get_json()
    text=payload["data"]
    regex = '\d+'
    match = re.findall(regex, text)
    return jsonify({"result":match})





@aiTest.route('/find_clear_data', methods=['POST'], strict_slashes=False)
def find_data():
    payload = request.get_json()
    text=payload["data"]
    match = re.sub(r"(http[s]?\://\S+)|([\[\(].*[\)\]])|([#@]\S+)|\n", "", text)
    return jsonify({"result":match})


@aiTest.route('/dateofbirth', methods=['POST'], strict_slashes=False)
def calculateAge():
    payload = request.get_json()
    birthDate = datetime.strptime (payload['date'],"%d/%m/%Y")
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
    return jsonify({"result":age})


@aiTest.route('/date_of_birth_in_days', methods=['POST'], strict_slashes=False)
def calculate_age_in_years_months_days():
    payload = request.get_json()

    day1 = datetime.strptime(payload["t1"],"%d/%m/%Y")
    day2 = datetime.strptime(payload["t2"],"%d/%m/%Y")
    delta1 = (day1-day2).days
    age1 = f"{delta1//365} year {(delta1%365)//30} month {(delta1%365)%30} day"
    return jsonify({"result":age1})



@aiTest.route('/find_day', methods=['POST'], strict_slashes=False)
def findDay():
    payload = request.get_json()
    born = datetime.strptime(payload["date"], "%d/%m/%Y")
    birth_day=born.strftime("%A")
    return jsonify({"result":birth_day})


@aiTest.route('/find_day_year', methods=['POST'], strict_slashes=False)
def findDayyear():
    payload = request.get_json()
    born = datetime.strptime(payload["date"], "%d/%m/%Y")
    birth_day=born.strftime("%A")
    birth_year = born.strftime("%d" " " "%B" " " "%Y")
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return jsonify({"year": age, "day": birth_day, "date_of_birth": birth_year})
