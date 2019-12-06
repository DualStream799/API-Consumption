# -*- coding: utf-8 -*-

# Importing libraries:
from twilio.rest import Client
import json
import os

def load_database(filename):
    """Reads the database and returns it as a dictionary"""
    with open("../{}.json".format(filename), 'r+') as main_file:
        return json.loads(main_file.read())

def check_twilio_credentials(credentials_filename, path=os.getcwd()):
    """Checks if there's a file with twillio API's developer credentials"""
    if credentials_filename+".json" in os.listdir(path+'/..'):
        client_database = load_database(credentials_filename)
        to_number = client_database['to_number']
        from_number = client_database['from_number']
        client = Client(client_database['twilio_account_sid'], client_database['twilio_auth_token'])
        return client, to_number, from_number
    else:
    	print('File not found')

def send_message(message, to_number, from_number, client, whatsapp=False):
    """Sends a message to a number from Twilio standart number via SMS(or via WhatsApp if "whatsapp" is True)"""
    to_number, from_number = ['+'+number for number in [to_number, from_number]]
    if whatsapp == True:
        to_number, from_number = ['whatsapp:'+number for number in [to_number, from_number]]
        #to_number = 'whatsapp:' + to_number
        #from_number = 'whatsapp:' + from_number
    send_message = client.messages.create(
        to=to_number,
        from_=from_number, 
        body=message)