"""
PYTHON 3 PRACTICE — ALL-IN-ONE (MENU DRIVEN)
Author: Haris Khan

Run this file and choose a topic:
1) Strings
2) Menu formatting
3) Data types
4) User input
5) Rock Paper Scissors
6) Lists
7) Tuples
0) Run ALL
q) Quit
"""

import random
from enum import Enum
from pprint import pprint


# ============================================================
# Helpers
# ============================================================
def show(label, value):
    """Pretty-print helper for demo output."""
    print(f"\n--- {label} ---")
    pprint(value)


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# TOPIC 1: Strings + Types
# ============================================================
def topic_strings():
    print("\n=== TOPIC: Strings + Types ===")
    line1 = "Vecna"
    line2 = "Stranger Things!!!"

    print(type(line1))
    print(type(line2))
    print(type(line2) == str)
    print(isinstance(line2, str))

    print(f"{line2} of {line1}")

    decade = str(1980)
    print(decade)
    print(type(decade))

    multilines = """
Hey, how are you!?

I was just checking in.

Hope all is well!
"""
    print(multilines)

    print(line1.lower())
    print(line2.upper())

    print(multilines.title())
    print(multilines.replace("well", "GREAT"))


# ============================================================
# TOPIC 2: String formatting mini-project (Menu)
# ============================================================
def topic_menu_formatting():
    print("\n=== TOPIC: String Formatting (Menu) ===")
    title = "menu".upper()
    print(title.center(24, "="))
    print("Black Coffee".ljust(20, ".") + "$1".rjust(4))
    print("Cappuccino".ljust(20, ".") + "$3".rjust(4))
    print("Latte".ljust(20, ".") + "$5".rjust(4))
    print("Cheesesteak Panini".ljust(20, ".") + "$8".rjust(4))


# ============================================================
# TOPIC 3: Core data types (bool / int / float / complex)
# ============================================================
def topic_data_types():
    print("\n=== TOPIC: Core Data Types ===")
    val = True
    x = bool(False)
    print(type(x))
    print(isinstance(val, bool))

    price = 100
    best_price = int(100)
    print(type(price))
    print(isinstance(best_price, int))

    price = 9.55
    gpa = 3.55
    print(type(price))
    print(type(gpa))
    print(type(price) == type(gpa))
    print(isinstance(price, float))

    comp_value = 5 + 45j
    print(type(comp_value))


# ============================================================
# TOPIC 4: User input (simple)
# ============================================================
def topic_user_input():
    print("\n=== TOPIC: User Input ===")
    value = input("Please enter a value: ").strip()
    print(f"You entered: {value!r}")


# ============================================================
# TOPIC 5: Mini-project — Rock / Paper / Scissors (1 player vs CPU)
# ============================================================
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def topic_rps():
    print("\n=== TOPIC: Rock Paper Scissors ===")
    print("Rock Paper Scissors!")

    raw = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n> ").strip()

    # Validate input safely
    if not raw.isdigit():
        print("Invalid input. Please enter 1, 2, or 3.")
        return

    player1 = int(raw)
    if player1 < 1 or player1 > 3:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    player2 = random.randint(1, 3)

    print("\nPlayer1 chose " + RPS(player1).name + ".")
    print("Player2 chose " + RPS(player2).name + ".\n")

    if player1 == player2:
        print("IT'S A TIE GAME!")
    elif (
            (player1 == RPS.ROCK.value and player2 == RPS.SCISSORS.value)
            or (player1 == RPS.PAPER.value and player2 == RPS.ROCK.value)
            or (player1 == RPS.SCISSORS.value and player2 == RPS.PAPER.value)
    ):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


# ============================================================
# TOPIC 6: Lists
# ============================================================
def topic_lists():
    print("\n=== TOPIC: Lists ===")
    users = ["Alice", "Brian", "Clara"]
    data = ["Alice", 30, False]
    empty_list = []

    show("Is 'Alice' in empty_list?", "Alice" in empty_list)

    show("users[0]", users[0])
    show("users[-2]", users[-2])
    show("Index of 'Clara'", users.index("Clara"))

    show("users[0:2]", users[0:2])
    show("users[1:]", users[1:])
    show("users[-3:-1]", users[-3:-1])

    show("len(data)", len(data))

    # Mutations
    users.append("Diana")
    show("After append('Diana')", users)

    users += ["Ethan"]
    show("After += ['Ethan']", users)

    users.extend(["Frank", "Grace"])
    show("After extend(['Frank','Grace'])", users)

    users.insert(0, "Zoe")
    show("After insert(0,'Zoe')", users)

    users[2:2] = ["Henry", "Ivy"]
    show("After insert via slice users[2:2] = ...", users)

    users[1:3] = ["Jack", "Kara"]
    show("After replace via slice users[1:3] = ...", users)

    users.remove("Zoe")
    show("After remove('Zoe')", users)

    last = users.pop()
    show("Popped last", last)
    show("After pop()", users)

    del users[0]
    show("After del users[0]", users)

    data.clear()
    show("After data.clear()", data)

    # Sorting
    users[1:2] = ["alice"]
    users.sort()
    show("After users.sort()", users)

    users.sort(key=str.lower)
    show("After users.sort(key=str.lower)", users)

    # Numbers ops + sorted vs sort
    nums = [9, 3, 71, 14, 6]
    nums.reverse()
    show("After nums.reverse()", nums)

    show("sorted(nums, reverse=True)", sorted(nums, reverse=True))
    show("nums (unchanged by sorted)", nums)

    # Copies
    nums_copy = nums.copy()
    nums_list = list(nums)
    nums_slice = nums[:]

    show("nums_copy", nums_copy)
    show("nums_list", nums_list)

    nums_slice.sort()
    show("nums_slice (sorted copy)", nums_slice)
    show("nums (still)", nums)

    show("type(nums)", type(nums))

    mylist = [7, "Olivia", False]
    show("mylist", mylist)


# ============================================================
# TOPIC 7: Tuples
# ============================================================
def topic_tuples():
    print("\n=== TOPIC: Tuples ===")
    mytuple = ("Mark", 55, False)
    another_tuple = (10, 5, 10, 20, 10, 5)

    show("mytuple", mytuple)
    show("type(mytuple)", type(mytuple))
    show("type(another_tuple)", type(another_tuple))

    # Convert tuple -> list -> modify -> tuple
    new_list = list(mytuple)
    new_list.append("Noah")
    new_tuple = tuple(new_list)
    show("new_tuple (after converting + append)", new_tuple)

    first, *middle, last = another_tuple
    show("first", first)
    show("middle", middle)
    show("last", last)

    show("another_tuple.count(10)", another_tuple.count(10))

def topic_dict_sets():
    """
    TOPIC: Dictionaries and Sets (Simple Practice)
    """

    # ============================================================
    # DICTIONARIES: Create and Inspect
    # ============================================================
    team = {
        "lead": "Maya",
        "developer": "Ethan"
    }

    team2 = dict(lead="Maya", developer="Ethan")

    print(team)
    print(team2)
    print(type(team))
    print(len(team))

    # ============================================================
    # DICTIONARIES: Access Items
    # ============================================================
    print(team["lead"])
    print(team.get("developer"))

    print(team.keys())
    print(team.values())
    print(team.items())

    print("developer" in team)
    print("tester" in team)

    # ============================================================
    # DICTIONARIES: Update and Add
    # ============================================================
    team["lead"] = "Nora"
    team.update({"tester": "Liam"})
    print(team)

    # ============================================================
    # DICTIONARIES: Remove Items
    # ============================================================
    print(team.pop("tester"))
    print(team)

    team["designer"] = "Olivia"
    print(team)

    print(team.popitem())
    print(team)

    # ============================================================
    # DICTIONARIES: Delete and Clear
    # ============================================================
    team["manager"] = "Sophia"
    del team["manager"]
    print(team)

    team2.clear()
    print(team2)

    # ============================================================
    # DICTIONARIES: Copying
    # ============================================================
    # GOOD copy
    team_copy = team.copy()
    team_copy["intern"] = "Alex"

    print("Original team:", team)
    print("Copied team:", team_copy)

    team_copy2 = dict(team)
    print("Copied via dict():", team_copy2)

    # ============================================================
    # DICTIONARIES: Nested Dictionaries
    # ============================================================
    member1 = {
        "name": "Ryan",
        "role": "backend"
    }

    member2 = {
        "name": "Zoe",
        "role": "frontend"
    }

    project_team = {
        "member1": member1,
        "member2": member2
    }

    print(project_team)
    print(project_team["member1"]["name"])

    # ============================================================
    # SETS: Create and Basics
    # ============================================================
    scores = {10, 20, 30, 40}
    scores2 = set((10, 20, 30, 40))

    print(scores)
    print(scores2)
    print(type(scores))
    print(len(scores))

    # ============================================================
    # SETS: No Duplicates
    # ============================================================
    scores = {10, 20, 20, 30}
    print(scores)

    # True == 1, False == 0
    scores = {0, 1, True, False, 2, 3}
    print(scores)

    # ============================================================
    # SETS: Membership
    # ============================================================
    print(20 in scores)
    print(99 in scores)

    # ============================================================
    # SETS: Add and Update
    # ============================================================
    scores.add(50)
    print(scores)

    more_scores = {60, 70}
    scores.update(more_scores)
    print(scores)

    scores.update([80, 90])
    print(scores)

    # ============================================================
    # SETS: Union (New Set)
    # ============================================================
    a = {1, 2, 3}
    b = {4, 5, 6}

    new_set = a.union(b)
    print(new_set)

    # ============================================================
    # SETS: Intersection (Duplicates Only)
    # ============================================================
    a = {1, 2, 3, 4}
    b = {3, 4, 5}

    a.intersection_update(b)
    print(a)

    # ============================================================
    # SETS: Symmetric Difference (No Overlap)
    # ============================================================
    a = {1, 2, 3, 4}
    b = {3, 4, 5}

    a.symmetric_difference_update(b)
    print(a)

def topic_loops():
    """
    TOPIC: Loops (while / for / range / break / continue / else / nested)
    """

    # ============================================================
    # WHILE LOOP: Basic counting
    # ============================================================
    counter = 1
    while counter <= 5:
        print("Counter:", counter)
        counter += 1


    # ============================================================
    # WHILE LOOP: break
    # ============================================================
    counter = 1
    while counter <= 10:
        print("Counter:", counter)
        if counter == 4:
            print("Breaking early!")
            break
        counter += 1


    # ============================================================
    # WHILE LOOP: continue
    # ============================================================
    counter = 0
    while counter < 6:
        counter += 1
        if counter == 3:
            print("Skipping 3")
            continue
        print("Counter:", counter)


    # ============================================================
    # WHILE LOOP: else
    # ============================================================
    counter = 1
    while counter <= 3:
        print("Counting:", counter)
        counter += 1
    else:
        print("While loop finished cleanly")


    # ============================================================
    # FOR LOOP: Iterating over a list
    # ============================================================
    people = ["Liam", "Emma", "Noah"]
    for person in people:
        print(person)


    # ============================================================
    # FOR LOOP: Iterating over a string
    # ============================================================
    for char in "Python":
        print(char)


    # ============================================================
    # FOR LOOP: break
    # ============================================================
    for person in people:
        if person == "Emma":
            print("Stopping at Emma")
            break
        print(person)


    # ============================================================
    # FOR LOOP: continue
    # ============================================================
    for person in people:
        if person == "Emma":
            print("Skipping Emma")
            continue
        print(person)


    # ============================================================
    # FOR LOOP: range()
    # ============================================================
    for num in range(3):
        print("range(3):", num)

    for num in range(2, 5):
        print("range(2, 5):", num)

    for num in range(10, 51, 10):
        print("range(10, 51, 10):", num)
    else:
        print("Finished counting by tens!")


    # ============================================================
    # NESTED LOOPS
    # ============================================================
    names = ["Ava", "Mason", "Lucas"]
    activities = ["reads", "builds", "relaxes"]

    for activity in activities:
        for name in names:
            print(name + " " + activity + ".")

def topic_functions():
    """
    TOPIC: Functions (basics, parameters, defaults, *args, **kwargs)
    """

    # ============================================================
    # BASIC FUNCTION
    # ============================================================
    def greet():
        print("Hello from a function!")

    greet()


    # ============================================================
    # FUNCTION WITH PARAMETERS + DEFAULT VALUES
    # ============================================================
    def add_numbers(a=0, b=0):
        if not isinstance(a, int) or not isinstance(b, int):
            return 0
        return a + b

    result = add_numbers(8, 4)
    print("Sum:", result)

    print("Sum with defaults:", add_numbers())
    print("Invalid input:", add_numbers("8", 4))


    # ============================================================
    # *args (Multiple Positional Arguments)
    # ============================================================
    def show_items(*items):
        print(items)
        print(type(items))

    show_items("Apple", "Banana", "Cherry")


    # ============================================================
    # **kwargs (Multiple Named Arguments)
    # ============================================================
    def show_profile(**details):
        print(details)
        print(type(details))

    show_profile(first_name="Liam", last_name="Walker", age=28)

def topic_recursion():
    """
    TOPIC: Recursion (function calling itself)
    """
    # ============================================================
    # RECURSIVE FUNCTION
    # ============================================================
    def add_one(number):
        print("Current value:", number)
        if number >= 9:
            return number + 1

        return add_one(number + 1)

    # Start recursion
    final_result = add_one(0)
    print("Final result:", final_result)

def topic_scope():
    """
    TOPIC: Variable Scope (global, local, nonlocal)
    """

    # ============================================================
    # GLOBAL SCOPE
    # ============================================================
    name = "Alex"
    count = 1

    print("Initial global count:", count)


    # ============================================================
    # FUNCTION WITH GLOBAL + NESTED FUNCTION
    # ============================================================
    def outer_function():
        nonlocal_name = "blue"
        nonlocal_count_holder = {"count": count}  # avoid modifying real globals

        print("\nInside outer_function")
        print("Starting count:", nonlocal_count_holder["count"])

        def inner_function(person):
            nonlocal nonlocal_name
            nonlocal_name = "red"

            nonlocal_count_holder["count"] += 1

            print("Inner function color:", nonlocal_name)
            print("Hello,", person)
            print("Updated count:", nonlocal_count_holder["count"])

        inner_function(name)

    outer_function()

def topic_string_formatting():
    """
    TOPIC: String Formatting (concatenation, %, format(), f-strings)
    """

    person = "Harris"
    coins = 3

    # ============================================================
    # STRING CONCATENATION (Old school)
    # ============================================================
    print("\n" + person + " has " + str(coins) + " coins left.")


    # ============================================================
    # %-STYLE FORMATTING (Legacy)
    # ============================================================
    message = "\n%s has %s coins left." % (person, coins)
    print(message)


    # ============================================================
    # str.format() METHOD
    # ============================================================
    message = "\n{} has {} coins left.".format(person, coins)
    print(message)

    message = "\n{1} has {0} coins left.".format(coins, person)
    print(message)

    message = "\n{person} has {coins} coins left.".format(
        coins=coins,
        person=person
    )
    print(message)

    player = {"person": "Dave", "coins": 3}
    message = "\n{person} has {coins} coins left.".format(**player)
    print(message)


    # ============================================================
    # F-STRINGS (Modern & Recommended)
    # ============================================================
    message = f"\n{person} has {coins} coins left."
    print(message)

    message = f"\n{person} has {2 * 5} coins left."
    print(message)

    message = f"\n{person.lower()} has {2 * 5} coins left."
    print(message)

    message = f"\n{player['person']} has {2 * 5} coins left."
    print(message)


    # ============================================================
    # F-STRING FORMAT SPECIFIERS
    # ============================================================
    num = 10
    print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

    for num in range(1, 11):
        print(f"2.25 times {num} is {2.25 * num:.2f}")

    print()

    for num in range(1, 11):
        print(f"{num} divided by 4.52 is {num / 4.52:.2%}")


def topic_modules():
    """
    TOPIC: Modules and Imports
    """

    # ============================================================
    # STANDARD LIBRARY IMPORTS
    # ============================================================
    from math import pi
    import random as rnd
    import sys
    from enum import Enum

    print("Value of pi:", pi)


    # ============================================================
    # CUSTOM MODULE IMPORT
    # ============================================================
    import space_facts

    # ============================================================
    # USING VALUES FROM A CUSTOM MODULE
    # ============================================================
    print("Closest planet to the Sun:", space_facts.closest_planet)
    print("Largest planet:", space_facts.largest_planet)

    space_facts.random_space_fact()


    # ============================================================
    # __name__ BEHAVIOR
    # ============================================================
    print("__name__ in modules.py:", __name__)
    print("space_facts.__name__:", space_facts.__name__)


def topic_argparse():
    """
    TOPIC: Command-Line Arguments (argparse)
    """

    import argparse

    # ============================================================
    # FUNCTION THAT USES ARGUMENTS
    # ============================================================
    def greet(name, language):
        greetings = {
            "English": "Hello",
            "Spanish": "Hola",
            "German": "Hallo",
        }

        message = f"{greetings[language]} {name}!"
        print(message)


    # ============================================================
    # ARGPARSE SETUP
    # ============================================================
    parser = argparse.ArgumentParser(
        description="Prints a greeting in the selected language."
    )

    parser.add_argument(
        "-n", "--name",
        required=True,
        help="Name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang",
        required=True,
        choices=["English", "Spanish", "German"],
        help="Language of the greeting"
    )

    args = parser.parse_args()

    greet(args.name, args.lang)

def topic_functional():
    """
    TOPIC: Functional Programming (lambda, closures, map, filter, reduce)
    """

    from functools import reduce

    # ============================================================
    # LAMBDA BASICS (same as small one-line functions)
    # ============================================================
    def square(n):
        return n * n

    def add_two(n):
        return n + 2

    def add(a, b):
        return a + b

    print(square(3))
    print(add_two(15))
    print(add(11, 9))


    # ============================================================
    # FUNCTION BUILDER / CLOSURE
    # ============================================================
    def make_adder(x):
        return lambda n: n + x

    add_5 = make_adder(5)
    add_12 = make_adder(12)

    print(add_5(7))
    print(add_12(7))


    # ============================================================
    # map(): transform each item
    # ============================================================
    nums = [4, 6, 9, 13, 18, 21]
    squared_nums = map(lambda n: n * n, nums)
    print(list(squared_nums))


    # ============================================================
    # filter(): keep only items that match condition
    # ============================================================
    odd_nums = filter(lambda n: n % 2 != 0, nums)
    print(list(odd_nums))


    # ============================================================
    # reduce(): combine items into a single value
    # ============================================================
    nums2 = [1, 2, 3, 4, 5, 1]
    total = reduce(lambda acc, curr: acc + curr, nums2, 10)
    print(total)

    # Built-in alternative for summing numbers
    print(sum(nums2, 10))


    # ============================================================
    # reduce() example: total characters across names
    # ============================================================
    names = ["Ava Chen", "Noah Patel", "Sofia Hernandez"]
    char_count = reduce(lambda acc, name: acc + len(name), names, 0)
    print(char_count)

def topic_oop():
    """
    TOPIC: Object-Oriented Programming (classes, inheritance, polymorphism)
    """

    # ============================================================
    # BASE CLASS
    # ============================================================
    class Vehicle:
        def __init__(self, make, model):
            self.make = make
            self.model = model

        def move(self):
            print("Moves along...")

        def describe(self):
            print(f"I'm a {self.make} {self.model}.")


    # ============================================================
    # CHILD CLASSES (Inheritance)
    # ============================================================
    class Airplane(Vehicle):
        def __init__(self, make, model, faa_id):
            super().__init__(make, model)
            self.faa_id = faa_id

        def move(self):
            print("Flies through the sky...")


    class Truck(Vehicle):
        def move(self):
            print("Rumbles down the road...")


    class GolfCart(Vehicle):
        pass


    # ============================================================
    # OBJECT CREATION
    # ============================================================
    car_one = Vehicle("Tesla", "Model Y")
    car_two = Vehicle("Ford", "Mustang")

    plane = Airplane("Cessna", "Skyhawk", "N-54321")
    truck = Truck("Volvo", "VNL")
    cart = GolfCart("Yamaha", "Drive2")


    # ============================================================
    # METHOD CALLS
    # ============================================================
    car_one.describe()
    car_one.move()

    car_two.describe()
    car_two.move()

    plane.describe()
    plane.move()

    truck.describe()
    truck.move()

    cart.describe()
    cart.move()


    # ============================================================
    # POLYMORPHISM (same method, different behavior)
    # ============================================================
    print("\n--- Polymorphism Demo ---")
    for vehicle in (car_one, car_two, plane, truck, cart):
        vehicle.describe()
        vehicle.move()

def topic_exceptions():
    """
    TOPIC: Exceptions (custom exceptions, try / except / else / finally)
    """

    # ============================================================
    # CUSTOM EXCEPTION
    # ============================================================
    class JustNotCoolError(Exception):
        pass


    # ============================================================
    # TRY / EXCEPT / ELSE / FINALLY DEMO
    # ============================================================
    x = 2

    try:
        # Uncomment one line at a time to see different exceptions
        #raise JustNotCoolError("This just isn't cool, man.")
        # raise Exception("I'm a custom exception!")
        print(x / 0)
        # if not isinstance(x, str):
        #     raise TypeError("Only strings are allowed.")

    except NameError:
        print("NameError means something is probably undefined.")

    except ZeroDivisionError:
        print("Please do not divide by zero.")

    except TypeError as error:
        print("TypeError:", error)

    except Exception as error:
        print("Caught exception:", error)

    else:
        print("No errors!")

    finally:
        print("I'm going to print with or without an error.")


# ============================================================
# Runner
# ============================================================
TOPICS = {
    1: ("Strings + Types", topic_strings),
    2: ("Menu Formatting", topic_menu_formatting),
    3: ("Core Data Types", topic_data_types),
    4: ("User Input", topic_user_input),
    5: ("Rock Paper Scissors", topic_rps),
    6: ("Lists", topic_lists),
    7: ("Tuples", topic_tuples),
    8: ("Dictionaries", topic_dict_sets),
    9: ("Loops", topic_loops),
    10: ("Functions", topic_functions),
    11: ("Recursion", topic_recursion),
    12: ("Scope", topic_scope),
    13: ("f-strings", topic_string_formatting),
    14: ("Modules", topic_modules),
    15: ("Argparse", topic_argparse),
    16: ("Lambda", topic_functional),
    17: ("OOP/Classes", topic_oop),
    18: ("Exceptions", topic_exceptions)
}


def run_all():
    for key in sorted(TOPICS.keys()):
        name, func = TOPICS[key]
        print(f"\n\n########## Running: {key}) {name} ##########")
        func()
        pause()


def main():
    while True:
        print("\n\n========== PYTHON PRACTICE MENU ==========")
        print("0) Run ALL")
        for key in sorted(TOPICS.keys()):
            print(f"{key}) {TOPICS[key][0]}")
        print("q) Quit")
        choice = input("\nChoose an option: ").strip()
        if choice.isdigit():
            choice = int(choice)

        if (choice == "q" or choice == "Q"):
            print("Goodbye!")
            break
        if choice == "0":
            run_all()
            continue

        topic = TOPICS.get(choice)
        if not topic:
            print("Invalid choice. Try again.")
            continue

        _, func = topic
        func()
        pause()


if __name__ == "__main__":
    main()
