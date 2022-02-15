from flask import Flask,request
import requests
from user_agent import generate_user_agent
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route('/Telegram/Check/')
def home_page():
    user = str(request.args.get('user'))
    url = requests.get(f'https://t.me/{user}').text
    if 'tgme_username_link' in url:
        data = {'data':'Valid User','result':'true'}
        return data
    else:
        data = {'data':'Taken User','resut':'true'}
        return data
@app.route('/tele-check/',methods=['GET'])
def app3():
    user = str(request.args.get('user'))
    isChannel = requests.get(f'https://t.me/s/{user}/1', allow_redirects=False).status_code
    if isChannel == 200:
        data_set = {'type': 'Channel', 'stats': 'loaded'}
        return data_set
    elif isChannel == 302:
        isUser = requests.get(f'https://t.me/{user}').text
        if not 'members' in isUser:
            data_set = {'type': 'Pierson', 'stats': 'loaded'}
            return data_set
        elif 'members' in isUser:
            data_set = {'type': 'Group', 'stats': 'loaded'}
            return data_set


@app.route('/user-agent')
def arabicge():
    r = str(''.join((generate_user_agent() for i in range(1))))
    data_set = {'data':f'{r}','status':'loaded'}
    return data_set
@app.route('/instagram/info/',methods=['GET'])
def app4():
	user =	str(request.args.get('user'))
	url = 'https://www.instagram.com/'+str(user)+'/?__a=1'
	headers =	{
'Host': 'www.instagram.com',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
'cookie': 'mid=YZkPjQABAAER3b51Z8ah-YVxu-xm',
'cookie': 'ig_did=BEB7DE0C-FD7B-4ABB-A6C1-8A522CEA34DC',
'cookie': 'ig_nrcb=1',
'cookie': 'csrftoken=wM6BVNacm7VTF40daho2bwgYqInjifuo',
'cookie': 'ds_user_id=51709139961',
'cookie': 'sessionid=51709139961%3AMbTXsYBElAevDn%3A11'
	}
	
	response =	requests.get(url,headers=headers).json()
	id_pro = response['logging_page_id'].split('_')[1]
	get = response['graphql']
	iid = get['user']
	name = iid['full_name']
	idd = iid['edge_follow']
	iid1 = iid['edge_followed_by']
	followed = iid1['count']
	follow = idd['count']
	photo = iid['profile_pic_url']
	return {'User':user,'Full-Name':name,'Followers':followed,'Following':follow,'Pic':photo}
if __name__ == '__main__':             
    app.run(debug=True)        
