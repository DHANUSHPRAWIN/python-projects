#BMI calculator
def calculate_bmi(weight, height_meters):
    return weight / (height_meters ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_user_data():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kilograms: "))
    height_meters = float(input("Enter your height in meters: "))
    return name, weight, height_meters

def main():
    while True:
        name, weight, height_meters = get_user_data()
        bmi = calculate_bmi(weight, height_meters)
        category = categorize_bmi(bmi)

        print(f"{name}, your BMI is {bmi:.2f}")
        print(f"You are classified as: {category}")

        continue_or_exit = input("Do you want to calculate another BMI? (yes/no): ")
        if continue_or_exit.lower() != "yes":
            break

if __name__ == "__main__":
    main()
