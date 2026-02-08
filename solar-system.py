class Planet:
    def __init__(self, name, mass, distance, temperature, moons=[]):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.temperature = temperature
        self.moons = moons

class Question:
    def __init__(self, question, planets):
        self.question = question
        self.planets = planets
    
    def moonAnswer(self, name, moons):
        if len(moons) == 0:
            return f"{name.title()} has no moons." 
        if len(moons) == 1:
            return f"{name.title()} has 1 moon. The moon's name is {moons[0]}." 
        return f"{name.title()} has {len(moons)} moons: {', '.join(moons)}." 

    def answer(self):
        for item in self.planets:
            if item.name.lower() in self.question.lower():
                if "moon" in self.question.lower():
                    return self.moonAnswer(item.name, item.moons)
        return "no match"

def __main__():
    planets = [
        Planet("Mercury", "3.3022×10^23 kg", "46,000,000 km", 427, []), 
        Planet("Venus", "3.3022×10^23 kg", "7 km", 427, ["Bruja", "Moona"]),
        Planet("Earth", "34 kg", "46,000,000 km", 56, ["Luna"])
        ]
    user_question = Question(input("My name is Cosmos. Ask me about the Solar System. "), planets)
    answer = user_question.answer()
    print(answer)

__main__()

