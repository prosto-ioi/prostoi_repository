import math

def degree_to_radian():
    degree = float(input("Input degree: "))
    radian = degree * (math.pi / 180)
    print(f"Output radian: {round(radian, 6)}")

def trapezoid_area():
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    area = ((base1 + base2) / 2) * height
    print(f"Expected Output: {area}")

def polygon_area():
    n = int(input("Input number of sides: "))
    s = float(input("Input the length of a side: "))
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    print(f"The area of the polygon is: {round(area, 2)}")

def parallelogram_area():
    base = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    area = base * height
    print(f"Expected Output: {area}")

def main():
    while True:
        print("\n CALCULATOR")
        print("1 — Convert degree to radian")
        print("2 — Area of a trapezoid")
        print("3 — Area of a regular polygon")
        print("4 — Area of a parallelogram")
        print("0 — Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            degree_to_radian()
        elif choice == "2":
            trapezoid_area()
        elif choice == "3":
            polygon_area()
        elif choice == "4":
            parallelogram_area()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
