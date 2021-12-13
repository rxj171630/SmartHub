from __future__ import print_function
from flask import Flask, send_from_directory
from flask_restful import Resource, Api, reqparse
import requests
from flask_cors import CORS, cross_origin
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import googlemaps
import json
import pyaudio
import wave
import time
import speech_recognition as sr
from os import path

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("src", type=str)
parser.add_argument("dst", type=str)

cors = CORS(app, resources={r"*": {"origins": "*", "Access-Control-Allow-Origin": "*"}})

#exec(open("../Team-IOT-Smart-Hub-master/img_recog/light_trigger.py").read())


stream = None

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
        refreshToken = "GCkYLfAoZDxl-bomW27fJQQx1F7ImCSTPTlVO_pTGlz8p";
        apiKey = "cqnbQLMy6Zu8CuJnFjC1baKWWcL8Fx0K"

        accessTokenResp = requests.post(f"https://api.ecobee.com/token?grant_type=refresh_token&code={refreshToken}&client_id={apiKey}")
        accessToken = accessTokenResp.json()["access_token"]

        thermoResp = requests.get('https://api.ecobee.com/1/thermostat?json={"selection":{"includeDevice":"false","includeAlerts":"false","selectionType":"registered","selectionMatch":"","includeEvents":"false","includeSettings":"false","includeRuntime":"true"}}',
                                    headers={'Authorization': f'Bearer {accessToken}', 'dataType': 'json'}
        )
        return thermoResp.json()["thermostatList"]

class Calendar(Resource):
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
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
        return json.dumps(events)

        # if not events:
        #     print('No upcoming events found.')
        # for event in events:
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(start, event['summary'])

class Maps(Resource):
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get(self):
        args = parser.parse_args()
        print(args)
        gmaps = googlemaps.Client(key='AIzaSyC2GcW4pAHJuyTJJnsm3fV-krl0nCpOokw')
        now = datetime.datetime.now()

        dist_mat = gmaps.distance_matrix(origins=args.src,destinations=args.dst,mode='driving',departure_time=now)
        return dist_mat

class Alarm(Resource):
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get(self):
        r=requests.get(
            "https://maker.ifttt.com/trigger/trigger_alarm/with/key/dYp8LQdZcmQ_rlSx-Gfhpn",
        )
        return json.dumps({"done": True})

class Notes(Resource):
    def get(self):
        response = send_from_directory(directory='./', filename='notes.txt')
        return response


class Weather(Resource):
    def get(self):
        refreshToken = "GCkYLfAoZDxl-bomW27fJQQx1F7ImCSTPTlVO_pTGlz8p";
        apiKey = "cqnbQLMy6Zu8CuJnFjC1baKWWcL8Fx0K"

        accessTokenResp = requests.post(f"https://api.ecobee.com/token?grant_type=refresh_token&code={refreshToken}&client_id={apiKey}")
        accessToken = accessTokenResp.json()["access_token"]

        weatherResp = requests.get('https://api.ecobee.com/1/thermostat?json={"selection":{"includeWeather":"true","includeDevice":"false","includeAlerts":"false","selectionType":"registered","selectionMatch":"","includeEvents":"false","includeSettings":"false","includeRuntime":"true"}}',
                                    headers={'Authorization': f'Bearer {accessToken}', 'dataType': 'json'}
        )
        return weatherResp.json()["thermostatList"]

recording=False
class RecordStart(Resource):
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get(self):
        global stream, recording
        form_1 = pyaudio.paInt16 # 16-bit resolution
        chans = 1 # 1 channel
        samp_rate = 48000 # 44.1kHz sampling rate
        chunk = 4096 # 2^12 samples for buffer
        record_secs = 5 # seconds to record
        dev_index = 2 # device index found by p.get_device_info_by_index(ii)
        wav_output_filename = 'test1.wav' # name of .wav file

        audio = pyaudio.PyAudio() # create pyaudio instantiation

        # create pyaudio stream
        stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                            input_device_index = dev_index,input = True, \
                            frames_per_buffer=chunk)
        print("recording")
        frames = []

        # loop through stream and append audio chunks to frame array
        #for ii in range(0,int((samp_rate/chunk)*record_secs)):
        start = time.time()
        while(time.time()-start < 5):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        audio.terminate()

        # save the audio frames as .wav file
        wavefile = wave.open(wav_output_filename,'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()

        # obtain path to "english.wav" in the same folder as this script
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test1.wav")
        # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
        # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)

        with open("notes.txt", "a") as f:
            f.write(r.recognize_google(audio) + "\n")
        
        return json.dumps({"done": True}) 

api.add_resource(Stocks, '/stocks')
api.add_resource(News, "/news")
api.add_resource(Thermo, "/thermo")
api.add_resource(Calendar, "/calendar")
api.add_resource(Maps, "/maps")
api.add_resource(Alarm, "/alarm")
api.add_resource(Notes, "/notes")
api.add_resource(Weather, "/weather")
api.add_resource(RecordStart, "/recordStart")
#api.add_resource(RecordEnd, "/recordEnd")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=8000)
