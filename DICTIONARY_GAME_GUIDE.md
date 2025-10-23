# Dictionary Adventure Game - Learning Guide

## 🎮 About the Game

This is an interactive adventure game designed to teach Python dictionary concepts in a fun and engaging way!

## 📚 What You'll Learn

### 1. **Creating Dictionaries**
```python
character = {
    'name': 'Hero',
    'health': 100,
    'gold': 50,
    'level': 1,
    'inventory': ['sword', 'potion']
}
```

### 2. **Accessing Dictionary Values**
```python
print(character['name'])  # Output: Hero
print(character['health']) # Output: 100
```

### 3. **Updating Dictionary Values**
```python
character['gold'] += 50      # Add gold
character['health'] -= 20    # Take damage
character['level'] = 2       # Level up
```

### 4. **Adding New Items to Lists Within Dictionaries**
```python
character['inventory'].append('magic sword')
```

### 5. **Iterating Through Dictionaries**
```python
for key, value in character.items():
    print(f"{key}: {value}")
```

### 6. **Nested Dictionaries**
```python
encounters = {
    'treasure': {
        'description': 'You found treasure!',
        'gold': 50
    },
    'monster': {
        'description': 'A monster appears!',
        'damage': 20
    }
}
```

## 🎯 Game Features

1. **Character Creation** - Build your character using a dictionary
2. **Forest Exploration** - Random encounters using nested dictionaries
3. **Inventory System** - Manage items stored in a list within your character dictionary
4. **Combat System** - Update health and gain rewards
5. **Level Up System** - Track experience and increase levels
6. **Item Usage** - Use items with effects defined in dictionaries
7. **Scoring System** - Calculate final score from dictionary values

## 🚀 How to Play

1. Run the game:
   ```bash
   python dictionary_adventure_game.py
   ```

2. Create your character by entering a name

3. Choose actions each turn:
   - **Explore**: Find treasures, fight monsters, or meet merchants
   - **Use Item**: Consume potions or use special items
   - **Check Stats**: View your character dictionary
   - **Rest**: Restore health
   - **Quit**: Exit the game

4. Survive 10 turns and maximize your score!

## 💡 Dictionary Concepts in Action

### Character Stats (Simple Dictionary)
The character is stored as a dictionary with various attributes:
- `name`: String value
- `health`: Integer value (0-100)
- `gold`: Integer value
- `level`: Integer value
- `experience`: Integer value
- `inventory`: List value (contains items)

### Random Encounters (Nested Dictionary)
Each encounter type has its own sub-dictionary with specific properties:
```python
encounters = {
    'treasure': {...},
    'monster': {...},
    'merchant': {...}
}
```

### Item Effects (Dictionary Mapping)
Items are mapped to their effects using a dictionary:
```python
item_effects = {
    'health potion': {'health': 30, 'message': 'Restored 30 health!'},
    'magic amulet': {'gold': 25, 'message': 'Grants 25 gold!'}
}
```

## 🎓 Key Takeaways

1. **Dictionaries are perfect for storing related data** - All character information in one place
2. **Keys can be strings** - Like 'name', 'health', 'gold'
3. **Values can be any data type** - Integers, strings, lists, even other dictionaries!
4. **Easy to update** - Change values using `dictionary[key] = new_value`
5. **Dynamic** - Add new items to lists within dictionaries
6. **Organized** - Group related information together

## 🌟 Challenges

Try modifying the game to practice more dictionary skills:

1. Add a new character attribute (e.g., 'strength', 'magic')
2. Create new item types with different effects
3. Add more encounter types to the encounters dictionary
4. Create a shop system with items in a dictionary
5. Add character classes (warrior, mage, rogue) as a dictionary

## 📝 Notes for Beginners

- A **dictionary** is like a real-world dictionary: you look up a word (key) to find its definition (value)
- **Keys** must be unique within a dictionary
- **Values** can be duplicated and can be any data type
- Use **square brackets** `[]` to access values: `character['name']`
- Use **`.items()`** to loop through both keys and values
- Use **`.keys()`** to loop through just keys
- Use **`.values()`** to loop through just values

Have fun learning dictionaries through adventure! 🗡️✨
