
from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("900x550")
window.title("Multi-lingual_Dictionary")
window.configure(bg="black")

word_entry = Entry(window, width=30, font=("Times New Roman ", 12))
word_entry.configure(bg="white")
word_entry.pack()

word_result = StringVar()
word_result_label = Label(window,textvariable=word_result)
word_result_label.pack()

#MORKAH GRACE
filipino_dictionary = {'go':'pumunta ka',
                     'have':'mayroon',
                     'she':'siya',
                     'know':'alam',                    
                     'well':'mabuti',
                     'we':'tayo',
                     'but':'ngnuit',
                     'can':'pwede',
                     'want':'gusto',
                     'say':'sabihin',
                     'with':'kasama',
                     'black':'itim',
                     'blue':'asul',
                     'small':'maliit',
                     'give':'magbigay',
                     'arrive':'dumating',
                     'never':'kailanman',
                     'water':'tubig',
                     'blood':'dugo',
                     'full':'puno na',
                     'month':'buwan',
                     'against':'iaban sa',
                     'under':'sa ilalim',
                     'during':'habang',
                     'better':'mas mabuti',
                     'whore':'ang',
                     'write':'magsulat',
                     'upset':'nagagalit',
                     'stay':'manatili',
                     'serve':'maglingkod',
                     'some':'ilang',
                     'gate':'labasan',
                     'today':'ngayon',
                     'history':'kasaysayn',
                     'drink':'inumin',
                     'white':'puti',
                     'speak':'magsalita',
                     'thank you':'salamat po',
                     'good morning':'magandang umaga',
                     'meet':'makipagkita',
                      'land':'lupa'}
#OKEREKE FAVOUR

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
                     'please': 's\'il vous plaît',
                     'thank you': 'merci'}

#AWUHE TREASURE 
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
    "great":"sababa"}

#AJUFOH DASHA
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
                       'vegetable': 'Yasai'}

#OKECHUKWU ANGEL
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
    'congratulations': 'chughahae'}


def search_filipino_word(word):
    if word in filipino_dictionary:
        word_result.set("Not found")
        word_result.set(filipino_dictionary[word])
        print(filipino_dictionary[word])

    else:
        print("Not Found.")


def search_french_word(word):
    if word in french_dictionary:
        word_result.set("Not found")
        word_result.set(french_dictionary[word])
        print(french_dictionary[word])

    else:
        print("Not Found.")


def search_hebrew_word(word):
    if word in hebrew_dictionary:
        word_result.set("Not found")
        word_result.set(hebrew_dictionary[word])
        print(hebrew_dictionary[word])

    else:
        print("Not Found.")


def search_japanese_word(word):
    if word in japanese_dictionary:
        word_result.set("Not found")
        word_result.set(japanese_dictionary[word])
        print(japanese_dictionary[word])

    else:
        print("Not Found.")

def search_korean_word(word):
    if word in korean_dictionary:
        word_result.set("Not found")
        word_result.set(korean_dictionary[word])
        print(korean_dictionary[word])

    else:
        print("Not Found.")



filipino_search = Button(window, text='Filipino',width="20", command=lambda:search_filipino_word(word_entry.get()))
filipino_search.configure(bg="purple")
filipino_search.pack()

french_search = Button(window, text='French',width="20", command=lambda:search_french_word(word_entry.get()))
french_search.configure(bg="purple")
french_search.pack()

hebrew_search = Button(window, text='Hebrew',width="20", command=lambda:search_hebrew_word(word_entry.get()))
hebrew_search.configure(bg="purple")
hebrew_search.pack()

japanese_search = Button(window, text='Japanese',width="20", command=lambda:search_japanese_word(word_entry.get()))
japanese_search.configure(bg="purple")
japanese_search.pack()

korean_search = Button(window, text='Korean',width="20", command=lambda:search_korean_word(word_entry.get()))
korean_search.configure(bg="purple")
korean_search.pack()

window.mainloop()


