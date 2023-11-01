from flask import Flask, request
from utils import generate_random_values

app = Flask(__name__)


@app.route('/get_values', methods=['GET'])
def get_values():
    try:
        input_string = request.stream.read().decode('utf-8')
        if input_string == '':
            raise ValueError('Invalid string, please send some string')
        return generate_random_values()
    except UnicodeEncodeError:
        return 'Invalid string, please use only utf-8 encoding'


@app.route('/flask-health-check')
def flask_health_check():
	return "success"


if __name__ == '__main__':
    app.run()
