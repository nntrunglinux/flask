from flask import Flask, request

app = Flask(__name__)

@app.route('/hanet-webhook', methods=['POST'])
def hanet_webhook():
    data = request.json
    print("Webhook data received:", data)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run()
