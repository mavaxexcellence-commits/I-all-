from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    if "image" not in request.files:
        return jsonify({"error": "Aucune image reçue"}), 400

    file = request.files["image"]
    img = Image.open(io.BytesIO(file.read()))

    try:
        text = pytesseract.image_to_string(img, lang="fra+eng+spa+por+ara+rus")
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "OCR IA running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
