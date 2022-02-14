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
@app.route('/Instagran/Date/')
def app2():
    p = request.args.get('user')
    import requests, secrets
    from user_agent import generate_user_agent
    rs = requests.session()
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cookie': f'csrftoken={secrets.token_hex(8)*2}; sessionid={secrets.token_hex(8)*2};',
    'user-agent': generate_user_agent(),
    }
    url = f'https://www.instagram.com/{p}/?__a=1'
    req = rs.get(url,headers=headers).json()
    dady = str(req['logging_page_id']).split('_')[1]

    lord = f'https://o7aa.pythonanywhere.com/?id={dady}'

    dadyx = rs.get(lord)
    dewtools = dadyx.json()
    datee = dewtools['data']
    data  {'date':datee,'status':'loaded'}
    return data
if __name__ == '__main__':             
    app.run(debug=True)        
