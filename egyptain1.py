transportation_costs = {
    "Cairo": 50,
    "Giza": 60,
    "Alexandria": 100,
    "Luxor": 200,
    "Aswan": 250,
    "Matrouh": 150,
    "South Sinai": 180
}

categories=['Museums','Historical Sites','Cultural Attractions','Nature','Adventure']
class Attraction:
    def __init__(self,name,governorate,ticket_price,rating,visit_time,category):
        self.name = name
        self.governorate = governorate
        self.ticket_price = ticket_price
        self.rating = rating
        self.visit_time = visit_time
        self.category = category

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Governorate: {self.governorate}\n"
            f"Ticket Price: {self.ticket_price}\n"
            f"Rating: {self.rating}\n"
            f"Visit Time: {self.visit_time}\n"
            f"Category: {self.category}"
        )


bibliotheca_alexandrina = Attraction("Bibliotheca Alexandrina",'Alexandria',150,4.7,2,'Cultural Attractions')
egyptian_museum=Attraction("Egyptian Museum", "Cairo", 200,4.7,3,"Museums")
khan_elkhalili=Attraction( "Khan El Khalili","Cairo",0, 4.6,2,"Cultural Attractions")
pyramids=Attraction("Pyramids of Giza","Giza",200, 4.8, 4, "Historical Sites")
valley_of_kings=Attraction( "Valley of the Kings","Luxor", 400, 4.9, 3, "Historical Sites")
siwa_oasis=Attraction( "Siwa Oasis", "Matrouh", 100,4.7,5,"Nature")
Ras_mohammed=Attraction("Ras Mohammed","South Sinai",200, 4.8,5, "Adventure")
philae_temple=Attraction("Philae Temple", "Aswan",300, 4.8,3,"Historical Sites")

citadel_of_qaitbay = Attraction(
    "Citadel of Qaitbay",
    "Alexandria",
    100,
    4.7,
    2,
    "Historical Sites"
)

abu_simbel = Attraction(
    "Abu Simbel Temples",
    "Aswan",
    500,
    4.9,
    3,
    "Historical Sites"
)

karnak_temple = Attraction(
    "Karnak Temple",
    "Luxor",
    300,
    4.8,
    3,
    "Historical Sites"
)

egyptian_museum_cairo = Attraction(
    "National Museum of Egyptian Civilization",
    "Cairo",
    300,
    4.8,
    3,
    "Museums"
)

coptic_museum = Attraction(
    "Coptic Museum",
    "Cairo",
    100,
    4.6,
    2,
    "Museums"
)

felucca_nile = Attraction(
    "Felucca Ride",
    "Aswan",
    200,
    4.7,
    2,
    "Adventure"
)

white_desert = Attraction(
    "White Desert",
    "New Valley",
    150,
    4.8,
    5,
    "Nature"
)

colored_canyon = Attraction(
    "Colored Canyon",
    "South Sinai",
    150,
    4.7,
    4,
    "Nature"
)
Attractions = [
    bibliotheca_alexandrina,
    egyptian_museum,
    khan_elkhalili,
    philae_temple,
    pyramids,
    valley_of_kings,
    siwa_oasis,
    Ras_mohammed,

    citadel_of_qaitbay,
    abu_simbel,
    karnak_temple,
    egyptian_museum_cairo,
    coptic_museum,
    felucca_nile,
    white_desert,
    colored_canyon
]
class Attractionsmanager:
    def __init__(self,attractions):
        self.attractions=attractions
        self.current_attractions = attractions.copy()
    def category_search(self,category):
        category = category.title()
        categories=[]
        for attraction in self.current_attractions:
            if attraction.category == category:
                categories.append(attraction)
        return categories
    def show_attractions(self, categories):
        for category in categories:
            print(category)
            print("------------------------")
    def sort(self, attribute, ascending=True):
        for i in range(len(self.current_attractions) - 1):
            selected = i
            for j in range(i + 1, len(self.current_attractions)):
                if ascending:
                    if getattr(self.current_attractions[j], attribute) < getattr(self.current_attractions[selected], attribute):
                        selected = j
                else:
                    if getattr(self.current_attractions[j], attribute) > getattr(self.current_attractions[selected], attribute):
                        selected = j
            self.current_attractions[i], self.current_attractions[selected] = \
                self.current_attractions[selected], self.current_attractions[i]
        return self.current_attractions
    def binary_search(self,name):
        low = 0
        high = len(self.current_attractions)-1
        result=-1
        while low <= high:
            mid = (low+high)//2
            if self.current_attractions[mid].name.lower() < name.lower():
                low = mid + 1
            elif self.current_attractions[mid].name.lower() > name.lower():
                high = mid - 1
            else:
                result= mid
                high=mid-1
        return result
class Trip:
    def __init__(self):
        self.selected_attractions = []
    def add_attraction(self,attraction):
        self.selected_attractions.append(attraction)
    def remove_attraction(self,attraction):
        self.selected_attractions.remove(attraction)
    def show_attractions(self):
        for attraction in self.selected_attractions:
            print(attraction)
            print("-------------")
    def calculate_ticket_cost(self):
        ticket_cost = 0
        for attraction in self.selected_attractions:
            ticket_cost += attraction.ticket_price
        return ticket_cost
    def calculate_transportation_cost(self):
        transportation_cost = 0
        visited_attractions = []
        for attraction in self.selected_attractions:
            governorate = attraction.governorate
            if governorate not in visited_attractions:
                transportation_cost+=transportation_costs[governorate]
                visited_attractions.append(governorate)
        return transportation_cost
    def final_summary(self):
        ticket_cost = self.calculate_ticket_cost()
        transportation_cost = self.calculate_transportation_cost()
        total_cost = ticket_cost + transportation_cost
        self.show_attractions()
        print(f"ticket cost : {ticket_cost}")
        print(f'transportation cost : {transportation_cost}')
        print(f'total cost : {total_cost}')
manager = Attractionsmanager(Attractions)
trip = Trip()

while True:
    print("\n===== Egypt Explorer =====")
    print("1. Browse Categories")
    print("2. Search Attraction")
    print("3. Sort Attractions by Price")
    print("4. Add Attraction to My Trip")
    print("5. Remove Attraction from My Trip")
    print("6. View My Trip")
    print("7. Final Summary")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nCategories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        category_choice = input("Choose a category: ")

        if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
            selected_category = categories[int(category_choice) - 1]
            result = manager.category_search(selected_category)

            print(f"\n===== {selected_category} =====")
            manager.show_attractions(result)
        else:
            print("Invalid category.")

    elif choice == "2":
        name = input("Enter attraction name: ")

        manager.sort("name")

        index = manager.binary_search(name)

        if index != -1:
            print("\nAttraction Found:")
            print(manager.current_attractions[index])
        else:
            print("Attraction not found.")

    elif choice == "3":
        print("\n===== Sort by Ticket Price =====")
        print("1. Ascending (Low to High)")
        print("2. Descending (High to Low)")

        sort_choice = input("Choose sorting order: ")

        if sort_choice == "1":
            manager.sort("ticket_price", ascending=True)

            print("\n===== Attractions: Low to High =====")
            manager.show_attractions(manager.current_attractions)

        elif sort_choice == "2":
            manager.sort("ticket_price", ascending=False)

            print("\n===== Attractions: High to Low =====")
            manager.show_attractions(manager.current_attractions)

        else:
            print("Invalid sorting choice.")

    elif choice == "4":
        name = input("Enter attraction name to add: ")

        manager.sort("name")
        index = manager.binary_search(name)

        if index != -1:
            attraction = manager.current_attractions[index]
            trip.add_attraction(attraction)
            print(f"{attraction.name} added to My Trip.")
        else:
            print("Attraction not found.")

    elif choice == "5":
        name = input("Enter attraction name to remove: ")

        found = False

        for attraction in trip.selected_attractions:
            if attraction.name.lower() == name.lower():
                trip.remove_attraction(attraction)
                print(f"{attraction.name} removed from My Trip.")
                found = True
                break

        if not found:
            print("Attraction not found in My Trip.")

    elif choice == "6":
        print("\n===== My Trip =====")

        if len(trip.selected_attractions) == 0:
            print("Your trip is empty.")
        else:
            trip.show_attractions()

    elif choice == "7":
        if len(trip.selected_attractions) == 0:
            print("Your trip is empty.")
        else:
            print("\n===== Final Summary =====")
            trip.final_summary()

    elif choice == "8":
        print("Thank you for using Egypt Explorer!")
        break

    else:
        print("Invalid choice.")

