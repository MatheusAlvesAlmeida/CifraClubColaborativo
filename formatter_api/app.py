from flask import Flask, request
from flask_restful import Resource, Api
from formatter import cipher_formatter

app = Flask(__name__)
api = Api(app)


class CipherFormatter(Resource):
    def get(self):
        cipher_in = request.get_data().decode('utf-8')
        cipher_formatted = cipher_formatter(cipher_in)
        print(cipher_formatted)
        return cipher_formatted


api.add_resource(CipherFormatter, '/cipher')


if __name__ == "__main__":
    app.run(debug=True)
