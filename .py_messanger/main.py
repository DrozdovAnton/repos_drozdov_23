from flask import Flask, render_template, request
import datetime as dt
import json


app = Flask(__name__)

data_file = open('data_file.json') # file with all messages
all_message = [] # list with all messages

def add_message(sender, text):
    new_message = {
        'time' : dt.datetime.now().strftime('%D %H:%M:%S'),
        'sender' : sender,
        'text' : text
    }
    all_message.append(new_message)

    with open('data_file.json', 'w') as write_file:
         json.dump(all_message, write_file) # not correct save data

@app.route('/') # localhost
def start_page():
        return "<title>Start page | Chat</title>" \
               "<p>Hello, user! <a href=chat>Click for open chat</a></p>"

@app.route('/chat', methods =["GET", "POST"]) # localgost/chat
def chat_page():
    if request.method == "POST":
        add_message(request.form.get("name_sender"), request.form.get("message_sender"))
    return render_template('chat_form.html')

app.run(host='0.0.0.0', port=80)