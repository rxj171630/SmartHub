from __future__ import print_function
from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
from flask_cors import CORS, cross_origin
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from datetime import timezone


app = Flask(__name__)
api = Api(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Stocks(Resource):
    def get(self):
        r=requests.get(
            "https://yfapi.net/v6/finance/quote?region=US&lang=en&symbols=AAPL,FB,MSFT,GOOG,AMZN",
            headers={'x-api-key': 'WVRhYOnson33wifwsfdc04eqOwWI5bVm3gWEUzFz'}
        )
        return r.json()

class News(Resource):
    def get(self):
        r=requests.get(
            "https://newsapi.org/v2/top-headlines?country=us&apiKey=5bdffedcfaaf4f749980260dc68dd294",
        )
        return r.json()

class Thermo(Resource):
    def get(self):
        refreshToken = "";
        apiKey = ""

        accessTokenResp = requests.post(f"https://api.ecobee.com/token?grant_type=refresh_token&code={refreshToken}&client_id={apiKey}")
        accessToken = accessTokenResp.json()["access_token"]

        thermoResp = requests.get('https://api.ecobee.com/1/thermostat?json={"selection":{"includeDevice":"false","includeAlerts":"false","selectionType":"registered","selectionMatch":"","includeEvents":"false","includeSettings":"false","includeRuntime":"true"}}',
                                    headers={'Authorization': f'Bearer {accessToken}', 'dataType': 'json'}
        )
        return thermoResp.json()["thermostatList"]
        
class Weather(Resource):
    def get(self):
        refreshToken = "";
        apiKey = ""

        accessTokenResp = requests.post(f"https://api.ecobee.com/token?grant_type=refresh_token&code={refreshToken}&client_id={apiKey}")
        accessToken = accessTokenResp.json()["access_token"]

        weatherResp = requests.get('https://api.ecobee.com/1/thermostat?json={"selection":{"includeWeather":"true","includeDevice":"false","includeAlerts":"false","selectionType":"registered","selectionMatch":"","includeEvents":"false","includeSettings":"false","includeRuntime":"true"}}',
                                    headers={'Authorization': f'Bearer {accessToken}', 'dataType': 'json'}
        )
        return weatherResp.json()["thermostatList"]        

class Calendar(Resource):
    def get(self):
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        #print('Getting the upcoming 10 events')
        startTime=datetime.datetime.utcnow()
        endTime = (startTime + datetime.timedelta(days=7)).isoformat() + 'Z'


        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime', timeMax=endTime,
                                              ).execute()
        events = events_result.get('items', [])
        return events

        # if not events:
        #     print('No upcoming events found.')
        # for event in events:
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(start, event['summary'])



api.add_resource(Stocks, '/stocks')
api.add_resource(News, "/news")
api.add_resource(Thermo, "/thermo")
api.add_resource(Calendar, "/calendar")
api.add_resource(Weather, "/weather")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
