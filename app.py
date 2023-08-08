

from api import app
from api.config.db import db
from flask_sqlalchemy import SQLAlchemy
from api import app
db = db 
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)