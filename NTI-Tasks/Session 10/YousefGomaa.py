import os
from pdfminer.high_level import extract_text

def select_book(directory):
    files = os.listdir(directory)

    books = [file for file in files if file.endswith('.pdf')]

    print("Available books:")
    for i, book in enumerate(books):
        print(f"{i+1}. {book}")

    while True:
        try:
            choice = int(input("Enter the number of the book you want to read: "))
            if choice < 1 or choice > len(books):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid book number.")

    return books[choice-1]

directory = 'Session 10\CV'
selected_book = select_book(directory)
print(f"You selected: {selected_book}")

text = extract_text(directory+"\\"+selected_book)

print("Parsed text:")
print(text)