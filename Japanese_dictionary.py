from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("800x400")

window.title("Japanese Dictionary.")




entry= Entry(window)
entry.pack()


result = StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()



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










def search_word(word):
    if word in japanese_dictionary:
        result.set("Not found")
        result.set(japanese_dictionary[word])
        print(japanese_dictionary[word])

    else:
        print("Not Found.")




search_btn = Button(window, text='Search', command=lambda:search_word(entry.get()))
search_btn.pack()
window.mainloop()








