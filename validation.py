import re
from constants import (
    EMAIL_REGEX,
    PHONE_REGEX,
    NATIONAL_ID_REGEX,
    URL_REGEX,
    ALLOWED_FILE_FORMAT
)

class Validation:
    @staticmethod
    def get_email(prompt="Enter Email: "):
        while True:
            email = input(prompt).strip()
            if re.match(EMAIL_REGEX, email):
                return email
            print("❌ Invalid email address format.")

    @staticmethod
    def get_phone(prompt="Enter Phone: "):
        while True:
            phone = input(prompt).strip()
            if re.match(PHONE_REGEX, phone):
                return phone
            print("❌ Invalid mobile phone number (Must be 11 digits starting with 010, 011, 012, or 015).")

    @staticmethod
    def get_national_id(prompt="Enter 14-digit National ID: "):
        while True:
            national_id = input(prompt).strip()
            if re.match(NATIONAL_ID_REGEX, national_id):
                return national_id
            print("❌ Invalid National ID. Must consist of exactly 14 digits.")

    @staticmethod
    def get_age(prompt="Enter Age: "):
        while True:
            age_input = input(prompt).strip()
            if age_input.isdigit() and int(age_input) > 0:
                return int(age_input)
            print("❌ Invalid age. Numbers only.")

    @staticmethod
    def get_password(prompt="Enter Password (min 6 characters): "):
        while True:
            password = input(prompt)
            if len(password) >= 6:
                return password
            print("❌ Password too short (minimum 6 characters).")

    @staticmethod
    def get_gender():
        print("\nSelect Gender:")
        print("1) Male")
        print("2) Female")
        print("3) Other")
        gender_map = {"1": "Male", "2": "Female", "3": "Other"}
        while True:
            choice = input("Choice (1-3): ").strip()
            if choice in gender_map:
                return gender_map[choice]
            print("❌ Invalid option. Choose 1, 2, or 3.")