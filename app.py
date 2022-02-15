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
@app.route('/user-agent')
def arabicge():
    r = str(''.join((generate_user_agent() for i in range(1))))
    data_set = {'data':f'{r}','status':'loaded'}
    return data_set
if __name__ == '__main__':             
    app.run(debug=True)        
