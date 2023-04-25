from flask import Flask
from api.routes import api

app = Flask(__name__)

# Add all endpoints form the API with a "api" prefix
app.register_blueprint(api, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
