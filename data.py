import sqlite3

db_path = "knowledgem.db"

def conne2db(path):
    conne = sqlite3.connect(path)
    conne.row_factory = sqlite3.Row
    return (conne, conne.cursor())

def orderlist(order_status):
    conne, curs = conne2db(db_path)
    query = "SELECT * FROM orders WHERE status = ?"
    value = order_status
    results = curs.execute(query,(value,)).fetchall()
    conne.close()
    return results

def orderiread(order_id):
    conne, curs = conne2db(db_path)
    query = 'SELECT * FROM orders WHERE orderid = ?'
    value = order_id
    result = curs.execute(query,(value,)).fetchone()
    conne.close()
    return result

def orderisadded(order_data):
    conne, curs = conne2db(db_path)
    query = 'INSERT INTO orders (item, name, email, cp_number, address, status) VALUES (?,?,?,?,?,?)'
    values = (order_data['item'], order_data['name'],
              order_data['email'], order_data['cp_number'],
              order_data['address'], order_data['order_status'])
    curs.execute(query,values)
    conne.commit()
    conne.close()

def modifyorders(order_data):
    conne, curs = conne2db(db_path)
    query = "UPDATE orders SET status=?, name=?, cp_number=?, item=?, address=?, email=? WHERE orderid=?"
    values = (order_data['order_status'], order_data['name'],
              order_data['cp_number'], order_data['item'],
              order_data['address'], order_data['email'],
              order_data['order_id'])
    curs.execute(query, values)
    conne.commit()
    conne.close()

def deleteo(order_id):
    conne, curs = conne2db(db_path)
    query = "DELETE FROM orders WHERE orderid = ?"
    values = (order_id,)
    curs.execute(query, values)
    conne.commit()
    conne.close()

#def registerpg():
 #   if request.method == 'POST':
  #      connection = sqlite3.connect('knowledgem.db')
   #     cursor = connection.cursor()
    #    query1 = "INSERT INTO users VALUES('{u}', '{p}')".format(u = newname, p = newpassword)
     #   cursor.execute(query1)
      #  connection.commit()
       # connection.close()
    

    
