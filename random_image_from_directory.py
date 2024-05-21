import os
import random
from flask import Flask, send_file

app = Flask(__name__)

image_directory = "images"

@app.route("/random_image")
def random_image():
    # get a list of images in the directory
    images = os.listdir(image_directory)
    # select an image from random
    random_image = random.choice(images)
    # send file
    return send_file(os.path.join(image_directory, random_image))

if __name__ == '__main__':
    app.run(debug=True)