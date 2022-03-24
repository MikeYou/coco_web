#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response, redirect, url_for
import cv2
import os
import time
import datetime
import signal
import subprocess

app = Flask(__name__)

def get_detect_pid():
    return int(subprocess.check_output(['pgrep','-F', "python3", "[location of detect.py]", "--weights", "[weights]", "--img", "640", "640" ,"--conf", "0.8", "--source", "0", "--data", "[cocoadata.yaml]"]).strip())



def new_report(test_report):
    lists=os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report+"//"+fn))
    return lists[-1]



def gen_frames():
    while True:
        a = new_report("[location of detected image]")
        
        if a == None:
            pass
        else:
            frame = cv2.imread("location of detected image"+ str(a))

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            #time.sleep(0.1)



@app.route('/pic', methods=['POST', 'GET'])
def pic():
    
    p=subprocess.run(["python3", "location of detect.py", "--weights", "[weights]", "--img", "640", "640" ,"--conf", "0.8", "--source", "0", "--data", "[location of cocoadata.yaml]"])
    
    return redirect(url_for('index'))

@app.route('/exit', methods=['POST', 'GET'])
def kill_detect():

    os.system("pkill -f [location of detect.py]")
    return redirect(url_for('index'))




@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')







if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, threaded=True)
