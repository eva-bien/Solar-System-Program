class Planet:
    def __init__(self, name, mass, distance_from_the_sun, moons=[]):
        self.name = name
        self.mass = mass
        self.distance_from_the_sun = distance_from_the_sun
        self.moons = moons

class Moon:
    def __init__(self, name):
        self.name = name

class Question:
    def __init__(self, question, planets):
        self.question = question
        self.planets = planets

    def moonAnswer(self, name, moons):
        if len(moons) == 0:
            return f"{name.title()} has no moons." 
        if len(moons) == 1:
            return f"{name.title()} has 1 moon. The moon's name is {moons[0].name}." 
        return f"{name.title()} has {len(moons)} moons: {', '.join([moon.name for moon in moons])}." 
    
    def massAnswer(self, name, mass):
        return f"{name.title()} has a mass of {mass}." 
    
    def isMassQuestion(self, question):
        return "mass" in question.lower() or "big" in question.lower() or "size" in question.lower() or "heavy" in question.lower() or "kg" in question.lower()

    def answer(self):
        for item in self.planets:
            if item.name.lower() in self.question.lower():
                if "moon" in self.question.lower():
                    return self.moonAnswer(item.name, item.moons)
                if self.isMassQuestion(self.question):
                    return self.massAnswer(item.name, item.mass)
                return f"{self.moonAnswer(item.name, item.moons)} \n{self.massAnswer(item.name, item.mass)}"
        return "no match"

def __main__():
    planets = [
        Planet("Earth", 5.97217e24, (0.98, 1.02), [Moon("The Moon")])
        ]
    user_question = Question(input("My name is Cosmos🌝. Ask me about the Solar System. "), planets)
    answer = user_question.answer()
    print(answer)

__main__()

