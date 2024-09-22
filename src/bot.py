from src.read_emails import read_gmails
from helper.twilio_api import send_message

from flask import Flask, request
#from dotenv import load_dotenv
#load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
    return 'All is well...'


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        serviceRequest = request.form['Body']
        sender_id = request.form['From']

        #Código para controlar (con serviceRequest) la acción requerida de la API de gmail (read, etc)

        # Get response from gmailAPI
        result = read_gmails()
        if result['status'] == 1:
            #Eliminar lo del file, solo para testing purposes
            for message in result['response']:
                with open("email_samples.txt", "a") as f:
                    if message.plain:
                        #if len(message.plain) < 1000:
                            f.write(message.plain)
            """for message in result['response']:
                send_message(sender_id, "From: " + message.sender)
                send_message(sender_id, "Subject: " + message.subject)
                send_message(sender_id, "Date: " + message.date)
                send_message(sender_id, "Body: " + message.plain)"""
                
    except:
        pass
    return 'OK', 200
    
"""
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Preview: " + message.snippet)
        print("Message Body: " )
        print(message.plain)  # or message.html
        
        with open("email_samples.txt", "a") as f:
            if message.plain:
                if len(message.plain) < 1000:
                    f.write(message.plain)"""
        # print("Message Body: " + message.plain)  # or message.html