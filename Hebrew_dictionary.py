from tkinter import Tk,Entry,Button,Label,StringVar

window=Tk()
window.geometry("400x150")
window.title("Hebrew Dictionary")
entry_text= Entry(window)
entry_text.pack()

result=StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()

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

def search(word):
    if word in hebrew_dictionary:
        result.set(hebrew_dictionary[word])
        print(hebrew_dictionary[word])

    else:
        result.set("Not found")
        print("Not found")


search_btn=Button(window,text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()
window.mainloop()