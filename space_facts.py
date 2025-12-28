from random import choice

closest_planet = "Mercury"
largest_planet = "Jupiter"
brightest_star = "Sirius"


def random_space_fact():
    facts = [
        "Venus is hotter than Mercury despite being farther from the Sun.",
        "Jupiter is so large that all other planets could fit inside it.",
        "A day on Venus is longer than a year on Venus.",
        "Neutron stars can spin hundreds of times per second."
    ]

    print(choice(facts))


# ============================================================
# RUN ONLY WHEN THIS FILE IS EXECUTED DIRECTLY
# ============================================================
if __name__ == "__main__":
    random_space_fact()
