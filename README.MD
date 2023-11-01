To start the project:
1. `pip3 install -r requirements.txt`
2. `python3 app.py`

Endpoint for pinging:
`http://127.0.0.1:5000/get_values`


For run tests:
`pytest .`

For run lint:
`flake8`


Run with docker:
1. Install docker and docker-compose on your system
2. `docker compose up -d`


By following the steps above, you will have an NGINX Reverse Proxy and a Flask backend. The general traffic flow will look like the following:

`Client -> NGINX -> WSGI -> Flask`
