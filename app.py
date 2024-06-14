from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)