import random
import time

# ---------------------------------------------
#  The Sludge Pit
#  A weird text-based survival game starring
#  Glep, the Anomalous Amoeba.
# ---------------------------------------------

def chirp_event():
    """Return a random nonsense message for The Chirp."""
    messages = [
        "The fence is blue on Tuesdays.",
        "Gravity remembers your face.",
        "The spoon asks why.",
        "Your reflection dreams in porcelain.",
        "Silence chews loudly tonight.",
        "The triangle hums approvingly."
    ]
    return random.choice(messages)

def main():
    print("\n====== THE SLUDGE PIT ======\n")
    print("You are Glep, an Anomalous Amoeba drifting in a non-Euclidean pond.\n")
    print("Survive 50 turns without losing yourself to Viscosity or Dread.\n")

    # Initial stats
    viscosity = 50
    dread = 25
    turn = 1
    MAX_TURNS = 50

    while turn <= MAX_TURNS:
        print(f"\n--- Turn {turn}/{MAX_TURNS} ---")

        # 5% chance of The Chirp
        if random.random() < 0.05:
            print("\n*** THE CHIRP OCCURS ***")
            print(chirp_event())
            print("Time stands very still. Nothing changes this turn...")
            # Stats freeze; skip normal turn effects
            turn += 1
            continue

        # Passive dread gain per turn
        dread += 1

        # Display stats
        print(f"Viscosity: {viscosity}/100")
        print(f"Existential Dread: {dread}/100\n")

        # Check loss conditions
        if viscosity <= 0:
            print("You dissolve into a thin smear of hypotheticals. (Viscosity hit 0)")
            return
        if viscosity >= 100:
            print("You congeal into a solid lump of regret. (Viscosity hit 100)")
            return
        if dread >= 100:
            print("You achieve ultimate self-awareness and cease to be. (Dread hit 100)")
            return

        # Player actions
        print("Choose your action:")
        print("1. Consume Glop        (+10–15 Viscosity, -2–5 Dread)")
        print("2. Expel Pseudopods    (-5–10 Viscosity, +5–10 Dread)")
        print("3. Ponder Existence    (+20–30 Viscosity, -15–25 Dread)")
        choice = input("> ").strip()

        if choice == "1":
            delta_v = random.randint(10, 15)
            delta_d = -random.randint(2, 5)
            viscosity += delta_v
            dread += delta_d
            print(f"\nYou absorb a nearby globule of nutrient sludge.")
            print(f"Viscosity +{delta_v}, Dread {delta_d}")

        elif choice == "2":
            delta_v = -random.randint(5, 10)
            delta_d = random.randint(5, 10)
            viscosity += delta_v
            dread += delta_d
            print("\nYou expel several expressive pseudopods.")
            print(f"Viscosity {delta_v}, Dread +{delta_d}")

        elif choice == "3":
            delta_v = random.randint(20, 30)
            delta_d = -random.randint(15, 25)
            viscosity += delta_v
            dread += delta_d
            print("\nYou stop moving and contemplate your slimy existence.")
            print(f"Viscosity +{delta_v}, Dread {delta_d}")

        else:
            print("\nYou attempt a non-action. Nothing happens.")
            # No change to stats

        turn += 1

    # If player survives all turns
    print("\n===================================")
    print("You have survived 50 turns in the Sludge Pit!")
    print("Glep persists... for now.")
    print("===================================\n")

if __name__ == "__main__":
    main()
