import logging
import os.path
 
from flask import Flask, render_template, request, redirect, flash
 
# [logging config
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
# logging config]
 
 
app = Flask(__name__)
 
 
@app.route('/', methods=['GET'])
def index():
    logging.info('Showing index page')
    return render_template('upload.html')


if __name__ == '__main__':
    # Development only: run "python app.py" and open http://localhost:5000
    server_port = os.environ.get('PORT', '5001')
    app.run(debug=False, port=server_port, host='0.0.0.0')