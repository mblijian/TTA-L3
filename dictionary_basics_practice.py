"""
Dictionary Basics Practice - Start Here!
Complete these exercises before playing the adventure game.

A dictionary is a collection of key-value pairs.
Think of it like a real dictionary: you look up a WORD (key) to find its DEFINITION (value).
"""

print("="*50)
print("🐍 PYTHON DICTIONARY BASICS - PRACTICE EXERCISES 🐍")
print("="*50)

# ==========================================
# EXERCISE 1: Creating a Dictionary
# ==========================================
print("\n--- Exercise 1: Creating a Dictionary ---\n")

# Create a dictionary for a student
student = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A',
    'subjects': ['Math', 'Science', 'English']
}

print("Student dictionary created:")
print(student)

# TRY IT: Create your own dictionary for a book
# Include: title, author, pages, genre
print("\n📝 YOUR TURN: Create a book dictionary below")
book = {
    # Add your key-value pairs here
    'title': 'Python Adventure',
    'author': 'Code Master',
    'pages': 250,
    'genre': 'Educational'
}
print(book)


# ==========================================
# EXERCISE 2: Accessing Dictionary Values
# ==========================================
print("\n--- Exercise 2: Accessing Values ---\n")

# Access values using keys
print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")
print(f"Student grade: {student['grade']}")

# TRY IT: Access values from your book dictionary
print("\n📝 YOUR TURN: Print the book title and author")
print(f"Book title: {book['title']}")
print(f"Book author: {book['author']}")


# ==========================================
# EXERCISE 3: Updating Dictionary Values
# ==========================================
print("\n--- Exercise 3: Updating Values ---\n")

print(f"Original age: {student['age']}")
student['age'] = 21  # Update age
print(f"Updated age: {student['age']}")

print(f"Original grade: {student['grade']}")
student['grade'] = 'A+'  # Update grade
print(f"Updated grade: {student['grade']}")

# TRY IT: Update the number of pages in your book
print("\n📝 YOUR TURN: Change the number of pages to 300")
book['pages'] = 300
print(f"Updated pages: {book['pages']}")


# ==========================================
# EXERCISE 4: Adding New Key-Value Pairs
# ==========================================
print("\n--- Exercise 4: Adding New Items ---\n")

# Add a new key-value pair
student['email'] = 'alice@example.com'
print(f"Added email: {student['email']}")

student['gpa'] = 3.9
print(f"Added GPA: {student['gpa']}")

print("\nUpdated student dictionary:")
print(student)

# TRY IT: Add a 'publisher' key to your book dictionary
print("\n📝 YOUR TURN: Add a publisher to the book")
book['publisher'] = 'Learning Press'
print(f"Added publisher: {book['publisher']}")


# ==========================================
# EXERCISE 5: Removing Items from Dictionary
# ==========================================
print("\n--- Exercise 5: Removing Items ---\n")

# Remove a key-value pair
removed_value = student.pop('email')
print(f"Removed email: {removed_value}")
print("Student dictionary after removal:")
print(student)

# TRY IT: Remove the 'publisher' from your book
print("\n📝 YOUR TURN: Remove publisher from book")
book.pop('publisher')
print(book)


# ==========================================
# EXERCISE 6: Looping Through Dictionaries
# ==========================================
print("\n--- Exercise 6: Looping Through Dictionaries ---\n")

print("All student information:")
for key, value in student.items():
    print(f"  {key}: {value}")

print("\nOnly keys:")
for key in student.keys():
    print(f"  - {key}")

print("\nOnly values:")
for value in student.values():
    print(f"  - {value}")

# TRY IT: Loop through your book dictionary
print("\n📝 YOUR TURN: Print all book information")
for key, value in book.items():
    print(f"  {key}: {value}")


# ==========================================
# EXERCISE 7: Nested Dictionaries
# ==========================================
print("\n--- Exercise 7: Nested Dictionaries ---\n")

# A dictionary can contain other dictionaries!
school = {
    'student1': {
        'name': 'Alice',
        'grade': 'A'
    },
    'student2': {
        'name': 'Bob',
        'grade': 'B'
    },
    'student3': {
        'name': 'Charlie',
        'grade': 'A+'
    }
}

print("School dictionary:")
print(school)

# Access nested values
print(f"\nStudent 1 name: {school['student1']['name']}")
print(f"Student 2 grade: {school['student2']['grade']}")

# TRY IT: Create a library dictionary with 2 books
print("\n📝 YOUR TURN: Create a library with multiple books")
library = {
    'book1': {
        'title': 'Python Basics',
        'author': 'John Doe'
    },
    'book2': {
        'title': 'Advanced Python',
        'author': 'Jane Smith'
    }
}

for book_id, book_info in library.items():
    print(f"{book_id}: {book_info['title']} by {book_info['author']}")


# ==========================================
# EXERCISE 8: Checking if Key Exists
# ==========================================
print("\n--- Exercise 8: Checking if Keys Exist ---\n")

# Use 'in' to check if a key exists
if 'name' in student:
    print("✅ 'name' exists in student dictionary")

if 'phone' in student:
    print("✅ 'phone' exists in student dictionary")
else:
    print("❌ 'phone' does NOT exist in student dictionary")

# Safe way to access with .get()
email = student.get('email', 'No email found')
print(f"Email: {email}")

phone = student.get('phone', 'No phone found')
print(f"Phone: {phone}")


# ==========================================
# EXERCISE 9: Dictionary Methods
# ==========================================
print("\n--- Exercise 9: Useful Dictionary Methods ---\n")

# .keys() - Get all keys
print(f"All keys: {list(student.keys())}")

# .values() - Get all values
print(f"All values: {list(student.values())}")

# .items() - Get all key-value pairs
print(f"All items: {list(student.items())}")

# .clear() - Remove all items (be careful!)
temp_dict = {'a': 1, 'b': 2}
print(f"Before clear: {temp_dict}")
temp_dict.clear()
print(f"After clear: {temp_dict}")

# .copy() - Create a copy
student_copy = student.copy()
print(f"Student copy: {student_copy}")


# ==========================================
# MINI PROJECT: Simple Contact Book
# ==========================================
print("\n" + "="*50)
print("🎯 MINI PROJECT: Create a Contact Book")
print("="*50 + "\n")

contacts = {
    'Alice': {
        'phone': '555-0001',
        'email': 'alice@email.com',
        'age': 25
    },
    'Bob': {
        'phone': '555-0002',
        'email': 'bob@email.com',
        'age': 30
    },
    'Charlie': {
        'phone': '555-0003',
        'email': 'charlie@email.com',
        'age': 28
    }
}

print("📞 Contact Book:")
print("-" * 50)
for name, info in contacts.items():
    print(f"\nName: {name}")
    print(f"  Phone: {info['phone']}")
    print(f"  Email: {info['email']}")
    print(f"  Age: {info['age']}")

# Search for a contact
search_name = 'Bob'
if search_name in contacts:
    print(f"\n🔍 Found {search_name}!")
    print(f"  Phone: {contacts[search_name]['phone']}")
    print(f"  Email: {contacts[search_name]['email']}")

# Add a new contact
contacts['Diana'] = {
    'phone': '555-0004',
    'email': 'diana@email.com',
    'age': 27
}
print(f"\n✅ Added Diana to contacts!")

# Count contacts
print(f"\n📊 Total contacts: {len(contacts)}")


# ==========================================
# SUMMARY
# ==========================================
print("\n" + "="*50)
print("📚 SUMMARY - What You Learned")
print("="*50)
print("""
✅ Creating dictionaries with {}
✅ Accessing values with dictionary[key]
✅ Updating values with dictionary[key] = new_value
✅ Adding new key-value pairs
✅ Removing items with .pop()
✅ Looping through dictionaries with .items(), .keys(), .values()
✅ Using nested dictionaries
✅ Checking if keys exist with 'in'
✅ Using .get() for safe access
✅ Common dictionary methods

🎮 Now you're ready to play the Dictionary Adventure Game!
   Run: python dictionary_adventure_game.py
""")

print("="*50)
print("Great job! Keep practicing! 🌟")
print("="*50)
