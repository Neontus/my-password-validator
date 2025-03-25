import flask


# TODO: change this to your academic email
AUTHOR = "junokim@seas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Password < 8 characters"}), 400
    
    carr = [c for c in pw]
    seenUpper = False
    seenSpecial = False

    for char in carr:
        if char.isalpha() and not char.islower():
            seenUpper = True
        if char in '!@#$%^&*':
            seenSpecial = True
    
    if not seenUpper:
        return flask.jsonify({"valid": False, "reason": "No uppercase letter"}), 400

    if not seenSpecial:
        return flask.jsonify({"valid": False, "reason": "No special character"}), 400
    
    return flask.jsonify({"valid": True, "reason":""}), 200