import tkinter as tk
from tkinter import ttk

# French Dictionary (English to French)
French_dictionary = {'good morning': 'bonne matinée',
                     'good afternoon': 'bon après-midi',
                     'good evening': 'bonsoir',
                     'good night': 'bonne nuit',
                     'hello': 'bonjour',
                     'bye': 'au revoir',
                     'sit down': 'asseyez-vous',
                     'stand up': 'levez-vous',
                     'go': 'allez',
                     'come': 'viens',
                     'welcome': 'bienvenue',
                     'shut up': 'silence',
                     'friend': 'amie',
                     'enemy': 'ennemie',
                     'sorry': 'désolée',
                     'teacher': 'professeure',
                     'bless you': 'á dieu',
                     'excuse me': 'excusez-moi',
                     'please': 's\'il vous plaît',
                     'thank you': 'merci'}

def search_word():
    """
    Searches for the French translation of the entered English word and updates the result label.
    """
    word = word_entry.get().lower()  # Convert entered word to lowercase
    translation = French_dictionary.get(word)  # Get translation using get() method

    if translation:
        result_label.config(text=f"{word}: {translation}")
    else:
        result_label.config(text="Word not found, click the 'Show Available Words' button")

def show_words():
    """
    Displays the words available in the dictionary.
    """
    words_listbox.delete(0, tk.END)  # Clear the listbox
    for word in French_dictionary.keys():
        words_listbox.insert(tk.END, word)

# App begins
root = tk.Tk()
root.geometry("600x250")
root.title("French Dictionary")

# Entry space for user input
word_entry = tk.Entry(root)
word_entry.pack()

# Search button
search_button = tk.Button(root, text="Search", command=search_word)
search_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()