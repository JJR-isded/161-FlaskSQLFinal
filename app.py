from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

todos = [{"todo": "Sample Todo", "done": False}]

import sqlite3


@app.route('/', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        connection = sqlite3.connect('knowledgem_users.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        print(name, password)

        query = "SELECT username,password FROM users where username='"+name+"' and password='"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()
        connection.close()

        if len(results) == 0:
            return render_template("index.html")
            print("Wrong Password or Not Registered user")
        else:
            return render_template("/home.html/")

    return render_template("index.html")


@app.route('/home.html/')
def home():
    return render_template("home.html")  

@app.route('/register.html/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        connection = sqlite3.connect('knowledgem_users.db')
        cursor = connection.cursor()

        newname = request.form.get('Dname')
        newpassword = request.form.get('Dpassword')

        query1 = "INSERT INTO users VALUES('{u}', '{p}')".format(u = newname, p = newpassword)
        cursor.execute(query1)
        connection.commit()
        connection.close()

        return redirect("/")
    return render_template("register.html")


@app.route('/home.html/tickets.html/')
def tickets():
    return render_template('tickets.html')

@app.route('/orders.html/<order_status>')
def ordering(order_status):
    list_of_orders = orderlist(order_status)
    return render_template("orders.html", order_status=order_status, orders=list_of_orders)

@app.route('/orders.html/<int:order_id>')
def order(order_id):
    order = orderiread(order_id)
    return render_template("orderdesc.html",order=order)

@app.route('/home.html/addorders.html/')
def addorder():
    return render_template('addorders.html')

@app.route('/processed', methods=['POST'])
def processing():
    order_data = {
        "order_status": request.form['order_status'],
        "item": request.form['order_item'],
        "name": request.form['order_name'],
        "email": request.form['order_email'],
        "cp_number": request.form['order_cpnumber'],
        "address": request.form['order_address'],

    }
    orderisadded(order_data)
    return redirect(url_for('tickets'))

@app.route('/modifyorder', methods=['POST'])
def modify():
    if request.form["modify"] == "edit":
        order_id = request.form["order_id"] 
        order = orderiread(order_id)
        return render_template('modifyorders.html', order=order)
    elif request.form["modify"] == "delete":
        order_id = request.form["order_id"]
        order = orderiread(order_id)
        deleteo(order_id)
        return redirect(url_for("tickets"))
        pass

@app.route('/update', methods=['POST'])
def modifying():
    order_data = {
        "order_id" : request.form["order_id"],
        "order_status": request.form['order_status'],
        "name": request.form['order_name'],
        "email": request.form['order_email'],
        "cp_number": request.form['order_cpnumber'],
        "item": request.form['order_item'],
        "address": request.form['order_address']
    }
    modifyorders(order_data)
    return redirect(url_for('order',order_id = request.form['order_id']))

@app.route('/home.html/help.html/')
def helpme1():
    return render_template('help.html')

@app.route('/orders.html/help.html/')
def helpme2():
    return render_template('help.html')

@app.route('/tickets.html/help.html/')
def helpme3():
    return render_template('help.html')

@app.route('/register.html/help.html/')
def helpme4():
    return render_template('help.html')

@app.route('/orderdesc.html/help.html/')
def helpme5():
    return render_template('help.html')

@app.route('/modifyorders.html/help.html/')
def helpme6():
    return render_template('help.html')

@app.route('/help.html/')
def helpme7():
    return render_template('help.html')

@app.route('/addorders.html/help.html/')
def helpme8():
    return render_template('help.html')













if __name__ == "__main__":
    app.run(debug=True)
      
