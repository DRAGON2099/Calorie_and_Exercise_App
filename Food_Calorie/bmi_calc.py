def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) using weight (in kilograms) and height (in meters).
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI value and return a corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_result():
    # Get input from the user
    weight = float(input("Enter your weight in kilograms: "))
    print()
    height = float(input("Enter your height in meters: "))
    print()

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret the BMI value
    category = interpret_bmi(bmi)

    # Print the result
    print(f"Your BMI is: {bmi:.2f}")
    print()
    print(f"You are in the {category} category.")
    print()

