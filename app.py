import streamlit as st
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np


class ImageGrayscaleConverter:
    """
    A class for converting images to grayscale and generating histograms.

    Attributes:
        image_file (str): The path to the uploaded image file.
        original_image (PIL.Image): The original image loaded from the file.
        grayscale_image (PIL.Image): The grayscale version of the original image.
    """

    def __init__(self, image_file):
        """
        Initializes an instance of ImageGrayscaleConverter.

        Args:
            image_file: The uploaded image object.
        """
        self.image_file = image_file
        self.original_image = None
        self.grayscale_image = None

    def load_image(self) -> bool:
        """
        Loads the original image from the specified file path.

        Returns:
            bool: True if the image is loaded successfully, False otherwise.
        """
        try:
            self.original_image = Image.open(self.image_file)
            return True
        except Exception as e:
            st.error(f"Error opening image: {e}")
            return False

    def show_original_image(self) -> None:
        """
        Displays the original image in the Streamlit app.
        """
        if self.original_image:
            st.image(self.original_image, caption="Original Image",
                     use_container_width=True)

    def convert_to_grayscale(self) -> None:
        """
        Converts the original image to grayscale using Pillow's ImageOps.grayscale method.
        """
        if self.original_image:
            self.grayscale_image = ImageOps.grayscale(self.original_image)

    def show_grayscale_image(self) -> None:
        """
        Displays the grayscale version of the original image in the Streamlit app.
        """
        if self.grayscale_image:
            st.image(self.grayscale_image, caption="Grayscale Image",
                     use_container_width=True)

    def generate_histogram(self) -> None:
        """
        Generates a histogram for the grayscale image using Matplotlib.
        """
        if self.grayscale_image:
            img_array = np.array(self.grayscale_image)
            hist, bins = np.histogram(img_array.flatten(), 256, range=(0, 256))

            fig, ax = plt.subplots(figsize=(10, 4))
            ax.hist(hist, bins=bins, color="gray")
            ax.set_title("Grayscale Image Histogram")
            ax.set_xlabel("Pixel Intensity")
            ax.set_ylabel("Frequency")

            st.pyplot(fig)


def main():
    """
    The main function of the Streamlit application.
    """
    st.title("Image to Grayscale Histogram Converter")

    st.header("What is this app about?")
    st.write(
        "This app takes an image file as input, converts it to grayscale, and generates a histogram of pixel intensities."
    )

    st.header("How does it work?")
    st.write(
        "Here's what happens when you upload an image: "
        "1. The original image is loaded from the file. "
        "2. The image is converted to grayscale using Pillow's ImageOps.grayscale method. "
        "3. A histogram of pixel intensities is generated using Matplotlib."
    )

    uploaded_file = st.file_uploader(
        label="Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        converter = ImageGrayscaleConverter(uploaded_file)
        if converter.load_image():
            converter.show_original_image()
            converter.convert_to_grayscale()
            converter.show_grayscale_image()
            converter.generate_histogram()


if __name__ == "__main__":
    main()
