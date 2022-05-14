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