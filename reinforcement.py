emotions = {
    "Not great..": 1,
    "Okay": 2,
    "Fantastic!": 3
}

class Person:
    """ A class representing a person """
    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def mood(self):
        for emotion, rate in self.emotions.items():
            if rate == 1:
                print(f"I am feeling a low amount of {emotion}.")
            elif rate == 2:
                print(f"I am feeling a medium amount of {emotion}.")
            elif rate == 3:
                print(f"I am feeling a high amount of {emotion}.")



person = Person("Jasmin", emotions)
print(person)
person.mood()