def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def ideal_weight_range(height_m):
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return min_weight, max_weight


def main():
    print("Welcome to Enhanced BMI Calculator")
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters: "))
            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers.Try again.")
                continue
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            print(f"Your BMI is: {bmi:.2f}")
            print(f"Category: {category}")
            lower, upper = ideal_weight_range(height)
            print(f"Ideal weight range for your height: {lower:.2f} kg - {upper:.2f} kg")

            if weight < lower:
                print(f"You should gain at least {lower - weight:.2f} kg to reach a healthy BMI.")
            elif weight > upper:
                print(f"You should lose at least {weight - upper:.2f} kg to reach a healthy BMI.")
            else:
                print("You are within the ideal weight range. Keep it up!")

            again = input("Would you like to calculate again? (yes/no): ").lower()
            if again != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print("Thank you for using the BMI Calculator. Goodbye!")


if __name__ == "__main__":
    main()