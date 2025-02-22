import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_image():
    """
    Ask the user to input the image path and validate it.
    """
    while True:
        image_path = input("Enter the path to the Mondrian image (PNG/JPG): ").strip()

        if not os.path.isfile(image_path):
            print("Error: The file does not exist. Please try again.")
            continue

        if not (image_path.lower().endswith(".png") or image_path.lower().endswith(".jpg")):
            print("Error: The file must be in PNG or JPG format.")
            continue

        try:
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError("Error: Unable to load image. Ensure the file is a valid PNG/JPG.")
            return image, cv2.cvtColor(image, cv2.COLOR_BGR2HSV), image_path
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

def process_color(lower, upper, hsv_image):
    """
    Create a mask for the given color range, apply smoothing and edge detection.
    """
    mask = cv2.inRange(hsv_image, np.array(lower), np.array(upper))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    blurred = cv2.GaussianBlur(mask, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return mask, edges

def show_image(image, title="Image"):
    """ Display image using matplotlib to avoid OpenCV GUI issues """
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def analyze_colors(image, hsv_image):
    """
    Analyze each color in the image, count pixels, detect contours, and visualize.
    """
    color_ranges = {
        'Yellow': ([20, 100, 100], [30, 255, 255]),
        'Blue': ([90, 150, 50], [130, 255, 255]),
        'Red': ([0, 100, 100], [10, 255, 255], [160, 100, 100], [180, 255, 255]),
        'Black': ([0, 0, 0], [180, 255, 30]),
        'White': ([0, 0, 200], [180, 20, 255])
    }

    output_image = image.copy()
    results = []

    for color, value in color_ranges.items():
        if color == 'Red':
            mask1, edges1 = process_color(value[0], value[1], hsv_image)
            mask2, edges2 = process_color(value[2], value[3], hsv_image)
            mask = cv2.bitwise_or(mask1, mask2)
            edges = cv2.bitwise_or(edges1, edges2)
        else:
            mask, edges = process_color(value[0], value[1], hsv_image)

        num_pixels = cv2.countNonZero(mask)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        results.append({
            'Color': color,
            'Pixel Count': num_pixels,
            'Contour Count': len(contours)
        })

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(output_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show the processed image using matplotlib
        show_image(cv2.bitwise_and(image, image, mask=mask), f'{color}: {num_pixels} px, {len(contours)} contours')

    return output_image, results

def save_results_to_excel(results, output_file="color_analysis.xlsx"):
    """
    Save analysis results to an Excel file.
    """
    df = pd.DataFrame(results)
    df.to_excel(output_file, index=False)
    print(f"Results saved to {output_file}")

def main():
    while True:
        print("\nWelcome to the Mondrian Color Analyzer!")

        image, hsv_image, image_path = load_image()
        analyzed_image, results = analyze_colors(image, hsv_image)

        output_path = "processed_" + os.path.basename(image_path)
        cv2.imwrite(output_path, analyzed_image)
        print(f"Processed image saved as '{output_path}'")

        while True:
            choice = input("\nDo you want to (S)ave the results or (R)estart the analysis? (S/R): ").strip().lower()

            if choice == 's':
                save_results_to_excel(results)
                print("Results saved successfully!")
                break
            elif choice == 'r':
                print("Restarting the analysis...")
                break
            else:
                print("Invalid choice. Please enter 'S' to save or 'R' to restart.")

        # Ask if the user wants to run another analysis
        again = input("\nDo you want to analyze another image? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Mondrian Analyzer! Goodbye.")
            break

if __name__ == "__main__":
    main()

