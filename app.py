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
@app.route("/order/")
def setorder():
    username = request.args.get("username")
    urrl = f"https://www.instagram.com/{username}/?__a=1"
    headerss = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "cookie": """ig_nrcb=1; mid=YgJSbwALAAHmIewldap9YYmjMNQK; ig_did=EE0B775C-5314-44C7-A75A-5947BE5C8354; csrftoken=jDkCCw6jjGaPu7T9ZQK9DFuw8f8yx5a5; ds_user_id=51270159671; sessionid=51270159671%3AvJg7Iq4dcjaZys%3A29; shbid="17337\05451270159671\0541675855363:01f7082d9b4d7150c6b5a276c369217fd8c8b9608ba783ce0f8296a07ffef035571c401a"; shbts="1644319363\05451270159671\0541675855363:01f7088e5d280d9e850e7790aeff1a7841fcd48bc57367fa9e9e989d869571aeef028aa0"; rur="LDC\05451270159671\0541675879635:01f7eb8abafdff41eb532e8356f89f62130e64612f61e5e844d8b43b7867e82a347ceeca""",
        "sec-ch-ua": """Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97""",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }
    req_id = requests.get(urrl, headers=headerss).json()
    pro = str(req_id['graphql']["user"]["profile_pic_url"])
    id = str(req_id['graphql']['user']['id'])

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
        "user_pk": "52083953133",
        "post_code": "",
        "action": "follow",
        "ids": "",
        "user_token": "62405463b9d23cb100461071bea3c5ca",
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
