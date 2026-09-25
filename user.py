from egyptain1 import Trip

class User:
    def __init__(self, name, phone, email, gender, is_egyptian, password, age, national_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.is_egyptian = is_egyptian
        self.password = password
        self.age = age
        self.national_id = national_id

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender,
            "is_egyptian": self.is_egyptian,
            "password": self.password,
            "age": self.age,
            "national_id": self.national_id,
            "role": "User"
        }

    def __repr__(self):
        nationality = "Egyptian" if self.is_egyptian else "Foreigner"
        return f"{self.name} ({self.email}) - {nationality}"


class Tourist(User):
    def __init__(self, name, phone, email, gender, is_egyptian, password, age, national_id):
        super().__init__(name, phone, email, gender, is_egyptian, password, age, national_id)
        self.trip = Trip()

    def add_attraction(self, attraction):
        self.trip.add_attraction(attraction)

    def remove_attraction(self, attraction):
        self.trip.remove_attraction(attraction)

    def view_trip(self):
        self.trip.show_attractions()

    def final_summary(self):
        return self.trip.final_summary()

    def to_dict(self):
        d = super().to_dict()
        d["role"] = "Tourist"
        return d


class Admin(User):
    def add_attraction(self, manager, attraction):
        manager.attractions.append(attraction)
        manager.current_attractions.append(attraction)

    def update_attraction(self, manager, name, **changes):
        for attraction in manager.attractions:
            if attraction.name.lower() == name.lower():
                for key, value in changes.items():
                    if hasattr(attraction, key):
                        setattr(attraction, key, value)
                return True
        return False

    def remove_attraction(self, manager, name):
        for attraction in manager.attractions:
            if attraction.name.lower() == name.lower():
                manager.attractions.remove(attraction)
                if attraction in manager.current_attractions:
                    manager.current_attractions.remove(attraction)
                return True
        return False

    def to_dict(self):
        d = super().to_dict()
        d["role"] = "Admin"
        return d