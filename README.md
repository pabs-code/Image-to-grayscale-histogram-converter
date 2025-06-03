# Image Grayscale Converter and Histogram Generator

A Streamlit application that converts uploaded images to grayscale and generates pixel intensity histograms. Perfect for quick image processing tasks!

## 📚 Table of Contents
- [About This Project](#about-this-project)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)
- [Features](#features)
- [Demo](#video-demo)
- [License](#license)
- [Notes](#notes)

---

## About This Project

This is a simple yet powerful **Streamlit application** that allows users to upload an image and:

- Convert it into grayscale.
- Display the grayscale version of the image.
- Generate a histogram showing pixel intensity distribution.

The app is built using **Python**, with dependencies on **Streamlit**, **Pillow (PIL)**, and **Matplotlib**.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/image-to-grayscale-converter.git
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit pillow matplotlib numpy
   ```

3. **Navigate to the project directory:**
   ```bash
   cd image-to-grayscale-converter
   ```

---

## Usage Instructions

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Upload an image file (`.jpg`, `.jpeg`, or `.png`) through the interface.

3. The app will:
   - Display the original image.
   - Convert it to grayscale.
   - Generate and show a histogram of pixel intensities.

---

## Features

| Feature | Description |
|--------|-------------|
| 📎 Image Upload | Supports `.jpg`, `.jpeg`, and `.png` formats |
| 🧠 Grayscale Conversion | Uses Pillow's `ImageOps.grayscale()` for fast conversion |
| 📊 Histogram Visualization | Displays a histogram of pixel intensities (0–255) |
| 🖼️ Interactive UI | Simple, user-friendly interface with Streamlit |

---

## Demo

[main-app-video-sample.webm](https://github.com/user-attachments/assets/797bbb7c-7e2b-4954-82fc-1f564114c354)

*Example output: Original image (top), grayscale version (middle), and histogram (bottom).*

---

## License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

---

## Notes

- **Supported Formats**: JPG, JPEG, PNG (as per the code's file type filter).
- **Requirements**: Python 3.8+ with `streamlit`, `Pillow`, `matplotlib`, and `numpy` installed.
- **Example Use Case**: Quick analysis of image brightness or contrast for preprocessing in machine learning pipelines.
  
