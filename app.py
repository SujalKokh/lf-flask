from flask import Flask, jsonify
from flask_mysqldb import MySQL
import os

# init app
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'database'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'lf-iac'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def get():
  cur = mysql.connection.cursor()
  cur.execute('''SELECT * FROM books''')
  rv = cur.fetchall()
  return jsonify({"msg": rv})

# Run server
if __name__ == '__main__':
  print("running the flask application")
  app.run(host="0.0.0.0", debug=True)