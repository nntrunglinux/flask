from flask import Flask, request
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app, template_file='swagger.yml')


@app.route('/hanet-webhook', methods=['POST'])
def hanet_webhook():
    data = None

    if request.is_json:
        data = request.get_json()
    else:
        data = request.data.decode('utf-8') or request.form.to_dict()

    print("Webhook data received:")
    print(data)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run()
