import tkinter as tk

from tkinter import ttk


# Korean dictionary (English to Korean)
korean_dictionary = {
    'hello': 'annyeong',
    'come': 'oda',
    'go': 'gada',
    'stay': 'meomuleuda',
    'here': 'yeogi',
    'near': 'gakkaun',
    'far': 'meolli',
    'happy': 'haengboghada',
    'sad': 'saelpeun',
    'filled': 'chaeuneun',
    'hungry': 'baegopeun',
    'money': 'don',
    'please': 'jebal',
    'name': 'ileum',
    'food': 'eumsig',
    'sorry': 'mianhaeyo',
    'love': 'salang',
    'what': 'mwo?',
    'thank you': 'gomabseubnida',
    'congratulations': 'chughahae'
}

def search_word():
    """
    Searches for the Korean translation of the entered English word and updates the result label.
    """
    word = word_entry.get().lower()
    translation = korean_dictionary.get(word)

    if translation:
        result_label.config(text=f"{word} : {translation}")
    else:
        result_label.config(text="Word not found, click the 'show the available words' button")

def show_words():
    """
    Displays the words available in the dictionary.
    """
    words_listbox.delete(0, tk.END)
    for word in korean_dictionary.keys():
        words_listbox.insert(tk.END, word)

# App begins
root = tk.Tk()
root.geometry("600x250")
root.title("Korean Dictionary")

word_entry = tk.Entry(root)
word_entry.pack()

search_button = tk.Button(root, text="Search", command=search_word)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

words_listbox = tk.Listbox(root)
words_listbox.pack()

show_words_button = tk.Button(root, text="Show the available words", command=show_words)
show_words_button.pack()

root.mainloop()