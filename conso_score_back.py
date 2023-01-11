#!/bin/env python
import os
from conso_score_back import create_app
from flask_cors import CORS

#load_dotenv('.env')
app = create_app(debug=True)

# global to app
cors = CORS(app, resources={r"/*": {"origins": "localhost:5173"}})    
if __name__ == '__main__':
    app.run()
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=5000)
