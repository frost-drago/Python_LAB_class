status_modifiers = {
    "Depressed" : ["del self",
                   {"Happiness":-1, "Confusion":1, "Stress":1, "Denial of reality":1}],
    "Panicked"  : ["AAAAAAAAAAAAAAAAAAAA!",
                   {"Stress":1, "Productivity":1, "Confusion":1}],
    "Happy"     : ["If I could keep this streak on.",
                   {"Stress":-2, "Happiness":1}],
    "Grieving"  : ["It all begins with denial.",
                   {"Confusion":1, "Stress":1}],
    "Jaded"     : ["In the end, nothing matters, not even me. That's why I need to put in effort, "
                   "not for superficial grades but for the life I want.",
                   {"Productivity":1, "Time_management":1, "Determination":1}],
    "Tired"     : ["I feel lightheaded. I feel like fainting.",
                   {"Productivity":-1}],
    "Curious"   : ["Curiosity will lead me places... and lots of time wasted.", 
                   {"Discovery":2, "Audacity":1, "Time_management":-1}],
    "Frustrated": ["Fuuuuuuuuuuuuuuuuuuuuu-",
                   {"Stress":2}],
    "Mischievous":["When is April Fools? Who cares, let's just do this when no one is looking.",
                   {"Audacity":1, "Discovery":1, "Time_management":-1}],
    "Serious"   : ["Beyond this point, no more bullshit.",
                   {"Time_management":1, "Productivity":1, "Stress":1}],
    "Saw something silly" : ["I saw something and now I can't get it off my mind. Oh no. Oh no, no no... lol. Hehehe.",
                             {"Stress":-1, "Happiness":1}],
    "Existential crisis"  : ["Am I doing the right thing? What if it's all... pointless?",
                             {"Confusion":1}],
    "Persevere" :["Even if my body breaks apart, I won't back down. Heck, I should've been dead."
                  "So what if I die once more? This is nothing compared to that.",
                    {"Determination":1, "Relentlessness":1}],
    "Relieved"  :["Ah, I did it.",
                  {"Stress":-2}]
}

class this_particular_homo_sapiens:
    def __init__(self):
        self.status = {}
        self.modifiers = {}
        self.action = ""

    def check_condition(self):
        print(f"Action: {self.action}")
        print(f"Status:")
        for an_emotion, a_description in self.status.items():
            print(f" @ {an_emotion:14} - {a_description}")
        print(f"Modifiers:")
        for a_modifier, a_degree in self.modifiers.items():
            print(f" @ {a_modifier:14} [{a_degree}]")
        print()

    def add_emotion(self, emotion):
        self.status[emotion] = status_modifiers[emotion][0]
        modifiers_dictionary = status_modifiers[emotion][1]
        for a_modifier in modifiers_dictionary:
            if a_modifier in self.modifiers:
                self.modifiers[a_modifier] += modifiers_dictionary[a_modifier]
            else:
                self.modifiers[a_modifier] = 0
                self.modifiers[a_modifier] += modifiers_dictionary[a_modifier]
        
        to_delete = []
        for a_modifier in self.modifiers:
            if self.modifiers[a_modifier] == 0:
                to_delete += [a_modifier]

        for a_modifier in to_delete:
            del self.modifiers[a_modifier]

            
# MAIN

me = this_particular_homo_sapiens()

me.action = "Doing HW"
me.add_emotion("Tired")
me.check_condition()

me.action = "Submitting HW"
me.add_emotion("Relieved")
me.check_condition()

me.action = "Thinking about family"
del me.status["Relieved"]
me.add_emotion("Grieving")
me.add_emotion("Depressed")
me.check_condition()