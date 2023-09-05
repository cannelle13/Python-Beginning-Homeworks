class Country:
    def __init__(self, name: str, population: int) -> None:
        self.name = name
        self.population = population

    def __add__(self, other):
        combined_name = f"{self.name} {other.name}"
        combined_population = self.population + other.population
        combined_country = Country(combined_name, combined_population)
        return combined_country


bosnia = Country("Bosnia", 10_000_000)
herzegovina = Country("Herzegovina", 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
