from flask import Flask
import os

app = Flask(__name__)

@app.route('/beep', methods=['GET'])
def beep():
    os.system('beep')
    return "Beep triggered!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
