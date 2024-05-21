import os
import random
from flask import Flask, send_file

app = Flask(__name__)

CONFIG_PATH = "config.txt"

@app.route("/random_image")
def random_image():
    image_director = ""
    try:
        with open(CONFIG_PATH, 'r') as file:
            image_directory = file.read()
            image_directory = image_directory.split("=")[1]
            file.close()
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading or writing the file.")
    # get a list of images in the directory
    images = os.listdir(image_directory)
    # select an image from random
    random_image = random.choice(images)
    # send file
    return send_file(os.path.join(image_directory, random_image))

if __name__ == '__main__':
    app.run(debug=True)