# Blueprint Analyzer with OpenCV

This project introduces architecture students to the basics of OpenCV through a practical exercise in image processing. The program processes blueprint images, highlights walls and room boundaries, and calculates areas of detected rooms. It’s designed for beginners to learn Python and OpenCV while applying programming skills to an architecture-related task.

## Learning Objectives
By completing this exercise, students will:

- Learn the basics of OpenCV for image processing.
- Understand how to load, display, and manipulate images in Python.
- Use edge detection and contour analysis to extract shapes from images.
- Perform calculations like area measurement based on image data.

## Features
1. **Load and Display Blueprint**
   - Load a blueprint image from a file.
   - Display the image in a separate window.

2. **Convert to Grayscale**
   - Convert the image to grayscale to simplify processing.

3. **Edge Detection**
   - Use Canny Edge Detection to highlight walls and boundaries.

4. **Contour Detection**
   - Identify closed areas (like rooms) using contours.
   - Highlight these contours on the original image.

5. **Calculate Room Areas**
   - Approximate and display the area of detected rooms in square pixels.

## Prerequisites
Before starting, ensure you have Python installed on your system and the OpenCV library.

### Installation
Install OpenCV using pip:
```bash
pip install opencv-python-headless
```

## How to Run
1. Clone or download the repository.
2. Save the Python script as `blueprint_analyzer.py`.
3. Run the program from the terminal:

   ```bash
   python blueprint_analyzer.py
   ```

4. Provide the path to a sample blueprint image (e.g., a JPEG or PNG file) when prompted.

## Example Workflow
```plaintext
Enter the path to the blueprint image: blueprint.jpg

-- Displays the following windows --
1. Original Blueprint
2. Edges (processed image)
3. Outlined Blueprint (detected room contours)

-- Console Output --
Contour 0: Area = 1200.50 square pixels
Contour 1: Area = 800.75 square pixels
...
```

## Expansion Ideas
- **Unit Conversion**: Convert pixel-based areas to real-world units (e.g., square feet) by specifying a scale.
- **Interactive Room Selection**: Allow users to click on specific rooms to calculate or highlight areas.
- **Save Processed Image**: Save the image with highlighted contours to a file.
- **Color Segmentation**: Differentiate between walls, doors, and furniture based on color.

## Sample Blueprint Images
You can use any simple blueprint image (JPEG/PNG). For example:
- Images of floor plans with clear walls and rooms.
- Hand-drawn sketches converted to digital formats.
