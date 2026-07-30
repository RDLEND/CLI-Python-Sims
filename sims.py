import random
import json
import os

population = random.randint(30, 4000)
day = 2025
age = random.randint(1, 5)
sims = ["Bob", "Hannah"]
married = []
events = [
    "Became a Farmer!", 
    "Became a police guy!", 
    "bought mojang!", 
    "Got a new macbook!", 
    "built a mega potato!", 
    "is in jail!", 
    "committed a horrible crime!", 
    "invented an invention!", 
    "invented a PC Microwave!",
    "started a war!", 
    "started a pandemic!", 
    "became a doctor!", 
    "became a bus driver!", 
    "went to school!", 
    "went to the toilet!", 
    "got a new phone!", 
    "won the lottery!", 
    "is in federal high security prison", 
    "invented Windows Phone 11", 
    "Got Pregnant!", 
    "Was elected president!", 
    "is the owner of IKEA!", 
    "started a company!",
    "said yes!",
    "invented an anti-alien system!"
]

def save_game():
    data = {
        "population": population,
        "sims": sims,
        "age": age,
        "day": day,
        "married": married
    }

    with open("save.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Game saved!")
def load_game():
    global population, sims, age, married, day

    if not os.path.exists("save.json"):
        print("No save file found.")
        return

    with open("save.json", "r") as file:
        data = json.load(file)

    population = data["population"]
    sims = data["sims"]
    age = data["age"]
    married = data["married"]
    day = data["day"]

    print("Game loaded!")

print("Welcome to CLI Sims!")
print("The current population is ", population)
print("type 'population' to view the current population")
print("type 'help' to get instructions")
while True: 
    lifesim = input("> ")

    if len(sims) == 0 or len(sims) <= 1:
        sims = ["Bob", "Hannah"]
        print("You must atleast have 2 sims!")

    elif lifesim == "killsim":
        inp = input("name: ")
        if inp in sims:
            sims.remove(inp)
            print(f"{inp} was deleted from existence!")
            population -= 1
        if len(sims) == 2 or len(sims) < 2:
            print("You must atleast have 2 sims!")

    elif lifesim == "population":
        print("The current population is ", population)

    elif lifesim == "year":
        change = random.randint(-20, 50)
        population += change
        day += 1
        age += 1

        if change >= 0:
            print("Year", day, "passed. Population grew by", change)
            print(random.choice(sims), random.choice(events))
        else:
            print("Year", day, "passed. Population decreased by", abs(change))
            print(random.choice(sims), random.choice(events))

        print("Current population:", population)

    elif lifesim == "createsim":
        print("choose a name")
        name = input("name: ")
        print(f"Sim '{name}' created! population increased by 1.")
        sims.append(name)
        population += 1

    elif lifesim == "listsims":
        for sim in sims:
            print(sim)

    elif lifesim == "help":
        print("Commands: listsims, createsim, year, population, quit, exit, marry, divorce, stats, currentyear, save, load, killsim")
    elif lifesim == "exit" or lifesim == "quit":
        print("save? (y/n)")
        yn = input(">")
        if yn.lower() == "y":
            save_game()
            break
        else:
            break
    elif lifesim == "stats":
        print("avarage age: ", age)
        print("Year: ", day)
        for marry in married:
            print(marry)

    elif lifesim == "marry":
        marrier = input("Person1: ").strip()
        while marrier not in sims:
            print("Please enter a valid sim!")
            marrier = input("Person1: ").strip()

        person2 = input("Person2: ").strip()
        while person2 not in sims:
            print("Please enter a valid sim!")
            person2 = input("Person2: ").strip()
        else:
            print(marrier, "and", person2, "are married! and have kids! population increased by 1")
            print("choose a name")
            name = input("name: ")
            print(f"Sim '{name}' created! population increased by 1.")
            sims.append(name)
            population += 1
            married.append((marrier, person2))

    elif lifesim == "save":
        save_game()

    elif lifesim == "load":
        load_game()

    elif lifesim == "divorce":
        divorcer = input("Person1: ").strip()
        while divorcer not in sims:
            print("Please enter a valid sim!")
            divorcer = input("Person1: ").strip()

        person2divorce = input("Person2: ").strip()
        while person2divorce not in sims:
            print("Please enter a valid sim!")
            person2divorce = input("Person2: ").strip()

        couple = (divorcer, person2divorce)
        reverse = (person2divorce, divorcer)

        if couple in married:
            married.remove(couple)
            print(divorcer, "and", person2divorce, "are divorced!")

        elif reverse in married:
            married.remove(reverse)
            print(divorcer, "and", person2divorce, "are divorced!")

        else:
            print("Those sims are not married.")

    elif lifesim == "currentyear":
        print("The current year is ", day)

    elif lifesim == "clear":
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
    else:
        print("Invalid command, type help")
