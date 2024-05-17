def bmi_calculator(height,weight):
    bmi=(weight/height*height)
    return bmi
def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid input! Weight and height must be greater than zero.")
        else:
            bmi = bmi_calculator(weight, height)
            print(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category:Under weight")
        elif bmi < 24.9:
            print("Category:Normal weight")
        elif bmi < 29.9:
            print("Category:Over weight")
        else:
            print("Category:obese")

    except ValueError:
        print("Invalid input! Weight and height must be numeric values.")

if __name__ == "__main__":
    main()

