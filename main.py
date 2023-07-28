from flask import Flask, request, jsonify
import qrcode_generation

# Create a Simple Flask Application
app= Flask(__name__)

#QR Code API
@app.route("/generate_qr_code", methods=["POST"])
def generate_qr_code():
    try:
        data = dict(request.get_json())
        if data["link"] != '':
            qr = qrcode_generation.QRCodeClass(data["link"])
            code = qr.create_qr_code()
            return jsonify({
                "response": code
            })
    except Exception as e:
        print(f'Error Generating QR Code - {e}')
        return jsonify({
            "response":"Some Error Occured. Please Try again Later."
        })



if __name__ == "__main__":
    app.run(debug=True)
    