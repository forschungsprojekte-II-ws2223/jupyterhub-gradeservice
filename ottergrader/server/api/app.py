import requests
import base64
import logging
import os.path

import directory

from directory import check_submission_dir
from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, flash
from werkzeug.utils import secure_filename
from datetime import date

# [logging config
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
# logging config]

app = Flask(__name__)
app.secret_key = "somesecretkey"
 
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.png']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

@app.route('/upload_b64', methods=['POST'])
def getting_file():
    # getting base64 string over https request
    base64_string = request.json['base64String']

    # remove URI prefix to get base64 data
    base64_data = base64_string.split(',')
    ipynb_data = base64.b64decode(base64_data[1])

    # getting system time
    today = date.today
    d4 = today.strftime("%b-%d-%Y")

    # save file in container
    with open(d4 + '.ipynb', 'wb') as f:
        f.write(ipynb_data)

    return Flask.jsonify({'response': ipynb_data})
 

@app.route('/upload', methods=['POST'])
def upload_files():
    logging.info('Starting file upload')
 
    if 'file' not in request.files:
        flash('No file part')
        return {"Error": "File not found"}, 404 #redirect(redirectURL)
 
    file = request.files['file']
    # obtaining the name of the destination file
    filename = file.filename
    if filename == '':
        logging.info('Invalid file')
        flash('No file selected for uploading')
        return {"Error": "File not uploaded"}, 404
    else:
        logging.info('Selected file is= [%s]', filename)
        file_ext = os.path.splitext(filename)[1]
        if file_ext in app.config['ALLOWED_EXTENSIONS']:
            secure_fname = secure_filename(filename)

            logging.info('Secure filename is= [%s]', secure_fname)

            file.save(os.path.join(directory.submission_dir(), secure_fname))

            logging.info('Upload is successful')

            flash('File uploaded successfully')
            return {"file": "File uploaded successfully"}, 201
        else:
            logging.info('Invalid file extension')
            flash('Not allowed file type')
            return {"Error": "File type not allowed"}, 404

if __name__ == '__main__':
    check_submission_dir()

    server_port = os.environ.get('PORT', '5000')
    app.run(debug=False, port=server_port, host="0.0.0.0")
