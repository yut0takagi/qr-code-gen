from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        img_io = generate_qr_image(text)
        return send_file(img_io, mimetype='image/png')
    return render_template("index.html")

def generate_qr_image(data):
    qr = qrcode.QRCode(
        version=1, box_size=10, border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

if __name__ == "__main__":
    app.run(debug=True)