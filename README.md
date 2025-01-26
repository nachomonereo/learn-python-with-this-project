Author: [Marita Georganta](https://github.com/maritaganta)


# Learn Python and OpenCV through Hands-On Projects

This repository serves as a resource for IAAC students and faculty to enhance their skills in **Python** and **OpenCV** through practical projects. The goal is to build real-world applications while reinforcing fundamental concepts of programming and image processing.

## 📂 Projects in the Repository

### 1. 🖼️ Mondrian Analyzer

The **Mondrian Analyzer** is a Python-based tool designed to analyze images inspired by the art of Piet Mondrian. It leverages the power of **OpenCV** to detect and analyze primary colors in an image, calculate pixel coverage, and visualize detected regions.

#### **Key Features:**
- Load images in PNG or JPG format.
- Detect and analyze primary colors: **red, blue, yellow, black, and white**.
- Count the number of pixels occupied by each color.
- Identify contours and visualize the detected shapes.
- Export analysis results to an Excel file (`color_analysis.xlsx`).
- Display processed images using **Matplotlib**.

#### **Usage Instructions:**
1. Run the script using:

   ```bash
   python mondrian_analyzer.py
   
- Provide the path to the Mondrian-style image when prompted.
- Choose to save the results or restart the analysis.
- Processed images will be saved as processed_<original_image>.png.


### 2.Material Cost Estimator

The **Material Cost Estimator** is a simple Python-based tool that helps estimate construction costs by calculating the total cost of materials required for a project.

#### **Key Features:**

- Input room dimensions (length and width).
- Choose from available materials such as wood, concrete, brick, and tiles, with associated costs per square foot.
- Automatic calculation of total material cost.
- Option to save the estimate to an Excel file for future reference.

### ⚙️ Installation Instructions

Ensure you have the necessary dependencies installed before running the scripts:
	pip install opencv-python numpy pandas matplotlib openpyxl
	
### 📝 Acknowledgment

This repository was originally created by:

Author: [Marita Georganta](https://github.com/maritaganta)
Updated and maintained by: [nachomonereo]

This project is part of the IAAC curriculum to prepare MRAC students for their second term, which focuses on sensing.
📚 Additional Resources

    Python Tutorial - Learn Python basics and explore hands-on examples.
    OpenCV Tutorial - Comprehensive guide to OpenCV, from basics to advanced techniques.

Thank you for exploring these projects! 🚀

