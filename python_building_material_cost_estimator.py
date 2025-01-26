import pandas as pd

def get_room_dimensions():
    while True:
        try:
            length = input("Enter the length of the room (in feet): ")
            width = input("Enter the width of the room (in feet): ")
            
            # Validación de entrada para números decimales o enteros
            if not (length.replace('.', '', 1).isdigit() and width.replace('.', '', 1).isdigit()):
                raise ValueError("Invalid input. Please enter a valid number.")

            length = float(length)
            width = float(width)

            if length <= 0 or width <= 0:
                raise ValueError("Dimensions must be greater than zero.")

            area = length * width
            print(f"The total area of the room is {area:.2f} square feet.")
            return area
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

def choose_material():
    materials = {
        1: ("Wood", 8),
        2: ("Concrete", 12),
        3: ("Brick", 10),
        4: ("Tiles", 5),
    }
    
    while True:
        try:
            print("Choose material for the floor:")
            for key, (material, cost) in materials.items():
                print(f"{key}. {material} (${cost}/sq ft)")
            
            choice = input("Enter your choice (1/2/3/4): ")
            if not choice.isdigit() or int(choice) not in materials:
                raise ValueError("Invalid choice. Please enter a valid option (1-4).")
            
            choice = int(choice)
            material, cost_per_sqft = materials[choice]
            print(f"\nYou chose {material} costing ${cost_per_sqft}/sq ft.")
            return material, cost_per_sqft
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

def calculate_cost(area, cost_per_sqft):
    total_cost = area * cost_per_sqft
    print(f"The total cost for the floor is: ${total_cost:.2f}")
    return total_cost

def save_project_to_excel(area, material, cost_per_sqft, total_cost):
    save = input("Do you want to save this project to an Excel file? (yes/no): ").lower()
    if save == 'yes':
        data = {
            "Room Area (sq ft)": [area],
            "Material": [material],
            "Cost per sq ft ($)": [cost_per_sqft],
            "Total Cost ($)": [total_cost]
        }
        df = pd.DataFrame(data)
        df.to_excel("project_estimate.xlsx", index=False)
        print("Project saved successfully to 'project_estimate.xlsx'!")
    else:
        print("Project not saved.")

def main():
    print("Welcome to the Building Material Cost Estimator!\n")
    area = get_room_dimensions()
    material, cost_per_sqft = choose_material()
    total_cost = calculate_cost(area, cost_per_sqft)
    save_project_to_excel(area, material, cost_per_sqft, total_cost)
    print("\nThank you for using the estimator!")

if __name__ == "__main__":
    main()

