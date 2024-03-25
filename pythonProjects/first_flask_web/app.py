from flask import Flask, request
from flask import render_template
import mysql.connector
import json

app = Flask(__name__)


# Connect to MySQL
#connection = mysql.connector.connect(
   # host="@localhost",
#    user="",
#    password="",
#    port = 0,
#    database = ""
#)
#cursor = connection.cursor(dictionary=True)

@app.route('/')
def home():  
    #connection.reconnect()
    #cursor.execute("select value,date from db order by date asc")
    #data = cursor.fetchall()
    data = []
    data.append((1685557800000,0.5116))
    data.append((1685557920000,0.5117))
    data.append((1685569260000,0.5153))
    data.append((1685576760000,0.5189))
    data.append((1685588160000,0.5047))
    data.append((1685588460000,0.5055))
    data.append((1685595180000,0.5066))
    data.append((1685602860000,0.5038))
    data.append((1685606700000,0.504))
    data.append((1685613540000,0.5065))
    return render_template('home.html', data=data)

# Route to process the form data
@app.route('/process_data', methods=['POST'])
def process_data():
    #data_input = request.form['data_input']
   # cursor.execute("select value,date from db order by date asc ")  
    # Do something with the input data
    #data = cursor.fetchall()
    #data.append(data_input)
    #print("Input data:", data_input)
    
    data = []
    data.append((1685557800000,0.5116))
    data.append((1685557920000,0.5117))
    data.append((1685569260000,0.5153))
    data.append((1685576760000,0.5189))
    data.append((1685588160000,0.5047))
    data.append((1685588460000,0.5055))
    data.append((1685595180000,0.5066))
    data.append((1685602860000,0.5038))
    data.append((1685606700000,0.504))
    data.append((1685613540000,0.5065))
    return data

if __name__ =="__main__":
    app.run(debug=True)