from flask import Flask
from api import api

#app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    app.run(debug=True, host='0.0.0.0')
    return 

# Initialize and run app
#if __name__ == '__main__':
#    api.init_app(app)
#    app.run(debug=True, host='0.0.0.0')