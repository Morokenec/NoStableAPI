from flask import Flask, render_template, request
import time
from services import Settings

app = Flask(__name__)



@app.route('/')
def root():
    settings = Settings(2, 0)
    if  settings.get_error() > 0 and request.remote_addr == "127.0.0.1":
        time.sleep(1)
        settings.edit_error(-1)
        return request.remote_addr, 502

    return { 
        "message" : "Hello",
        "errors" : settings.get_error(),
        "ip" : request.remote_addr
        }

@app.route("/settings", methods=['GET', 'POST'])
def settings():

    if request.method == 'POST':
        print("ОК")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)