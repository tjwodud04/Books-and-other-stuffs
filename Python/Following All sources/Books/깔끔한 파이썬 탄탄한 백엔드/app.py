app = flask(__name__)

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"
