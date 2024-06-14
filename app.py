from flask import Flask
from dotenv import load_dotenv
import os
from controllers.pvalue_controller import pvalue_bp


load_dotenv()

app = Flask(__name__)
app.register_blueprint(pvalue_bp, url_prefix = '/pvalue')


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)