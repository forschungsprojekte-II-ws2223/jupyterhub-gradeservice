import logging
import os.path

SUBMISSION_FOLDER = os.path.join(os.getcwd(), 'submissions')

def check_submission_dir():
    if not os.path.exists(SUBMISSION_FOLDER):
        os.makedirs(SUBMISSION_FOLDER, exist_ok=True)
        logging.info('Created Submission directory')

def submission_dir():
    return SUBMISSION_FOLDER

def check_course_dir(course):
    os.chdir('submissions')
    if not os.path.exists(os.path.join(os.getcwd(), course)):
        os.makedirs(os.path.join(os.getcwd(), course), exist_ok=True)
        logging.info('Created {} directory'.format(course))
        os.chdir('../')
        logging.info("Current working dir : %s" % os.getcwd())
        return
    os.chdir('../')
    logging.info("Current working dir : %s" % os.getcwd())

def check_activity_dir(course, activity):
    os.chdir('submissions/{}'.format(course))
    if not os.path.exists(os.path.join(os.getcwd(), activity)):
        os.makedirs(os.path.join(os.getcwd(), activity), exist_ok=True)
        logging.info('Created {} directory'.format(activity))
        os.chdir('../../')
        logging.info("Current working dir : %s" % os.getcwd())
        return
    os.chdir('../../')
    logging.info("Current working dir : %s" % os.getcwd())

def activity_dir(course, activity):
    os.chdir('submissions/{}/{}'.format(course, activity))
    return os.getcwd()

def defaultDir():
    os.chdir('../../../')
    return os.getcwd()
