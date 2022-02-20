import requests
import json
import flask
from flask import *
from bs4 import BeautifulSoup
import lxml,json,requests

app = Flask(__name__)
@app.route("/send")
def start():
    url = f"https://ingame.id.supercell.com/api/account/login"
    em = request.args.get("email")
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-US,en;q=0.5",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"ingame.id.supercell.com",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"none",
        "Sec-Fetch-User":"?1",
        "TE":"trailers",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }

    data = {
        "email":em,
        "rememeber":"true",
        "lang":"en",
        "game":"magic",
        "env":"prod"
    }
    req = requests.post(url,headers=headers,data=data).json()
    print(req)
    if req["ok"] == True:
        return "Done Send Code!"
    if req["ok"] == False:
        return "Not Linked With Clash :("
@app.route("/login")
def log():
    emaill = request.args.get("email")
    pin = request.args.get("pin")
    url2 = f"https://ingame.id.supercell.com/api/account/login.validate"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "ingame.id.supercell.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }
    data2 = {
        "email": emaill,
        "pin": int(pin)
    }
    reqq = requests.post(url2, headers=headers, data=data2).json()
    return reqq

import requests
import flask 
from flask import *

app = Flask(__name__)

@app.route("/f")
def Login_Facebook():
    email = request.args.get("email")
    passs = request.args.get("pass")
    s = requests.session()
    req = s.post(
        url = "https://b-api.facebook.com/method/auth.login",
        headers={
    'content-type':'application/x-www-form-urlencoded',
    'authority': 'b-api.facebook.com', 
    'accept-language': 'en-US,en;q=0.9', 
    'authorization': 'OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko) [FBAN/MessengerLite;FBAV/115.0.0.2.114;FBPN/com.facebook.mlite;FBLC/ar_EG;FBBV/257412622;FBCR/Orange - STAY SAFE;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi 7;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1369};]',
        },
        data=f"email={email}&password={passs}&credentials_type=password&error_detail_type=button_with_disabled&format=json&device_id=cdc4558c-4dd4-4fd0-9ba6-d09e0223d5e5&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&method=auth.login"
    )
    if "Invalid username or password" in req.text:
        data = {
        "status":"Invalid username or password",
        }
        return data
    elif "session_key" in req.text:
        data = {
        "status":"Success Login",
        }
        return data
    elif "User must verify" in req.text:
        data = {
        "status":"User must verify",
        }
        return data
    elif "User must confirm" in req.text:
        data = {
        "status":"User must confirm"
        }
        return data
    else:
        return "Error"
@app.route('/teleinfo/',methods=['GET'])
def telegraminfograber_page():

    search_query = str(request.args.get('url'))
    try:
        url = f'{search_query}?embed=1'
        views_table = []
        date_table = []
        title_table = []

        result = requests.get(f"{url}")
        src = result.content

        soup = BeautifulSoup(src, "lxml")

        views = soup.find_all("span", {"class": "tgme_widget_message_views"})
        g = str(views[0]).replace('</span>','').replace('<span class="tgme_widget_message_views">','')

        title = soup.find_all("div", {"class": "tgme_widget_message_text js-message_text"})
        for i in range(len(title)):
            title_table.append(title[i].text)

        date = soup.find_all("time")
        for i in range(len(date)):
            date_table.append(date[i].text)

        data_set = {'date': f'{date_table[0]}', 'msg': f'{title_table[0]}', 'views': f'{g}', 'stats': f'Loaded'}
        json_string = json.dumps(data_set, ensure_ascii=False)
        response = Response(json_string, content_type="application/json; charset=utf-8")
        return response
    except:
        data_set = {'stats': f'Error!'}
        return data_set
if __name__ =='__main__':
    app.run(debug=True)
