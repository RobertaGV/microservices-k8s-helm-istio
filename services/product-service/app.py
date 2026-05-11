from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({
        "service": "product-service",
        "products": [
            {"id": 1, "name": "Parmigiano Reggiano"},
            {"id": 2, "name": "Aceto Balsamico"},
            {"id": 3, "name": "Prosciutto di Modena"}
        ]
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)