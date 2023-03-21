import logging
import os.path

SUBMISSION_FOLDER = os.path.join(os.getcwd(), 'submissions')

def check_submission_dir():
    if not os.path.exists(SUBMISSION_FOLDER):
        os.makedirs(SUBMISSION_FOLDER, exist_ok=True)
        logging.info('Created Submission directory')

def submission_dir():
    return SUBMISSION_FOLDER