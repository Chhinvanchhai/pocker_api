
# from dotenv import load_dotenv
# load_dotenv() 
from api import app
from api.config.db import db
from api import app
db = db 

# if __name__ == '__main__':
#     app.run(host="localhost", port=8000, debug=True)
# from logging.config import dictConfig


if __name__ == '__main__':
    app.run(debug=True)