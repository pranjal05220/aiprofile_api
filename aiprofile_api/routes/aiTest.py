from flask import Blueprint, request
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
