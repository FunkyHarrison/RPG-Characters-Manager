import json
from pathlib import Path

character_path = Path(__file__).resolve().parent / "RPGcharacters.json"
#Empty file recovery test: PASS#

def ask_for_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Values must be in whole numbers.")
        return None


def save_characters(characters):
    with character_path.open("w", encoding="utf-8") as file:
        json.dump(characters, file, indent=4)


def load_characters():
    if not character_path.exists():
        return []

    try:
        with character_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("The character file is empty or contains invalid JSON.")
        return []


def heal_character(characters):
    if not characters:
        print("there are no characters.")
        return
    view_characters(characters)
    try:
        character_number = ask_for_int("Which character do you want to heal? ")
        if character_number is None:
            return

        if character_number < 1 or character_number > len(characters):
            print("That character does not exist.")
            return

        heal_amount = int(input("How much health do they gain? "))

        if heal_amount < 1:
            print("Health gain must be at least 1.")
            return

        character = characters[character_number - 1]

        character["health"] += heal_amount

    except ValueError:
        print("Values must be in whole numbers.")
        return


    if character["health"] > character["max_health"]:
        character["health"] = character["max_health"]

    save_characters(characters)

    if character["health"] == character["max_health"]:
        print(f"{character['name']} is max health!")
    else:
        print(
            f"{character['name']} has recovered {heal_amount} health! "
            f"and has {character['health']} health remaining."
        )


def damage_character(characters):
    if not characters:
        print("there are no characters.")
        return
    view_characters(characters)
    try:
        character_number = ask_for_int("which character should take damage? ")
        if character_number is None:
            return

        if character_number < 1 or character_number > len(characters):
            print("That character does not exist.")
            return

        damage_amount = int(input("How much damage did they take? "))

        if damage_amount < 1:
            print("Damage must be at least 1.")
            return

        character = characters[character_number - 1]

        character["health"] -= damage_amount

    except ValueError:
        print("Values must be in whole numbers.")
        return

    if character["health"] < 0:
        character["health"] = 0

    save_characters(characters)

    if character["health"] == 0:
        print(f"{character['name']} has been slain!")
    else:
        print(
            f"{character['name']} has taken {damage_amount} damage! "
            f"and has {character['health']} health remaining."
        )


def add_characters(characters):
    character_name = input("What is the character's name? ").strip()

    if not character_name:
        print("No character name was added.")
        return

    try:
        character_level = int(input("what is the character's level? "))
        maximum_health = int(input("what is the charachter's maximum health? "))
    except ValueError:
        print("Level and health must be whole numbers.")
        return

    if character_level < 1 or maximum_health < 1:
        print("Level and maximum health must be at least 1.")
        return

    new_character = {
        "name": character_name,
        "level": character_level,
        "health": maximum_health,
        "max_health": maximum_health,
    }

    characters.append(new_character)
    save_characters(characters)
    print("Character added and saved.")


def view_characters(characters):
    if not characters:
        print("You have no saved characters.")
        return

    print("\n--- SAVED CHARACTERS ---")

    for index, character in enumerate(characters):
        if character["health"] > 0:
            status = "alive"
        else:
            status = "dead"

        print(
            f"{index + 1}. {character['name']} | "
            f"Level: {character['level']} | "
            f"HP: {character['health']}/{character['max_health']} | "
            f"{status}"
        )


def delete_characters(characters):
    if not characters:
        print("there are no characters.")
        return
    view_characters(characters)
    try:
        character_number = int(input("which character should be deleted? "))

        if character_number < 1 or character_number > len(characters):
            print("That character does not exist.")
            return
    except ValueError:
        print("Selection must be a whole number.")
        return
    deleted_character = characters.pop(character_number - 1)
    save_characters(characters)
    print(f"{deleted_character['name']} deleted.")

def main():
    characters = load_characters()


    while True:
        print("\n--- RPG CHARACTER MANAGER ---")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Damage Character")
        print("4. Heal Character")
        print("5. Delete character")
        print("6. Quit")

        choice = input("choose an option: ")

        if choice == "1":
            add_characters(characters)
        elif choice == "2":
            view_characters(characters)
        elif choice == "3":
            damage_character(characters)
        elif choice == "4":
            heal_character(characters)
        elif choice == "5":
            delete_characters(characters)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()