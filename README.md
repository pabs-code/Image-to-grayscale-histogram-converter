# Image to Grayscale Histogram Converter 🖼️

A Streamlit application that converts uploaded images to grayscale and generates pixel intensity histograms. Perfect for quick image processing tasks!

## 📚 Table of Contents

- [Image to Grayscale Converter 🖼️](#image-to-grayscale-converter-️)
  - [📚 Table of Contents](#-table-of-contents)
  - [🧠 About This Project](#-about-this-project)
  - [🛠️ Installation](#️-installation)
  - [🚀 Usage Instructions](#-usage-instructions)
  - [✅ Features](#-features)
  - [📸 🎉 Animated GIF Demo](#--animated-gif-demo)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [📌 Notes](#-notes)

---

## 🧠 About This Project

This project provides a simple yet powerful tool for converting RGB images to grayscale and visualizing their pixel intensity distributions. Built using **Streamlit**, **Pillow**, and **Matplotlib**, it's ideal for developers looking to quickly add image processing capabilities to their workflows.

---

## 🛠️ Installation

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

## 🚀 Usage Instructions

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

## ✅ Features

| Feature                | Description                                                                  |
| ---------------------- | ---------------------------------------------------------------------------- |
| **Image Conversion**   | Converts RGB images to grayscale using Pillow's `ImageOps.grayscale` method. |
| **Histogram Analysis** | Visualizes pixel intensity distribution using Matplotlib histograms.         |
| **Interactive UI**     | Streamlit-based interface for easy upload and visualization.                 |

---

## 📸 🎉 Animated GIF Demo

![Animated GIF](assets/video-sample.gif)


*Example output: Original image (top), grayscale version (middle), and histogram (bottom).*

---

## 🤝 Contributing

Contributions are welcome! To submit a pull request:

1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Test your changes locally.
4. Push your changes and create a pull request.

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.


---

## 📌 Notes

- **Supported Formats**: JPG, JPEG, PNG (as per the code's file type filter).
- **Requirements**: Python 3.8+ with `streamlit`, `Pillow`, `matplotlib`, and `numpy` installed.
- **Example Use Case**: Quick analysis of image brightness or contrast for preprocessing in machine learning pipelines.
