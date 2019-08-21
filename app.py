import argparse
from flask import Flask
from flask import request
from flask import render_template
from views import products_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix='/products')


@app.route('/')
def index():
    return render_template('index.html')


def get_parsed_arguments():
    """ get and parse parameters from CLI """
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='debug mode')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_parsed_arguments()
    debug = args.debug
    app.run('localhost', 8080, debug=debug)
