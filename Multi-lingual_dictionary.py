
from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("900x550")
window.title("Multi-lingual_Dictionary")
window.configure(bg="black")


word_entry = Entry(window, width=30, font=("", 12))
word_entry.configure(bg="white")
word_entry.pack()

word_result = StringVar()
word_result_label = Label(window,textvariable=word_result)
word_result_label.pack()


japanese_dictionary = {'you': 'Anata' ,
                       'thank you': 'Arigato' ,
                       'okay': 'Daijoubu' ,
                       'please': 'Douzo' ,
                       'sorry': 'Gomennasai' ,
                       'rice': 'Gohan' ,
                       'yes': 'Hai' ,
                       'no': 'Lie' ,
                       'receive': 'Itadakimasu' ,
                       'good evening': 'Konbanwa' ,
                       'hello': 'Konnichiwa' ,
                       'this': 'kore' ,
                       'coffe': 'Koohii' ,
                       'fruit': 'Kudamono' ,
                       'water': 'Mizu' ,
                       'name': 'Namae' ,
                       'meat': 'Niku' ,
                       'tea': 'Ocha' ,
                       'good morning': 'Ohayou.' ,
                       'delicious': 'Oishii' ,
                       'rice ball': 'Onigiri' ,
                       'good night': 'Oyasumi' ,
                       'bread': 'Pan' ,
                       'fish': 'Fish' ,
                       'excuse me': 'Sumimasen' ,
                       'egg': 'Tamago' ,
                       'I': 'Watashi' ,
                       'me': 'Watashi' ,
                       'vegetable': 'Yasai' ,
                       }


hebrew_dictionary={
    "hello":"shalom",
    "book":"sefer",
    "food":"ochel",
    "water":"mayim",
    "chair":"khise",
    "yes":"ken",
    "no":"lo",
    "thank you": "toda",
    "please":"bevakasha",
    "sorry":"slicha",
    "house": "bayit",
    "friend":"chaver",
    "day":"yom",
    "night":"laila",
    "money":"kesef",
    "heart":"lev",
    "good":"tov",
    "bad":"ra",
    "beautiful":"yav",
    "head": "rosh",
    "love":"ahavah",
    "big":"gadol",
    "small":"katan",
    "world":"olam",
    "fire":"esh",
    "sea":"yam",
    "light":"ohr",
    "table":"shulchan",
    "clothes":"begadim",
    "great":"sababa"
}

french_dictionary = {'good morning': 'bonne matinée',
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
                     'please': 'sil vous plaît',
                     'thank you': 'merci'}



def search_japanese_word(word):
    if word in japanese_dictionary:
        word_result.set("Not found")
        word_result.set(japanese_dictionary[word])
        print(japanese_dictionary[word])

    else:
        print("Not Found.")


def search_hebrew_word(word):
    if word in hebrew_dictionary:
        word_result.set("Not found")
        word_result.set(hebrew_dictionary[word])
        print(hebrew_dictionary[word])

    else:
        print("Not Found.")

def search_french_word(word):
    if word in french_dictionary:
        word_result.set("Not found")
        word_result.set(french_dictionary[word])
        print(french_dictionary[word])

    else:
        print("Not Found.")


french_search = Button(window, text='French',width="20", command=lambda:search_french_word(word_entry.get()))
french_search.configure(bg="purple")

french_search.pack()


hebrew_search = Button(window, text='Hebrew',width="20", command=lambda:search_hebrew_word(word_entry.get()))
hebrew_search.configure(bg="purple")
hebrew_search.pack()



japanese_search = Button(window, text='Japanese',width="20", command=lambda:search_japanese_word(word_entry.get()))
japanese_search.configure(bg="purple")
japanese_search.pack()
window.mainloop()


