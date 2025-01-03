def get_room_dimensions():
    length = float(input("Enter the length of the room (in feet): "))
    width = float(input("Enter the width of the room (in feet): "))
    area = length * width
    print(f"The total area of the room is {area:.2f} square feet.")
    return area

def choose_material():
    materials = {
        1: ("Wood", 8),
        2: ("Concrete", 12),
        3: ("Brick", 10),
        4: ("Tiles", 5),
    }
    
    print("Choose material for the floor:")
    for key, (material, cost) in materials.items():
        print(f"{key}. {material} (${cost}/sq ft)")
    
    choice = int(input("Enter your choice (1/2/3/4): "))
    
    if choice in materials:
        material, cost_per_sqft = materials[choice]
        print(f"\nYou chose {material} costing ${cost_per_sqft}/sq ft.")
        return material, cost_per_sqft
    else:
        print("Invalid choice. Please try again.")
        return choose_material()

def calculate_cost(area, cost_per_sqft):
    total_cost = area * cost_per_sqft
    print(f"The total cost for the floor is: ${total_cost:.2f}")
    return total_cost

def save_project(area, material, cost_per_sqft, total_cost):
    save = input("Do you want to save this project? (yes/no): ").lower()
    if save == 'yes':
        with open("project_estimate.txt", "w") as file:
            file.write("Building Material Cost Estimator Project\n")
            file.write(f"Room Area: {area:.2f} square feet\n")
            file.write(f"Material: {material}\n")
            file.write(f"Cost per square foot: ${cost_per_sqft}\n")
            file.write(f"Total Cost: ${total_cost:.2f}\n")
        print("Project saved successfully!")
    else:
        print("Project not saved.")

def main():
    print("Welcome to the Building Material Cost Estimator!\n")
    area = get_room_dimensions()
    material, cost_per_sqft = choose_material()
    total_cost = calculate_cost(area, cost_per_sqft)
    save_project(area, material, cost_per_sqft, total_cost)
    print("\nThank you for using the estimator!")

if __name__ == "__main__":
    main()