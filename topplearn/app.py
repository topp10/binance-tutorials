from flask import Flask, render_template, request, flash, redirect, jsonify
import config1, config2, csv
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = b'gsdfgsdfgdsgfdfgsdfgdf'
client = Client(config2.API_KEY, config2.API_SECRET)

@app.route('/')
def index():
    title = "CoinView"

    account = client.get_account()
    # print(account)
    
    balances = account['balances']
    # print(balances)

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)
    try:
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity']
            )
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')



@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'