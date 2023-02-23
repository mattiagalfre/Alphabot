import socket
import alphabot
import time
import sqlite3
import hashlib
import secrets

from flask import Flask, render_template, redirect, url_for, request

#dichiarazione e inizializzazione del socket TCP che fa da server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#inizializzazione Alphabot
bot = alphabot.AlphaBot()
comandi = {"w":bot.forward, "a":bot.left, "d":bot.right, "s":bot.backward, "q":bot.stop}

index = secrets.token_urlsafe()
indexUrl = "/" + index
          
app = Flask(__name__)

def validate(username, password):
    completion = False
    con = sqlite3.connect('./Alphabot.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS")
    rows = cur.fetchall()
    for row in rows:
        dbUser = row[1]
        dbPass = row[2]
        if dbUser==username:
            completion=check_password(dbPass, password)
    return completion

def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = hashlib.md5(password.encode())
        hashed_password = result.hexdigest()
        completion = validate(username, hashed_password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('./login.html', error=error)

@app.route(indexUrl, methods=['GET', 'POST'])
def secret():
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
        elif request.form.get('stop') == 'stop':
            bot.stop()
        elif request.form.get('curvaDx') == 'curvaDx':
            con = sqlite3.connect("./Alphabot.db")
            cur = con.cursor()        
            res = cur.execute(f"SELECT Movimento FROM ALPHABOT WHERE ID = 1" )

            move = res.fetchall()
            move = move[0][0]

            lista = move.split(";")
            for comando in lista:
                msg = comando.split("|")
                comandi[msg[0]]()
                time.sleep(float(msg[1]))
                bot.stop()

            con.close()

        elif request.form.get('curvaSx') == 'curvaSx':
            con = sqlite3.connect("./Alphabot.db")
            cur = con.cursor()        
            res = cur.execute(f"SELECT Movimento FROM ALPHABOT WHERE ID = 2" )

            move = res.fetchall()
            move = move[0][0]

            lista = move.split(";")
            for comando in lista:
                msg = comando.split("|")
                comandi[msg[0]]()
                time.sleep(float(msg[1]))
                bot.stop()

            con.close()
        elif request.form.get('rotondaDx') == 'rotondaDx':
            con = sqlite3.connect("./Alphabot.db")
            cur = con.cursor()        
            res = cur.execute(f"SELECT Movimento FROM ALPHABOT WHERE ID = 3" )

            move = res.fetchall()
            move = move[0][0]

            lista = move.split(";")
            for comando in lista:
                msg = comando.split("|")
                comandi[msg[0]]()
                time.sleep(float(msg[1]))
                bot.stop()

            con.close()
        elif request.form.get('rotondaSx') == 'rotondaSx':
            con = sqlite3.connect("./Alphabot.db")
            cur = con.cursor()        
            res = cur.execute(f"SELECT Movimento FROM ALPHABOT WHERE ID = 4" )

            move = res.fetchall()
            move = move[0][0]

            lista = move.split(";")
            for comando in lista:
                msg = comando.split("|")
                comandi[msg[0]]()
                time.sleep(float(msg[1]))
                bot.stop()

            con.close()
        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('./index.html')
    
    return render_template("./index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

