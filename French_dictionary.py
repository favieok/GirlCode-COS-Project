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
    word = word_entry.get().lower()
    translation = French_dictionary.get(word) 

    if translation:
        result_label.config(text=f"{translation}")
    else:
        result_label.config(text="Word not found, TRY AGAIN!!!")

# Dictionary begins
root = tk.Tk()
root.geometry("600x250")
root.title("French Dictionary")

# Entry space for the user's input
word_entry = tk.Entry(root)
word_entry.pack()

# The search button
search_button = tk.Button(root, text="SEARCH", command=search_word)
search_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
