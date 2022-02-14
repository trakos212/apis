from flask import Flask,request
import requests
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
if __name__ == '__main__':             
    app.run(debug=True)        
