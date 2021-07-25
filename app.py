from flask import Flask, jsonify
import os
# init app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
  return jsonify({"msg": "hello world"})

# Run server
if __name__ == '__main__':
  print("running the flask application")
  app.run(host="0.0.0.0", debug=True)