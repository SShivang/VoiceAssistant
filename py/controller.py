from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import mysql.connector
from twilio.rest import Client


app = Flask(__name__)


mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'clock123'
# app.config['MYSQL_DATABASE_DB'] = 'truckdb'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# USER: bb0c0affdfeedb
# PASS: a6d7f403
# Host: us-cdbr-iron-east-02.cleardb.net
# DATABASE: heroku_7debe1263990cca

app.config['MYSQL_DATABASE_USER'] = 'bb0c0affdfeedb'
app.config['MYSQL_DATABASE_PASSWORD'] = 'a6d7f403'
app.config['MYSQL_DATABASE_DB'] = 'heroku_7debe1263990cca'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-02.cleardb.net'


mysql.init_app(app)

con = mysql.connect()




def select(attribute, table, value="",query=""):
    cur = mysql.get_db().cursor()
    if query == "":
        res = cur.execute("SELECT {} FROM truckdb.{}".format(attribute, table))
    else: 
        res = cur.execute("SELECT {} FROM truckdb.{} where {}={}".format(attribute, table, query, value))
    con.commit()
    data = cur.fetchall()
    cur.close
    return data


@app.route('/')
def home():
	return "OK 200"

@app.route('/diagnostic/<int:id>', methods=['GET', 'POST', 'DELETE','PUT'])
def diagnostic(id): 
    if request.method == "GET":
        data = select("*", "diagnostic", "diagnostic_id", 1)
        return jsonify(data)
   
    return "BOOO :("

@app.route('/diagnostic')
def diagnostics():
    data = select("*", "diagnostic")
    #sendText()
    makeCall()
    return jsonify(data)
   
    
    # cur = mysql.connection.cursor()
    # res = cur.execute("SELECT * FROM truckdb.service")
    # mysql.connection.commit()
    # cur.close()
    # print(res)
    # return 'success'


def makeCall(phoneNumber="3057854963"):
    account_sid = 'AC9d73877c3494c64be0e863b8f0c63fef'
    auth_token = 'eac4bd1897c29a0d4e1921fecf8809b1'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=phoneNumber,
        from_='+19545161885'
                    )
    print(call.sid)

def sendText(phoneNumber="3057854963"):
    account_sid = 'AC9d73877c3494c64be0e863b8f0c63fef'
    auth_token = 'eac4bd1897c29a0d4e1921fecf8809b1'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Daimler Truck: Approve Transaction 1249, $1,200.00",
                     from_='+19545161885',
                     to=phoneNumber
                 )

    print(message.sid)



app.run(debug=True, port=8000)
