Author: [Marita Georganta](https://github.com/maritaganta)


# Learn Python and OpenCV through Hands-On Projects

This repository serves as a resource for IAAC students and faculty to enhance their skills in **Python** and **OpenCV** through practical projects. The goal is to build real-world applications while reinforcing fundamental concepts of programming and image processing.

## 📂 Projects in the Repository

### 1. 🖼️ Mondrian Analyzer

The **Mondrian Analyzer** is a Python-based tool designed to analyze images inspired by the art of Piet Mondrian. It leverages the power of **OpenCV** to detect and analyze primary colors in an image, calculate pixel coverage, and visualize detected regions.

#### **Key Features:**
- Load images in PNG or JPG format.
- Detect and analyze primary colors: red, blue, yellow, black, and white.
- Calculate pixel count for each detected color.
- Identify contours and visualize detected areas.
- Save results in an Excel file (color_analysis.xlsx).
- Interactive user experience with options to save or restart analysis.

#### **Usage Instructions:**
1. Run the script using:

   ```bash
   python mondrian_analyzer.py
   
2. Enter the path to the Mondrian-style image when prompted:

   ```bash
   Enter the path to the Mondrian image (PNG/JPG): mondrian1.png
   
3. The program will process the image, calculate areas, and show visual output.
4. Example output:

   ```bash
   Yellow: 5230 px, 8 contours
   Blue: 4320 px, 5 contours
   Red: 6700 px, 10 contours
   
5. The processed image will be displayed and saved as processed_mondrian1.png.




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
	
#### **Usage Instructions:**
1. Run the script using:

   ```bash
   python python_building_material_cost_estimator.py

	
2. Enter the required details when prompted:
	```bash
	Enter the length of the room (in feet): 20
	Enter the width of the room (in feet): 15
	hoose a material:
	1. Wood ($8/sq ft)
	2. Concrete ($12/sq ft)
	3. Brick ($10/sq ft)
	4. Tiles ($5/sq ft)

	Enter your choice (1/2/3/4): 2

3.  The tool will calculate and display the total cost:

	```bash
	The total cost for the selected material is: $3600.00

4. Choose whether to save the results:

	```bash
	Do you want to save this estimate to a file? (yes/no): yes
	Project saved successfully!

	
### 📝 Acknowledgment

This repository was originally created by:

Author: [Marita Georganta]
Updated and maintained by: [nachomonereo]

This project is part of the IAAC curriculum to prepare MRAC students for their second term, which focuses on sensing.



### 📚 Additional Resources

- [Python Tutorial] - Learn Python basics and explore hands-on examples.
- [OpenCV Tutorial] - Comprehensive guide to OpenCV, from basics to advanced techniques.

### 🎓 Project Submission Information

This repository has been modified and submitted as part of the Master in Robotics and Advanced Construction (MRAC) program at the Institute for Advanced Architecture of Catalonia (IAAC).

The project aims to demonstrate the application of Python and OpenCV skills acquired during the course, focusing on automation and digital fabrication processes.

Thank you for exploring these projects! 🚀

