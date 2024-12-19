Author: [Marita Georganta](https://github.com/maritaganta)

# Building Material Cost Estimator

This project serves as an opportunity for students with architectural background to learn Python. It assumes that the student is an absolute beginner and is used to teach the fundamental conecpts of Python through a hands on approach.

The project will be written as one script. The script calculates the cost of flooring for a room based on user input for dimensions and material choices. The program also allows users to save project details to a file.

The project consists of two parts, the basic and the custom version. Students are asked to complete the basic version, and then create a new script where they would implement the basic version integrating one of the expansion ideas listed below.

## Learning Objectives
By completing this exercise, students will:

- Learn basic Python syntax.
- Understand variables and data types.
- Work with conditional statements.
- Use loops for repetitive tasks (if expanded).
- Create and use functions.
- Work with lists, tuples, and dictionaries.
- Learn basic file handling operations.

## Features
1. **Calculate Room Area**
   - Users input the length and width of the room.
   - The program calculates the total area in square feet.

2. **Choose Flooring Material**
   - Users choose a material for the flooring from predefined options.
   - Each material has a cost per square foot.

3. **Calculate Total Cost**
   - The program calculates the total cost based on the chosen material and room area.

4. **Save Project Details**
   - Users can save the project details (dimensions, material, cost) to a file.

## How to Run
1. After forking, clone the repository `building_material_cost_estimator.py` file.
2. Open a terminal or command prompt.
3. Run the program using Python:

   ```bash
   python building_material_cost_estimator.py
   ```

4. Follow the prompts to:
   - Enter room dimensions.
   - Choose a flooring material.
   - View the total cost.
   - Save the project details if desired.

## Example Workflow
```plaintext
Welcome to the Building Material Cost Estimator!

Enter the length of the room (in feet): 10
Enter the width of the room (in feet): 12
The total area of the room is 120.00 square feet.

Choose material for the floor:
1. Wood ($8/sq ft)
2. Concrete ($12/sq ft)
3. Brick ($10/sq ft)
4. Tiles ($5/sq ft)
Enter your choice (1/2/3/4): 2

You chose Concrete costing $12/sq ft.
The total cost for the floor is: $1440.00

Do you want to save this project? (yes/no): yes
Project saved successfully!

Thank you for using the estimator!
```

## File Details
- `building_material_cost_estimator.py`: The main Python script for the project.

## Expansion Ideas
Add an additional feature to your script, either from the list below or propose your own.
- Support for multiple rooms.
- A budget management feature.
- Advanced file handling for saving/loading multiple projects.
- Material waste calculation.
- Visualization of cost breakdowns using charts.

## Documentation
Ensure that the custom version is well documented, including usage instructions and demo.
