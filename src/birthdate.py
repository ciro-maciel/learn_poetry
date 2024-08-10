import datetime

def calculate_age(birthdate):
    """
    Calculates a person's age based on their birthdate.

    Args:
        birthdate (str): Birthdate in the format 'dd/mm/yyyy'.

    Returns:
        int: Calculated age.
    """
    day, month, year = map(int, birthdate.split('/'))
    birthdate = datetime.date(year, month, day)
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return age

def main():
    birthdate = input("Enter your birthdate (dd/mm/yyyy): ")
    age = calculate_age(birthdate)
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
