class Country:
    def __init__(self, name: str, population: int) -> None:
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        combined_country = Country(combined_name, combined_population)
        return combined_country


bosnia = Country("Bosnia", 10_000_000)
herzegovina = Country("Herzegovina", 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
