from flask import Flask,request
import requests,os
app = Flask(__name__)
@app.route('/Telegram')
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
    app.run()        
