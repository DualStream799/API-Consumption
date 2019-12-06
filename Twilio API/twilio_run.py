# -*- coding: utf-8 -*-

# Importing libraries:
import twilio_integration as twi

filename = "client_database"
message = input("Type your message: ")

# Loads Twilio Client with the credentials in the .json file:
client, to_number, from_number = twi.check_twilio_credentials(filename)
# Send message via SMS:
twi.send_message(message, to_number, from_number, client)
# Send message via WhatsApp:
#twi.send_message(message, to_number, from_number, client, whatsapp=True)