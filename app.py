from bs4 import BeautifulSoup
import lxml,json,requests
from flask import *

app = Flask(__name__)
@app.route("/data/)
def info():
    userid = request.args.get("id")
    try:
        URL = f"https://i.instagram.com/api/v1/users/{userid}/info/"
        headers = {'User-Agent':'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)'} 
        response = requests.get(URL, headers=headers)
        return (response.json()["user"])
    except:
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
    
if __name__ == "__main__":
    app.run()
