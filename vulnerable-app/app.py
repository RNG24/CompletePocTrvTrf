from flask import Flask
import requests
app = Flask(__name__)

# Intentional RCE/unsafe eval (vuln)
@app.route("/run/<code>")
def run_code(code):
    return str(eval(code))

@app.route("/get")
def fetch():
    return requests.get("http://example.com").text

# intentionally add an in-source secret as example
SECRET_KEY="supersecretkey123456"
if __name__ == "__main__":
    app.run(debug=True)
