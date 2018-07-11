from flask import Flask, request, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getInfo', methods=['GET'])
def get_info():
    query = request.args.get('query')

    responseText = {}
    responseText["status"] = 200
    responseText["query"] = query

    responseTextJson = json.dumps(responseText, ensure_ascii=False).encode('utf8')

    responseJson = app.response_class(
        response=responseTextJson,
        status=200,
        mimetype='application/json'
    )
    return responseJson


@app.route('/postInfo', methods=['POST'])
def post_info():
    query = request.get_json()
    queryJson = json.dumps(query, ensure_ascii=False).encode('utf8')

    responseJson = app.response_class(
        response=queryJson,
        status=200,
        mimetype='application/json'
    )

    return responseJson


if __name__ == '__main__':
    app.run()
