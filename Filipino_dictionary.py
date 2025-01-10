from tkinter import Tk,Entry,Button,Label,StringVar

window = Tk()
window.geometry("600x250")
window.title("Filipino_Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()


filipino_dictionary ={'other':'ibang',
                       'said':'sinabi',
                       'three':'tatlong',
                      'deos':'gumagana',
                      'tell':'sibihin',
                      'home':'tahanan',
                      'read':'basahin',
                      'hand':'kamay',
                      'put':'ilagay',
                      'large':'malaki',
                      'small':'maliit',
                      'play':'maglaro',
                      'air':'naka',
                      'want':'gusto',
                      'will':'pamanahan',
                      'each':'bawat',
                      'which':'kung saan',
                      'how':'kung paano',
                      'do':'gawin',
                      'also':'ring',
                      'why':'bakit',
                      'land':'lupa',
                      'must':'kailangan',
                      'kind':'uri',
                      'light':'liwanag',
                      'house':'bahay',
                      'again':'muli',
                      'mother':'nanay',
                      'new':'bago',
                      'part':'bahagi',
                      'place':'lugar',
                      'made':'ginawa',
                      'take':'kumuha',
                      'father':'ama',
                      'change':'pagbabago',
                      'went':'nagpunta',
                      'animal':'hayop',
                      'live':'mabuhay',
                      'back':'likod',
                      'year':'taon',
                      'very':'napaka',
              }

def search(word):
    if word in filipino_dictionary:
        result.set(filipino_dictionary[word])
        print(filipino_dictionary[word])
    else:
        result.set("Not found")
        print("Not found")


search_btn = Button(window, text='Search' , command=lambda:search(entry_text.get()))
search_btn.pack()
window.mainloop()























