from flask import Flask, render_template, request

app = Flask(__name__)

MODEL_PATH = '/models/model.h5'

@app.route('/',methods=["GET"])

def main():
    return render_template('index.html')

@app.route('/',methods=["POST"])

def upload():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)

