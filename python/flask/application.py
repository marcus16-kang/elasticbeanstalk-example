import boto3
from flask import Flask

application = Flask(__name__)

@application.get('/health')
def get_health():
    return {'status': 'OK'}

@application.get('/version')
def get_version():
    return {'version': 'v1.0'}

@application.get('/aws')
def get_aws():
    return boto3.client('sts').get_caller_identity()

if __name__ == '__main__':
    application.debug = True
    application.run()