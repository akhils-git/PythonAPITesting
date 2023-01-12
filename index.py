from flask import Flask

app = Flask(__name__)

print("Python Api Running...")


@app.route("/")
def hello():
    print('Base called')
    return "Hello, World!"


@app.route("/api/getname/<name>")
def getname(name):
    print('Getname called')
    return "Hi" + name


# app.run(debug=True, port=5000)
app.run(host='0.0.0.0', port=5000)
