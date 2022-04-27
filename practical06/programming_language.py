class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, reflection={self.reflection}, first appeared in {self.year}"

    def isDynamic(self):
        return self.typing == "Dynamic"
