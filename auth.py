from user import Tourist, Admin
from validation import Validation
from json_handler import JSONHandler
from constants import USERS_FILE

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"

def load_users():
    raw_data = JSONHandler.read_json(USERS_FILE)
    users = {}

    # Admin default
    users[ADMIN_EMAIL] = Admin(
        name="System Admin",
        phone="01000000000",
        email=ADMIN_EMAIL,
        gender="N/A",
        is_egyptian=True,
        password=ADMIN_PASSWORD,
        age=30,
        national_id="00000000000000"
    )

    for email, u in raw_data.items():
        if u.get("role") == "Admin":
            users[email] = Admin(u["name"], u["phone"], u["email"], u["gender"], u["is_egyptian"], u["password"], u["age"], u["national_id"])
        else:
            users[email] = Tourist(u["name"], u["phone"], u["email"], u["gender"], u["is_egyptian"], u["password"], u["age"], u["national_id"])

    return users

def save_users(users):
    data = {email: u.to_dict() for email, u in users.items()}
    JSONHandler.write_json(USERS_FILE, data)


class Auth:
    @staticmethod
    def check_password(input_password, stored_password):
        return input_password == stored_password

    @staticmethod
    def register(users):
        print("\n--- Register New Tourist ---")
        email = Validation.get_email()
        if email in users:
            return None, "This email is already registered."

        national_id = Validation.get_national_id()
        for user in users.values():
            if user.national_id == national_id:
                return None, "This National ID is already registered."

        name = input("Name: ").strip()
        phone = Validation.get_phone()
        gender = Validation.get_gender()
        nationality = input("Are you Egyptian? (y/n): ").strip().lower()
        is_egyptian = nationality == "y"
        password = Validation.get_password()
        age = Validation.get_age()

        new_tourist = Tourist(name, phone, email, gender, is_egyptian, password, age, national_id)
        users[email] = new_tourist
        save_users(users)
        return new_tourist, "Registration successful ✅"

    @staticmethod
    def login(users):
        print("\n--- Login ---")
        email = Validation.get_email()
        password = input("Password: ")
        
        user = users.get(email)
        if user is None:
            return None, "No account found with this email."
        if not Auth.check_password(password, user.password):
            return None, "Incorrect password."
        return user, "Login successful ✅"


class ResetPassword:
    @staticmethod
    def reset(users):
        print("\n--- Forgot Password ---")
        email = Validation.get_email()
        national_id = Validation.get_national_id()
        
        user = users.get(email)
        if user is None:
            return False, "No account found with this email."
        if user.national_id != national_id:
            return False, "National ID does not match this account."
        
        new_password = Validation.get_password("Enter New Password: ")
        user.password = new_password
        save_users(users)
        return True, "Password reset successful ✅"