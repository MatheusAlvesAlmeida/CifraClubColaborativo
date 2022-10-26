from flask import Flask, request
from flask_restful import Resource, Api
from formatter import cipher_formatter

app = Flask(__name__)
api = Api(app)


class CipherFormatter(Resource):
    def get(self):
        cipher = request.get_data().decode('utf-8')
        formatted_cipher = cyphet_formatter(cipher)
        print(formatted_cipher)
        return formatted_cipher


api.add_resource(CipherFormatter, '/cipher')


if __name__ == "__main__":
    app.run(debug=True)
