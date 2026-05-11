from flask import Flask, jsonify
import requests

app = Flask(__name__)

PRODUCT_SERVICE_URL = "http://product-service:5002/products"

@app.route("/orders", methods=["GET"])
def get_orders():
    products_response = requests.get(PRODUCT_SERVICE_URL, timeout=2)
    products = products_response.json()

    return jsonify({
        "service": "order-service",
        "message": "Orders retrieved successfully",
        "products": products
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)