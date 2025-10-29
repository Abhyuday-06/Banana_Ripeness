# Banana Ripeness Detector

This project uses a simple machine learning approach to determine the ripeness of a banana based on its color. It can analyze images from a webcam in real-time or predict the ripeness of bananas from a folder of images.

## How it works

The scripts work by calculating the average color of an image and comparing it to the average colors of a set of training images. The training images are located in the `Data` directory, which is divided into three subdirectories:

- `Riped`: Contains images of ripe bananas.
- `Unriped`: Contains images of unripe bananas.
- `No Banana Found`: Contains images without bananas.

The prediction is made by finding the training image with the closest average color to the input image.

## File Structure

- `Banana_Ripeness(webcam).py`: A Python script that uses a webcam to capture real-time video and predict the ripeness of a banana in each frame.
- `Banana_predict.py`: A Python script that predicts the ripeness of bananas from images in a `Test` directory.
- `Data/`: A directory containing the training images.
  - `Riped/`: Contains images of ripe bananas.
  - `Unriped/`: Contains images of unripe bananas.
  - `No Banana Found/`: Contains images without bananas.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/banana-ripeness-detector.git
   ```
2. **Install the dependencies:**
   ```bash
   pip install opencv-python numpy
   ```
3. **Organize the `Data` directory:**
   - Make sure the `Data` directory is in the same directory as the Python scripts.
   - The `Data` directory should contain the `Riped`, `Unriped`, and `No Banana Found` subdirectories with the corresponding images.

## Usage

### Real-time detection with a webcam

To use the real-time banana ripeness detector, run the following command:

```bash
python Banana_Ripeness(webcam).py
```

This will open a window with the webcam feed, and the predicted ripeness will be displayed on the screen. Press `q` to quit.

### Predict from a folder of images

To predict the ripeness of bananas from a folder of images, you first need to create a `Test` directory inside the `Data` directory and place the images you want to test in it. Then, run the following command:

```bash
python Banana_predict.py
```

The script will print the predicted ripeness for each image in the `Test` directory.

## Limitations

This project is a simple implementation and has some limitations:

- **Accuracy:** The accuracy of the prediction is highly dependent on the quality and variety of the training images.
- **Hardcoded paths:** The paths to the `Data` and `Test` directories are hardcoded in the scripts. You will need to modify the scripts if you want to use a different directory structure.
- **Basic features:** The prediction is based solely on the average color of the image, which may not be a reliable indicator of ripeness in all cases.
