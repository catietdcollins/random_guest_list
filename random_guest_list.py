import random

class ThanksgivingGuestList:
    def __init__(self, menu):
        self.guests = []
        self.menu = menu

    def randomize_guest_list(self):
        random.shuffle(self.menu)
        self.guests = [f"Guest {i+1}: {dish}" for i, dish in enumerate(self.menu)]

    def print_guest_list(self):
        print("Thanksgiving Guest List:")
        for guest in self.guests:
            print(guest)

    def print_individual_dish(self, guest_number):
        if guest_number < 1 or guest_number > len(self.guests):
            print("Invalid guest number.")
        else:
            print(self.guests[guest_number - 1])

# Thanksgiving Menu
menu = [
    "turkey", "stuffing", "cranberry sauce", "mashed potatoes", "green bean casserole",
    "sweet potatoes", "rolls", "gravy", "pumpkin pie", "apple pie", "pecan pie", "cornbread",
    "salad", "corn", "macaroni and cheese", "dressing", "green beans", "biscuits", "winter squash",
    "fresh fruit plate", "apple cider", "coffee", "tea", "butter", "cru de te", "sweet potato pie", "quiche",
]

# Create an instance of the ThanksgivingGuestList class
guest_list = ThanksgivingGuestList(menu)

# Randomize the guest list
guest_list.randomize_guest_list()

# Print the randomized guest list
guest_list.print_guest_list()

# Print individual guest-dish assignments
guest_list.print_individual_dish(3)