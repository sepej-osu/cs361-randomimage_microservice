# Random Image Microservice

This microservice is built with Flask and serves random images from a specified directory.

## Installation

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Edit the `config.txt` file with the directory for your images. The default is set to the `images` folder in this repository.

## Usage

The microservice uses Flask's `send_file` function to serve the file. You can read more about this function [here](https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.send_file).

To get a random image, send a GET request to the following URL:

    http://127.0.0.1:5000/random_image

This will return a random image from the directory specified in your `config.txt` file.

## Example Usage using Javascript

An example using a request to get a random image can be seen [here](https://github.com/sepej-osu/cs361-randomimage_microservice/blob/c961aa02f66effd9262295f6dd43b4a8fb2cfa67/templates/index.html#L20)
```
<script>
    const imageElement = document.getElementById('random-image');

    function getRandomImage() {
      fetch('http://127.0.0.1:5000/random_image')
        .then(response => response.blob())
        .then(blob => {
          const imageUrl = URL.createObjectURL(blob);
          imageElement.src = imageUrl;
        })
        .catch(error => {
          console.error('Error fetching image:', error);
        });
    }

    getRandomImage();
</script>
```

## Running the Microservice

You can run the microservice locally using the following command:

    python random_image_from_directory.py

Replace the image directory in the config file with the path to the directory containing your images before running.

## UML Sequence Diagram
![UML Diagram](https://github.com/sepej-osu/cs361-randomimage_microservice/blob/main/UML%20Sequence%20Diagram.png?raw=true)
