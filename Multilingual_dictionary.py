import tkinter as tk
from tkinter import messagebox

# Sample dictionaries (these should be replaced with your group members' actual dictionaries)
french_dict = {
    'hello': 'bonjour',
    'cat': 'chat',
    'dog': 'chien',
}

spanish_dict = {
    'hello': 'halo',
    'cat': 'gato',
    'dog': 'perro',
}

german_dict = {
    'hello': 'hallo',
    'cat': 'katze',
    'dog': 'hund',
}

# Combine all dictionaries into one multilingual dictionary
multilingual_dict = {
    'French': french_dict,
    'Spanish': spanish_dict,
    'German': german_dict,
}

# Function to perform translation lookup
def translate_word():
    language = language_var.get()  # Selected language
    word = word_entry.get().lower()  # Word entered by the user

    # Check if word exists in selected language dictionary
    if word in multilingual_dict[language]:
        translation = multilingual_dict[language][word]
        result_label.config(text=f"Translation: {translation}")
    else:
        result_label.config(text="Word not found in the dictionary.")
        messagebox.showwarning("Word Not Found", f"The word '{word}' is not in the {language} dictionary.")

# Create main window
root = tk.Tk()
root.title("Multilingual Dictionary")

# Language selection (Dropdown)
language_var = tk.StringVar(value="French")  # Default to French
language_menu = tk.OptionMenu(root, language_var, *multilingual_dict.keys())
language_menu.pack(pady=10)

# Entry widget to input the word
word_entry = tk.Entry(root, font=('Arial', 14))
word_entry.pack(pady=10)

# Button to trigger translation
translate_button = tk.Button(root, text="Translate", font=('Arial', 14), command=translate_word)
translate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
