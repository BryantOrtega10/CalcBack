from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app, resources={r"/*"}, origins="*")

@app.route("/suma/<int:a>/<int:b>")
def getSuma(a,b):
    return jsonify({"success" : True, "resultado" : (a+b)})

@app.route("/resta/<int:a>/<int:b>")
def getResta(a,b):
    return jsonify({"success" : True, "resultado" : (a-b)})

@app.route("/multiplicacion/<int:a>/<int:b>")
def getMultiplicacion(a,b):
    return jsonify({"success" : True, "resultado" : (a*b)})

@app.route("/division/<int:a>/<int:b>")
def getDivision(a,b):
    res = 0
    if(b != 0):
        res = str(a/b)

    return jsonify({"success" : True, "resultado" : res})

@app.route("/modulo/<int:a>/<int:b>")
def getModulo(a,b):
    res = 0
    if(b != 0):
        res = str(a%b)   

    return jsonify({"success" : True, "resultado" : res})


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", debug=True)