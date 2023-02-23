import socket
import alphabot
import time
import sqlite3

from flask import Flask, render_template, request

#dichiarazione e inizializzazione del socket TCP che fa da server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#inizializzazione Alphabot
bot = alphabot.AlphaBot()
          
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('avanti') == 'avanti':
            bot.forward()
            time.sleep(1)
            bot.stop()
        elif  request.form.get('sinistra') == 'sinistra':
            bot.left()
            time.sleep(0.15)
            bot.stop()
        elif request.form.get('destra') == 'destra':
            bot.right()
            time.sleep(0.15)
            bot.stop()
        elif request.form.get('indietro') == 'indietro':
            bot.backward()
            time.sleep(1)
            bot.stop()
        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('./index.html')
    
    return render_template("./index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
