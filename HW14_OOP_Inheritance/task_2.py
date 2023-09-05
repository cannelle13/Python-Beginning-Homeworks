class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict[str, dict]) -> None:
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(
        self, name: str, cuisine: str, menu: dict[str, dict], drive_thru: bool
    ) -> None:
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name not in self.menu:
            return "Dish not available"

        if self.menu[dish_name]["quantity"] < quantity:
            return "Requested quantity not available"

        total_cost = self.menu[dish_name]["price"] * quantity
        self.menu[dish_name]["quantity"] -= quantity
        return total_cost


menu = {
    "burger": {"price": 5, "quantity": 10},
    "pizza": {"price": 10, "quantity": 20},
    "drink": {"price": 1, "quantity": 15},
}

mc = FastFood("McDonalds", "Fast Food", menu, True)


print(mc.order("burger", 5))  # 25
print(mc.order("burger", 15))  # Requested quantity not available
print(mc.order("soup", 5))  # Dish not available
