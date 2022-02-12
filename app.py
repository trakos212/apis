from flask import Flask,request
from InstagramIG import SidraELEzz
import json,requests,random,os,time
from telegraph import Telegraph
import requests,user_agent,json,flask,bs4,os
from user_agent import generate_user_agent
from flask import Flask,jsonify
from flask import *
from bs4 import BeautifulSoup
from datetime import date
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route('/',methods=['GET'])
def home_page():
    return redirect("https://dev-apis-x.pantheonsite.io/api/Website/", code=302)
@app.route('/Token-Generator')
def home_age():
    chars1 = "AaBbCcDdEeFfGgaHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890"
    u1 = str("".join(random.choice(chars1)for i in range(35)))
    char = "1234567890"
    u = str("".join(random.choice(char)for i in range(10)))
    Token = u+':'+u1
    data = {'data':f'{Token}','result':'loaded'}
    return data
@app.route('/Gmail')
def Gmail():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    name = str("".join(random.choice(chars)for i in range(7)))
    email = name+'@gmail.com'
    data = {'data':f'{email}','result':'true'}

    return data
@app.route('/Yahoo')
def Gmailx():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    name = str("".join(random.choice(chars)for i in range(7)))
    email = name+'@yahoo.com'
    data = {'data':f'{email}','result':'true'}
    return data
@app.route('/Visa-gen')
def bin():
        bin = str(request.args.get('bin'))
        chars = "1234567890"
        v = str("".join(random.choice(chars)for i in range(10)))
        date1 = str("".join(random.choice('123456789')for i in range(1)))
        date2 = str("".join(random.choice('3456789')for i in range(1)))
        cvc = str("".join(random.choice(chars)for i in range(3)))
        visa = f'{bin}{v}|0{date1}|202{date2}|{cvc}'
        data = {'info':{'data':f'{visa}','result':'loaded'}}
        return data
@app.route('/Visa')
def bin_v2():
    chars = "1234567890"
    v0 = str("".join(random.choice(chars)for i in range(4)))
    v = str("".join(random.choice(chars)for i in range(10)))
    date1 = str("".join(random.choice('123456789')for i in range(1)))
    date2 = str("".join(random.choice('3456789')for i in range(1)))
    cvc = str("".join(random.choice(chars)for i in range(3)))
    visa = f'{random.choice("345")}6{v0}{v}|0{date1}|202{date2}|{cvc}'
    data = {'info':{'data':f'{visa}','result':'loaded'}}
    return data

@app.route('/Bin')
def api():
    chars0 = "1234567890"
    v00 = str("".join(random.choice(chars0)for i in range(4)))
    binn = f'56{v00}'
    data = {'info':{'data':f'{binn}','result':'loaded'}}
    return data
@app.route('/upload-telegraph')
def api_x():
    title = request.args.get('title')
    content = request.args.get('content')
    telegraph = Telegraph()
    telegraph.create_account(short_name='Vodka_Tools')

    response = telegraph.create_page(
   f'{title}',
        html_content=f'<p>{content}</p>'
    )
    x = (response['url'])
    data_x = {'ok':True,'result':{"data":f"{x}","status":"loaded"}}
    return data_x
@app.route('/Insta-login', methods=['GET'])
def Login():
    user = request.args.get("username")
    pas = request.args.get("password")
    Lo = SidraELEzz.Instalogin(str(user),str(pas))
    if Lo == True:
        data = {'data':'Good Login','result':'bad'}
        return data
    elif Lo == False:
        data = {'data':'Secure','result':'loaded'}
        return data
    else:
        data = {'data':'Error In Login','result':'bad'}
        return data
@app.route('/info/tiktok', methods=['GET'])
def info():
	username = request.args.get('user')
	url = 'https://www.tiktok.com/@'+str(username)+'?lang=en'
	headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	'cookie' : 's_v_web_id=verify_4759e77ec70b30f5809b99b4e83cf170; tt_csrf_token=UnnTT-BD3b77BER0ScMT23x9; tt_webid_v2=6972528352738199042; tt_webid=6972528352738199042; MONITOR_WEB_ID=6972528352738199042; csrf_session_id=33dd9ae2d7064521b1fb68c47fb6e376; ttwid=1%7CwLimK0e14CMaCXiLsX2myGQvJoR3fo915olavJk5Dj8%7C1623418284%7Ce18f90ac79a745872544fd1583a806821d5f6c9158b0d627195c391e1826811a; R6kq3TV7=AMcrRft5AQAAjVJfEPehKE83G62yRxwPcWPaXYFikZR7GX1aQHzgFfgvUVYW|1|0|2b554837c6bb50a519a30dbd9d5993dc6bc9a899; ak_bmsc=81F43ED7B422ED308CE38925766575B825EEFE85C4210000AE65C360177EFA1B~pl1L8RCHdpnfcXaxKe2pz/rrFGQ7AvIDfN7D/22TzpTU+jZhxDJTPJeeBqZzBzFebXtRYd+rf7S7OmBWLe/P+NNTeXnw6pCQxbC3oIFuwYRtUEK/JN2GEhm+/Aft3RoUgU4e/U9MIt7FtXUm521joEAelJCNASPG7sXkCL9Gquc/S7Ss/uOSbUow59iqm/DE20qw90c3qyotU354d2k5uT/ZtjaXyF1fKW5RtVkjiSo2o=; bm_sz=37D69FC94E991FC2E9B16E331298202E~YAAQhf7uJch1QPd5AQAAtjFF+wwIPFmp+JnukUWFwWqe7X7doAuSddcEaF98dBdy4UG5HI0g+qLiAFukmWs9uJR48l9ItBNHUpPwRrW2gnAfasr0c7zqprBzAMgrMT0jqPEG2GenpL5lp6psMYSUW2agxDZY++1VmDyejBjQGqRh/g4VVjEnSpZ1kTrkah0q; _abck=3BB0FC28EA3D19A3D635197B489889C5~-1~YAAQhf7uJcl1QPd5AQAAtjFF+wZF5KnpMJ3JntFWraZlabgy8zYpHCGWOOOlZvd9iDaNjP0aLxrOLfernQM/KlnKVqllWNtTsnVatlXA9uvEtOcTzhLFiEoynT/MfV6GtNEzx54dOdnFXliM7F0ifN4WMqNvlQddCjSTp4ESCxMCZ/wixpiJAj7fhh+lqObndimxpSyFkdDwKKL/2r+zoMxUTUz7vga3x19kWzjEHbFfRsUsKEsq8Kz945ZlHNTbYsGhuLJbYW7sfixqbGe5AnJcU+H/JwGPEgW3fCJiF7lWCaAm9zR6iwUoi6HfM4QlxsM2eNX0hXyFm75mwFrP5GDjVH5PWn9cpsoovHfhXb9cDwjlN2L0gvqUPCU=~-1~-1~-1',
	'referer': 'https://www.tiktok.com/@'+str(username)+'?lang=en',
	'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
	'sec-ch-ua-mobile': '?0',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'none',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': generate_user_agent() }

	response = requests.get(url, headers=headers)
	if(response.status_code == 200 and response.text):
		soup = BeautifulSoup(response.text, 'html.parser')
		Followers = soup.find('strong',{'data-e2e':'followers-count'}).string
		following = soup.find('strong',{'data-e2e':'following-count'}).string
		likes = soup.find('strong',{'data-e2e':'likes-count'}).string
		bio = soup.find('h2',{'data-e2e':'user-bio'}).string
		get_info = soup.find(id="Person").string
		name = get_info[0:175].split(':')[4].replace('","description"','').split('"')[1]
		data_json = {"data":{"Name":f"{name}","Followers":f"{Followers}","Following":f"{following}","Likes":f"{likes}","Bio":f"{bio}","UserName":f"{username}","status":"Taken User"}}
		return data_json
	else:
		data_json = {"data":{"Name":"Error","UserName":f"{username}","status":"Taken User"}}
		return data_json
@app.route('/user-agent')
def arabicge():
    r = str(''.join((generate_user_agent() for i in range(1))))
    data_set = {'data':f'{r}','status':'loaded'}
    return data_set
@app.route('/Token/Info', methods=['GET'])
def infotokxx():
    token = request.args.get('token')
    data = requests.get(f'https://api.telegram.org/bot{token}/getme').json()
    bot_id = data['result']['id']
    bot_firstname = data['result']['first_name']
    bot_username = data['result']['username']
    data_set = {'ok':True,'result':{'id':f'{bot_id}','first_name':f'{bot_firstname}','username':f'@{bot_username}','status':'loaded'}}
    return data_set
@app.route('/Random/Account', methods=['GET'])
def testerx():
    chars1 = 'abcdefghijklmnopqrstuvwxyz'
    chars = 'abcdefghijklmnopqrstuvwxyz%_@*#$1234567890'
    num = str("".join(random.choice(chars1)for i in range(4)))
    num_x = str("".join(random.choice(chars)for i in range(8)))
    num_xx = str("".join(random.choice(chars)for i in range(4)))
    user = f'{num}{num_xx}'
    Pass = num_x
    data_set = {'result':{'pass':f'{Pass}','user':f'{user}'}}
    return data_set
@app.route('/twitter/Info', methods=['GET'])
def infotwi():
    user = request.args.get('user')
    url = requests.get(f'https://sidraapi.pythonanywhere.com/v1/api/info/account/twitter/?username={user}').json()
    bio = url['Bio']
    folo = url['followers']
    pic = url['profile']
    loca = url['location']
    Date = url['Date']
    frend = url['friends']
    data_set = {'ok':True,'result':{'Bio':f'{bio}','Date':f'{Date}','Followers':f'{folo}','Friends':f'{frend}','Location':f'{loca}','profile-pic':f'{pic}','name':f'{url["name"]}','user-name':f'{url["username"]}','status':'loaded'}}
    return data_set
@app.route('/Outlook')
def outlooklx():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    name = str("".join(random.choice(chars)for i in range(7)))
    email = name+'@outlook.com'
    data = {'info':{'data':f'{email}','result':'true'}}
    return data
@app.route('/Hotmail')
def Gmaixxlx():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    name = str("".join(random.choice(chars)for i in range(7)))
    email = name+'@hotmail.com'
    data = {'info':{'data':f'{email}','result':'true'}}
    return data
@app.route('/info/tiktok-v2', methods=['GET'])
def infoxx():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    username = str("".join(random.choice(chars)for i in range(4)))
    url = 'https://www.tiktok.com/@'+str(username)+'?lang=en'
    headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	'cookie' : 's_v_web_id=verify_4759e77ec70b30f5809b99b4e83cf170; tt_csrf_token=UnnTT-BD3b77BER0ScMT23x9; tt_webid_v2=6972528352738199042; tt_webid=6972528352738199042; MONITOR_WEB_ID=6972528352738199042; csrf_session_id=33dd9ae2d7064521b1fb68c47fb6e376; ttwid=1%7CwLimK0e14CMaCXiLsX2myGQvJoR3fo915olavJk5Dj8%7C1623418284%7Ce18f90ac79a745872544fd1583a806821d5f6c9158b0d627195c391e1826811a; R6kq3TV7=AMcrRft5AQAAjVJfEPehKE83G62yRxwPcWPaXYFikZR7GX1aQHzgFfgvUVYW|1|0|2b554837c6bb50a519a30dbd9d5993dc6bc9a899; ak_bmsc=81F43ED7B422ED308CE38925766575B825EEFE85C4210000AE65C360177EFA1B~pl1L8RCHdpnfcXaxKe2pz/rrFGQ7AvIDfN7D/22TzpTU+jZhxDJTPJeeBqZzBzFebXtRYd+rf7S7OmBWLe/P+NNTeXnw6pCQxbC3oIFuwYRtUEK/JN2GEhm+/Aft3RoUgU4e/U9MIt7FtXUm521joEAelJCNASPG7sXkCL9Gquc/S7Ss/uOSbUow59iqm/DE20qw90c3qyotU354d2k5uT/ZtjaXyF1fKW5RtVkjiSo2o=; bm_sz=37D69FC94E991FC2E9B16E331298202E~YAAQhf7uJch1QPd5AQAAtjFF+wwIPFmp+JnukUWFwWqe7X7doAuSddcEaF98dBdy4UG5HI0g+qLiAFukmWs9uJR48l9ItBNHUpPwRrW2gnAfasr0c7zqprBzAMgrMT0jqPEG2GenpL5lp6psMYSUW2agxDZY++1VmDyejBjQGqRh/g4VVjEnSpZ1kTrkah0q; _abck=3BB0FC28EA3D19A3D635197B489889C5~-1~YAAQhf7uJcl1QPd5AQAAtjFF+wZF5KnpMJ3JntFWraZlabgy8zYpHCGWOOOlZvd9iDaNjP0aLxrOLfernQM/KlnKVqllWNtTsnVatlXA9uvEtOcTzhLFiEoynT/MfV6GtNEzx54dOdnFXliM7F0ifN4WMqNvlQddCjSTp4ESCxMCZ/wixpiJAj7fhh+lqObndimxpSyFkdDwKKL/2r+zoMxUTUz7vga3x19kWzjEHbFfRsUsKEsq8Kz945ZlHNTbYsGhuLJbYW7sfixqbGe5AnJcU+H/JwGPEgW3fCJiF7lWCaAm9zR6iwUoi6HfM4QlxsM2eNX0hXyFm75mwFrP5GDjVH5PWn9cpsoovHfhXb9cDwjlN2L0gvqUPCU=~-1~-1~-1',
	'referer': 'https://www.tiktok.com/@'+str(username)+'?lang=en',
	'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
	'sec-ch-ua-mobile': '?0',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'none',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': generate_user_agent() }

    response = requests.get(url, headers=headers)
    if(response.status_code == 200 and response.text):
        soup = BeautifulSoup(response.text, 'html.parser')
        Followers = soup.find('strong',{'data-e2e':'followers-count'}).string
        following = soup.find('strong',{'data-e2e':'following-count'}).string
        likes = soup.find('strong',{'data-e2e':'likes-count'}).string
        bio = soup.find('h2',{'data-e2e':'user-bio'}).string
        get_info = soup.find(id="Person").string
        name = get_info[0:175].split(':')[4].replace('","description"','').split('"')[1]
        data_json = {"data":{"UserName":f"{username}","Name":f"{name}","Followers":f"{Followers}","Following":f"{following}","Likes":f"{likes}","Bio":f"{bio}","status":"Taken User"}}
        return data_json
    else:
        data_json = {"data":{"UserName":f"{username}","Name":"Error","status":"Band or Valid User"}}
        return data_json
@app.route('/Hard/Password')
def hardpass():
    chars = 'abcdefghijklmnopqrstuvwxyz%_@*#$1234567890'
    num = str("".join(random.choice(chars)for i in range(8)))
    Pass = num
    data_set = {'info':{'data':f'{Pass}','status':'loaded'}}
    return data_set
@app.route('/tiktok/check', methods=['GET'])
def arabicfixpagexxb():
    user = request.args.get('user')
    head ={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
'cache-control': 'max - age = 0',
'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    Response = requests.get(f'https://www.tiktok.com/@{user}?', headers=head)
    if Response.status_code == 404:
        data = {'info':{'data':'Valid User','status':'loaded'}}
        return data
    else:
        data = {"info":{"data":"Taken User","status":"loaded"}}
        return data
@app.route('/Host/Maker', methods=['GET'])
def arabicfixpagexxgb():
        us = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM') for i in range(6))
        passw = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#') for i in range(14))
        eml = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM') for i in range(7))
        user = us
        password = passw
        email = f'{eml}@gmail.com'
        url = 'https://www.pythonanywhere.com/registration/register/beginner/'
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '256',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'cookie_warning_seen=True; csrftoken=QPldz6eClLRiMvczJ3gRu8FlCP45cbZzoGhc1tOUgsQZ381qvNJk2tXt2KVqfoeZ; sessionid=oag2fm4ea17dklxonpvmq26v93xtzuok; _ga=GA1.1.912772697.1641589928; _gid=GA1.1.1863051091.1641589928; _gat=1',
        'Host': 'www.pythonanywhere.com',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/registration/register/beginner/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        }
        data = {
        'csrfmiddlewaretoken': 'X3UhBXp7o52VRzA63M9InnvoGSwZq0uivUQg3kZpjM1C8cpXPwCbVINw6NnktdJI',
        'username': user,
        'email': email,
        'password1': password,
        'password2': password,
        'tos': 'on',
        'recaptcha_response_token_v3': '',
        }
        re = requests.post(url,headers=headers,data=data)
        data_set = {'ok':'true','status':'loaded','result':{'email':f'{email}','pass':f'{password}','user':f'{user}','login':'https://www.pythonanywhere.com/login/','Website-Url':f'http://{user}pythonanywhere.com/'}}
        return data_set
@app.route('/Host/Maker/v2', methods=['GET'])
def arabicfixpagexjxbx():
                url = 'https://dashboard.pantheon.io/register'
                head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '199',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.2.1442978344.1631760627; _gid=GA1.2.801729137.1631760627; __utmc=97458314; __utmz=97458314.1631760627.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _mkto_trk=id:316-GSV-089&token:_mch-dashboard.pantheon.io-1631760627584-29222; ajs_anonymous_id=%22fcf4b685-5a66-43f6-b3d5-6278cba8fcdf%22; pantheon_tracking=%7B%22utm_source%22%3A%22No%20UTM%22%2C%22utm_medium%22%3A%22No%20UTM%22%2C%22utm_device%22%3A%22No%20UTM%22%2C%22utm_content%22%3A%22No%20UTM%22%2C%22utm_campaign%22%3A%22No%20UTM%22%2C%22utm_term%22%3A%22No%20UTM%22%2C%22utm_ad_group_name%22%3A%22No%20UTM%22%2C%22dtl%22%3A%22%22%2C%22referrer_url%22%3A%22%22%7D; pantheon_tracking=%7B%22utm_source%22%3A%22No%20UTM%22%2C%22utm_medium%22%3A%22No%20UTM%22%2C%22utm_device%22%3A%22No%20UTM%22%2C%22utm_content%22%3A%22No%20UTM%22%2C%22utm_campaign%22%3A%22No%20UTM%22%2C%22utm_term%22%3A%22No%20UTM%22%2C%22utm_ad_group_name%22%3A%22No%20UTM%22%2C%22dtl%22%3A%22%22%2C%22referrer_url%22%3A%22%22%7D; __utma=97458314.1442978344.1631760627.1631760627.1631763283.2; OptanonAlertBoxClosed=2021-09-16T03:35:41.701Z; _vwo_uuid_v2=D85586077E6C3CC18432718487186C7FF|db298eece003160e44d7fe53c2338d53; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D85586077E6C3CC18432718487186C7FF; _vwo_ds=3%241631763524%3A1.13392115%3A%3A; _mkto_trk=id:316-GSV-089&token:_mch-pantheon.io-1631763528037-90938; _biz_sid=2a927e; _fbp=fb.1.1631763533718.266134017; _biz_uid=07537b0f05734e6795dddd255832c1b5; intercom-id-xkegk7cr=86cffc78-56ca-4239-9750-aefa9bb43ff3; intercom-session-xkegk7cr=; OptanonAlertBoxClosed=2021-09-16T03:39:16.803Z; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Frm%22%3A%221%22%7D; _vis_opt_exp_135_combi=1; _vis_opt_exp_141_combi=2; _vis_opt_exp_116_combi=2; _vis_opt_exp_116_goal_210=1; _biz_ABTestA=%5B1054094750%5D; _vis_opt_exp_141_goal_200=1; _vis_opt_exp_135_goal_200=1; _vis_opt_exp_116_goal_200=1; _vis_opt_exp_141_goal_212=1; _vis_opt_exp_135_goal_212=1; _vis_opt_exp_116_goal_212=1; _vis_opt_exp_141_goal_213=1; _vis_opt_exp_135_goal_213=1; _vis_opt_exp_116_goal_213=1; _csrf=eOFR7mv0u3d1sWGlWFzFQ1nK; __utmt=1; __utmb=97458314.4.10.1631763283; OptanonConsent=isIABGlobal=false&datestamp=Thu+Sep+16+2021+07%3A05%3A05+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.0.0&landingPath=NotLandingPage&groups=0_224028%3A1%2C1%3A1%2C2%3A1%2C0_224029%3A1%2C3%3A1%2C0_224030%3A1%2C0_224031%3A1%2C4%3A1%2C0_224032%3A1%2C0_224034%3A1%2C0_224036%3A1%2C0_224037%3A1%2C0_224039%3A1%2C0_224040%3A1%2C0_224041%3A1%2C0_224042%3A1%2C0_224043%3A1%2C0_224044%3A1%2C0_224045%3A1%2C0_224046%3A1%2C0_224047%3A1%2C0_263828%3A1%2C0_263832%3A1%2C0_224048%3A1%2C0_263836%3A1%2C0_263840%3A1%2C0_264785%3A1%2C0_263827%3A1%2C0_263831%3A1%2C0_224035%3A1%2C0_268794%3A1%2C0_263835%3A1%2C0_263839%3A1%2C0_263843%3A1%2C0_268773%3A1%2C0_268777%3A1%2C0_224038%3A1%2C0_263826%3A1%2C0_263830%3A1%2C0_263834%3A1%2C0_263838%3A1%2C0_268772%3A1%2C0_263842%3A1%2C0_263829%3A1%2C0_263833%3A1%2C0_263837%3A1%2C0_263292%3A1%2C0_263841%3A1%2C0_268771%3A1&consentId=61e45c1e-77a9-414d-8432-fd89a4b20575&AwaitingReconsent=false; OptanonConsent=isIABGlobal=false&datestamp=Thu+Sep+16+2021+07%3A05%3A41+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.7.0&landingPath=NotLandingPage&groups=0_224028%3A1%2C1%3A1%2C2%3A1%2C0_224029%3A1%2C3%3A1%2C0_224030%3A1%2C0_224031%3A1%2C4%3A1%2C0_224032%3A1%2C0_224034%3A1%2C0_224036%3A1%2C0_224037%3A1%2C0_224039%3A1%2C0_224040%3A1%2C0_224041%3A1%2C0_224042%3A1%2C0_224043%3A1%2C0_224044%3A1%2C0_224045%3A1%2C0_224046%3A1%2C0_224047%3A1%2C0_263828%3A1%2C0_263832%3A1%2C0_224048%3A1%2C0_263836%3A1%2C0_263840%3A1%2C0_264785%3A1%2C0_263827%3A1%2C0_263831%3A1%2C0_224035%3A1%2C0_268794%3A1%2C0_263835%3A1%2C0_263839%3A1%2C0_263843%3A1%2C0_268773%3A1%2C0_268777%3A1%2C0_224038%3A1%2C0_263826%3A1%2C0_263830%3A1%2C0_263834%3A1%2C0_263838%3A1%2C0_268772%3A1%2C0_263842%3A1%2C0_263829%3A1%2C0_263833%3A1%2C0_263837%3A1%2C0_263292%3A1%2C0_263841%3A1%2C0_268771%3A1&consentId=61e45c1e-77a9-414d-8432-fd89a4b20575&AwaitingReconsent=false; _vwo_sn=0%3A6%3A%3A%3A1; _uetsid=9baee920169f11ecb2033115ddab655c; _uetvid=9bb06660169f11ec8868995204769a69; _gat=1; _biz_nA=50; _biz_pendingA=%5B%22m%2Fblr%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26frm_c%3D-1955448038%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DonClick-Button%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171511%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D47%22%2C%22m%2Ffrm%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DAjaxIntercept%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171652%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D48%22%2C%22m%2Ffrm%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26frm_c%3D-1955448038%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DsubmitJQ%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171842%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D49%22%5D',
            'Host': 'dashboard.pantheon.io',
            'Origin': 'https://pantheon.io',
            'Pragma': 'no-cache',
            'Referer': 'https://pantheon.io/',
            'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
                }
                num = random.choice('1234567890')
                num2 = random.choice('1234567890')
                eml = f'Vodka{num}{num2}@gmail.com'
                data = {
            'pda_campaign':'{}',
            'firstname': 'Vodka',
            'lastname': 'Tools',
            'company': 'PHP-Hosting',
            'title': '{}',
            'email':f'{eml}',
            'password': 'QX#kC_Gdk%Z',
            'agency': 'agency',
            'edu': 'edu',
            'tos': 'tos',
            '_csrf': 'bl25T4Su-VrvpiI0Pjme3ObuIig4Q08ZrdNs',
                        }
                R = requests.post(url,headers=head,data=data)
                passw = 'QX#kC_Gdk%X'
                weblogin = 'https://pantheon.auth0.com/login?state=hKFo2SBKblczb3JaS3V6RHBTdnRUME5SbWdaMXFkRnVQaVljUKFupWxvZ2luo3RpZNkgU3M4S3B6YTJlUGRQaU1GRUNlaTJ3aDlfR1VDbU1mV06jY2lk2SBxOWZXajl4blB4NE9BQVk5SU5ZZGNmaVlJVGtHdmFIcg&client=q9fWj9xnPx4OAAY9INYdcfiYITkGvaHr&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fdashboard.pantheon.io%2Fauth%2Fcallback&scope=login%20openid%20pantheon&connection='
                data = {'ok':'true','result':{'Email':eml,'Password':passw,'status':'loaded','Login-Url':weblogin}}
                return data
@app.route('/Hadith',methods=['GET'])
def hadith():
    req = requests.get("https://pastebin.com/raw/AmRLni6r").json()  

    hadith = random.choice(req)
    data = {'info':{'data':hadith,'status':'loaded'}}
    json_data = json.dumps(data, ensure_ascii=False)    
    response = Response(json_data, content_type="application/json; charset=utf-8")         
    return response
@app.route('/insta/login/v2',methods=['GET'])
def login_insta(): 
    user = request.args.get('user')
    passw = request.args.get('pass')
    headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '321','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YMEcQAALAAEv7JAHx0HGAT9oOg5e; ig_did=BBD1FACB-65E8-433F-BB27-1554B5DC41E6; ig_nrcb=1; shbid=13126; shbts=1624283106.1767957; rur=PRN; csrftoken=kKQkGJjUqYTQVCewP9FEp6SZypK8iiSt','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','x-asbd-id': '437806','x-csrftoken': 'kKQkGJjUqYTQVCewP9FEp6SZypK8iiSt','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgSX-','x-instagram-ajax': 'a90c0f3c9877','x-requested-with': 'XMLHttpRequest',}
    data={'username': user,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{passw}','queryParams': '{}','optIntoOneTap': 'false','stopDeletionNonce': '','trustedDeviceRecords': '{}',}  
    
    GO=requests.post('https://www.instagram.com/accounts/login/ajax/',headers=headers,data=data).text
    if '"authenticated":true' in GO:
        return {'ok':'true','result':{'data':'Done Login','Username':user,'Password':passw,'status':'loaded'}}
    elif ('"user":true,"authenticated":false')in GO:return {'ok':'true','result':{'data':'Erorr Password','Username':user,'Password':passw,'status':'error'}}			
    elif ('"user":false') in GO:return {'ok':'true','result':{'data':'Username Not Found','Username':user,'Password':passw,'status':'error'}}
    elif '"checkpoint_required"'in GO:
        return {'ok':'true','result':{'data':'Secure Account','Username':user,'Password':passw,'status':'loaded'}}    
@app.route('/Instagram/data/',methods=['GET'])  
def user_insta():
    user = request.args.get('user')
    url = f"https://www.instagram.com/{user}/?__a=1"
    head = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'mid=YbysKAALAAGnsY7iGX9WEyOe8AaT; ig_did=EF4C2AFE-037F-4E1B-A158-C08728818708; ig_nrcb=1; ds_user_id=50787014839; csrftoken=UToGyPsqeTDVOZ7RVJNpWfFjMVUkdHn3; sessionid=50787014839%3Ajhdr3dv7iFRPYb%3A21; rur="RVA\05450787014839\0541672416874:01f7f7d72f9624862a45b7c7ed6092af21b367cd6ec4806e50222845967307214f80dac8"',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
    }
	
    try:
        request1 = requests.get(url,headers=head,data={'__a': '1'}).json()
        id_pro = request1['logging_page_id'].split('_')[1]
        get = request1['graphql']
        iid = get['user']
        idd = iid['edge_follow']
        iid1 = iid['edge_followed_by']
        followed = iid1['count']
        follow = idd['count']
        photo = iid['profile_pic_url']
        data = {'ok':'true','result':{'Followers':followed,'Following':follow,'Id':id_pro,'Photo':photo}}    
        return data
    except:
        data = {'ok':'false','result':{'status':'error'}}    
        return data
@app.route('/Telegram/Check')
def home_page():
    user = str(request.args.get('user'))
    url = requests.get(f'https://t.me/{user}').text
    if 'tgme_username_link' in url:
        data = {'data':'Valid User','result':'true'}
        return data
    else:
        data = {'data':'Taken User','resut':'true'}
        return data

if __name__ == '__main__':             
    app.run(debug=True)        
