set FLASK_APP=conso_score_back
set FLASK_ENV=development
set FLASK_DEBUG=on
set CORS_URL=http://127.0.0.1:5173
start .\env\Scripts\activate.bat
pip install -r requirements.txt
python -m flask run