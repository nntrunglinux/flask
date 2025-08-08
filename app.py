from flask import Flask, request

app = Flask(__name__)

@app.route('/hanet-webhook', methods=['POST'])
def hanet_webhook():
    data = None
    # Cố gắng lấy JSON
    if request.is_json:
        data = request.get_json()
    else:
        # Nếu không phải JSON, lấy raw data hoặc form
        data = request.data.decode('utf-8') or request.form.to_dict()
    print("Webhook data received:")
    print(data)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run()
