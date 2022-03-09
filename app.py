import requests

import json

import flask

from flask import *

from bs4 import BeautifulSoup

import lxml,json,requests

app = Flask(__name__)

@app.route("/or/")

def setorder():

    username = request.args.get("username")

    rq = requests.get(f"https://echoar.ml/Apimedia/infon.php?user={username}").json()["Info"]

    pro = rq['image']

    id = rq['account_id']

    header = {

        'X-Access': 'cafegram',

        'X-Version': '3',

        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',

        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)',

        'Host': 'apronista.ir',

        'Connection': 'Keep-Alive',

        'Accept-Encoding': 'gzip',

        'Content-Length': '609'

    }

    data = {

        "x_version": "3",

        "post_photo": "",

        "post_text": "",

        "speed": "false",

        "requested": "1000",

        "full_name": "",

        "post_pk": "",

        "user_pk": "51993501593",

        "post_code": "",

        "action": "follow",

        "ids": "",

        "user_token": "659cdce96cfed3f3d8e2e9fb797b3df3",

        "pk": f"{id}",

        "user_photo": f"""{pro}""",

        "username": f"{username}"

    }

    req = requests.post("http://apronista.ir/api/v1/addOrder.php", headers=header, data=data).text

    if "success" in req:

        sp = {

            "status":"ok",

            "data":"Done Send 1000 Follow"

        }

        return sp

    elif "nok" in req:

        sp = {

            "status": "nok",

            "data": "Error"

        }

        return sp
    if __name__ =='__main__':

    app.run(debug=True)

    
       



    
