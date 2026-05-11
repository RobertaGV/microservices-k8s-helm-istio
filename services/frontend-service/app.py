from flask import Flask, jsonify
import requests

app = Flask(__name__)

ORDER_SERVICE_URL = "http://order-service:5001/orders"

@app.route("/", methods=["GET"])
def home():
    orders_response = requests.get(ORDER_SERVICE_URL, timeout=2)
    orders = orders_response.json()

    return jsonify({
        "service": "frontend-service",
        "message": "Microservices platform is running",
        "orders": orders
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)