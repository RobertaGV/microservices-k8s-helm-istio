from flask import Flask, jsonify
import requests

app = Flask(__name__)

ORDER_SERVICE_URL = "http://order-service:5001/orders"

@app.route("/", methods=["GET"])
def home():
    try:
        orders_response = requests.get(ORDER_SERVICE_URL, timeout=5)
        orders_response.raise_for_status()
        orders = orders_response.json()

        return jsonify({
            "service": "frontend-service",
            "message": "Microservices platform is running",
            "orders": orders
        })

    except requests.exceptions.RequestException as error:
        return jsonify({
            "service": "frontend-service",
            "message": "Order service temporarily unavailable",
            "error": str(error)
        }), 503

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)