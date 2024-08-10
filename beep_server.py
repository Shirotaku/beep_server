from flask import Flask
import os

app = Flask(__name__)

@app.route('/beep', methods=['GET'])
def beep():
    os.system('beep')
    return "Beep triggered!", 200

@app.route('/beep_ok', methods=['GET'])
def beep_ok():
    # Zwei kurze Beep-Signale für "OK"
    os.system('beep -f 1000 -l 100 && sleep 0.1 && beep -f 1000 -l 100')
    return "OK beep triggered!", 200

@app.route('/beep_ok_2', methods=['GET'])
def beep_ok_2():
    # Zwei kurze Beep-Signale für "OK"
    os.system('beep -f 1000 -l 100 && sleep 0.1 && beep -f 1000 -l 100 && beep -f 1000 -l 100 && sleep 0.1 && beep -f 1000 -l 100')
    return "OK beep 2x triggered!", 200

@app.route('/beep_error', methods=['GET'])
def beep_error():
    # Ein längeres, tieferes Beep-Signal für Fehler
    os.system('beep -f 500 -l 500')
    return "Error beep triggered!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
