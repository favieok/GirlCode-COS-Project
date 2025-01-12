import tkinter as tk
from tkinter import ttk

# korean dicitionary (English to Korean)
korean_dictionary = {
    'hello' : 'annyeong',
    'come' : 'oda',
    'go' : 'gada',
    'stay' : 'meomuleuda',
    'here' : 'yeogi',
    'near' : 'gakkaun',
    'far' : 'moelli',
    'happy' : 'haengboghada',
    'sad' : 'saelpeun',
    'hungry' : 'baegopeun',
    'filled' : 'chaeuneun',
    'money' : 'don',
    'food' ; 'eumsig',
    'sorry' : 'mianhaeyo',
    'love' : 'salang',
    'what' : 'mwo?',
    'please' : 'jebal',
    'thank you' : 'gomabseubnida',
    'congratulations' : 'chughahae'
    }

def search_word () :
    """"""
    searches for the korean trranslation of the entered English word and updates the result label.
    """"""
    word = word_entry.get().lower()
    translation = korean_dictionary.get(word)

    if translation:
        result_label.config(text=f"{word} : {translation}")
    Else:
    result_label.config9text='word not `found, click the 'show the available words'button")

Def show_words () :
     """"""
     displays the words available in the dicitionary. 
     """""""
    words_listbox.delete(0, tk,END)
    for words in korean_dictionary.keys () :
       words_listbox.insert(tk,END,word)

# Apps begins
root = tk.TK()
root.geometry("600*250")
root.title("Korean Dictionary")

word_entry = tk.Entry(root)
word_entry.pack()

search_button = tk.Button(root, text = "search", command = search_word)
search_button.pack()
