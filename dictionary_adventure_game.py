"""
Dictionary Adventure Game - A beginner-friendly Python game
This game teaches dictionary concepts through an interactive adventure!

Learning objectives:
- Creating and using dictionaries
- Accessing dictionary values
- Updating dictionary values
- Adding new key-value pairs
- Iterating through dictionaries
"""

import random
import time

def print_slow(text, delay=0.03):
    """Print text with a typing effect for better engagement"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_character(character):
    """Display character stats in a formatted way"""
    print("\n" + "="*40)
    print(f"⚔️  {character['name']}'s Character Sheet")
    print("="*40)
    for key, value in character.items():
        if key == 'inventory':
            print(f"🎒 {key.capitalize()}: {', '.join(value) if value else 'Empty'}")
        else:
            print(f"   {key.capitalize()}: {value}")
    print("="*40 + "\n")

def create_character():
    """Create a character using a dictionary"""
    print_slow("\n🎮 Welcome to Dictionary Adventure! 🎮\n")
    print_slow("Let's create your character!\n")

    name = input("Enter your character's name: ").strip()

    # Creating a character dictionary
    character = {
        'name': name,
        'health': 100,
        'gold': 50,
        'level': 1,
        'experience': 0,
        'inventory': ['wooden sword', 'health potion']
    }

    print_slow(f"\n✨ {name} has been created! ✨\n")
    display_character(character)

    return character

def explore_forest(character):
    """Forest exploration event"""
    print_slow("\n🌲 You enter a mysterious forest...")
    time.sleep(1)

    # Random encounters stored in a dictionary
    encounters = {
        'treasure': {
            'description': '💰 You found a treasure chest!',
            'gold': random.randint(20, 50),
            'item': random.choice(['magic amulet', 'silver ring', 'ancient map'])
        },
        'monster': {
            'description': '👹 A goblin appears!',
            'damage': random.randint(10, 25),
            'reward_gold': random.randint(15, 30),
            'reward_xp': random.randint(20, 40)
        },
        'merchant': {
            'description': '🧙 You meet a friendly merchant!',
            'item': random.choice(['mega potion', 'shield', 'lucky charm']),
            'cost': 30
        }
    }

    # Randomly select an encounter
    encounter_type = random.choice(list(encounters.keys()))
    encounter = encounters[encounter_type]

    print_slow(encounter['description'])
    time.sleep(1)

    if encounter_type == 'treasure':
        # Update character's gold (dictionary update)
        character['gold'] += encounter['gold']
        # Add item to inventory (list within dictionary)
        character['inventory'].append(encounter['item'])
        print_slow(f"You gained {encounter['gold']} gold and found a {encounter['item']}!")

    elif encounter_type == 'monster':
        print_slow("⚔️  Battle time!")
        choice = input("Fight (f) or Run (r)? ").lower()

        if choice == 'f':
            # Update character's health (dictionary update)
            character['health'] -= encounter['damage']
            print_slow(f"You took {encounter['damage']} damage!")

            if character['health'] > 0:
                print_slow("💪 You defeated the goblin!")
                character['gold'] += encounter['reward_gold']
                character['experience'] += encounter['reward_xp']
                print_slow(f"Gained {encounter['reward_gold']} gold and {encounter['reward_xp']} XP!")

                # Level up system
                if character['experience'] >= 100:
                    character['level'] += 1
                    character['experience'] = 0
                    character['health'] = 100  # Restore health on level up
                    print_slow(f"\n🎉 LEVEL UP! You are now level {character['level']}! 🎉")
            else:
                print_slow("💀 You were defeated... Game Over!")
                return False
        else:
            print_slow("🏃 You ran away safely!")

    elif encounter_type == 'merchant':
        if character['gold'] >= encounter['cost']:
            choice = input(f"Buy {encounter['item']} for {encounter['cost']} gold? (y/n): ").lower()
            if choice == 'y':
                character['gold'] -= encounter['cost']
                character['inventory'].append(encounter['item'])
                print_slow(f"Purchased {encounter['item']}! Added to inventory.")
        else:
            print_slow("You don't have enough gold...")

    return True

def use_item(character):
    """Use an item from inventory"""
    if not character['inventory']:
        print_slow("Your inventory is empty!")
        return

    print("\n🎒 Inventory:")
    for i, item in enumerate(character['inventory'], 1):
        print(f"{i}. {item}")

    try:
        choice = int(input("\nEnter item number to use (0 to cancel): "))
        if choice == 0:
            return

        if 1 <= choice <= len(character['inventory']):
            item = character['inventory'][choice - 1]

            # Item effects dictionary
            item_effects = {
                'health potion': {'health': 30, 'message': '❤️  Restored 30 health!'},
                'mega potion': {'health': 50, 'message': '❤️  Restored 50 health!'},
                'wooden sword': {'message': '⚔️  Can\'t use this now!'},
                'magic amulet': {'gold': 25, 'message': '✨ The amulet grants you 25 gold!'},
                'silver ring': {'experience': 15, 'message': '💫 You gain 15 experience!'},
                'shield': {'message': '🛡️  Can\'t use this now!'},
                'lucky charm': {'gold': 40, 'message': '🍀 Lucky! You find 40 gold!'},
                'ancient map': {'gold': 35, 'experience': 20, 'message': '🗺️  The map reveals treasure!'}
            }

            if item in item_effects:
                effect = item_effects[item]
                print_slow(effect['message'])

                if 'health' in effect:
                    character['health'] = min(100, character['health'] + effect['health'])
                if 'gold' in effect:
                    character['gold'] += effect['gold']
                if 'experience' in effect:
                    character['experience'] += effect['experience']

                # Remove consumable items
                if 'potion' in item or item in ['magic amulet', 'lucky charm', 'ancient map']:
                    character['inventory'].remove(item)
                    print_slow(f"{item} was consumed.")
    except (ValueError, IndexError):
        print_slow("Invalid choice!")

def main():
    """Main game loop"""
    character = create_character()
    game_over = False
    turns = 0
    max_turns = 10

    print_slow("\n📜 Your quest: Survive 10 turns and collect as much treasure as possible!\n")
    input("Press Enter to begin your adventure...")

    while not game_over and turns < max_turns and character['health'] > 0:
        turns += 1
        print_slow(f"\n--- Turn {turns}/{max_turns} ---")

        print("\nWhat do you want to do?")
        print("1. Explore the forest")
        print("2. Use an item")
        print("3. Check character stats")
        print("4. Rest (restore 20 health)")
        print("5. Quit game")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            if not explore_forest(character):
                game_over = True
        elif choice == '2':
            use_item(character)
        elif choice == '3':
            display_character(character)
        elif choice == '4':
            character['health'] = min(100, character['health'] + 20)
            print_slow("😴 You rest and restore 20 health.")
        elif choice == '5':
            print_slow("Thanks for playing!")
            return
        else:
            print_slow("Invalid choice! Try again.")
            turns -= 1  # Don't count invalid turns
            continue

    # Game ending
    print_slow("\n" + "="*40)
    print_slow("🎮 GAME OVER 🎮")
    print_slow("="*40)

    if character['health'] > 0:
        print_slow(f"\n🏆 Congratulations {character['name']}! You survived!")
    else:
        print_slow(f"\n💀 {character['name']} has fallen in battle...")

    display_character(character)

    # Calculate score using dictionary values
    score = character['gold'] + (character['level'] * 50) + (len(character['inventory']) * 10)
    print_slow(f"📊 Final Score: {score} points!\n")

    # Score rankings (dictionary)
    rankings = {
        0: "Novice Adventurer",
        100: "Brave Explorer",
        200: "Skilled Warrior",
        300: "Master Adventurer",
        500: "Legendary Hero"
    }

    # Find appropriate rank
    rank = "Novice Adventurer"
    for points, title in sorted(rankings.items(), reverse=True):
        if score >= points:
            rank = title
            break

    print_slow(f"🌟 Your rank: {rank}! 🌟\n")

if __name__ == "__main__":
    main()
