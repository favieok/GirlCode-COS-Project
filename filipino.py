from tkinter import Tk, Entry, Button, Label, StringVar




window = Tk()
window.geometry("800x400")

window.title("French Dictionary.") 




entry= Entry(window)
entry.pack()


result = StringVar()
result_label=Label(window,textvariable=result)



french_dictionary = {'aller':'go',
                     'avoir':'have',
                     'elle':'she',
                     'saviour':'know',                    
                     'bien':'well',
                     'nous':'we',
                     'mais':'but',
                     'pauvoir':'can',
                     'voulair':'want',
                     'dire':'say',
                     'avec':'with',
                     'noir':'black',
                     'bleu':'blue',
                     'petit':'small',
                     'donner':'give',
                     'arriver':'arrive',
                     'jamais':'never',
                     'eau':'water',
                     'sang':'blood',
                     'plein':'full',
                     'mois':'month',
                     'contre':'against',
                     'sous':'under',
                     'pendant':'during',
                     'meilleur':'better',
                     'putain':'whore',
                     'ecrire':'write',
                     'desoler':'upset',
                     'ville':'stay',
                     'servir':'serve',
                     'quelques':'some',
                     'porte':'gate',
                     'aujord`hui':'today',
                     'historie':'history',
                     'boire':'drink',
                     'blanc':'white',
                     'parle':'speak',
                     'merci':'thank you',
                     'bonjour':'good morning',
                     'retrouver':'meet',}

def search_word(word):
    if word in french_dictionary:
        result.set(french_dictionary[word])
        print(french_dictionary[word])
        
    else:
        result.set("Not found")
        print("not found")
        
        
        
        
        search_btn = Button(window, text='search', command=lambda:search_word(entry()))
        search_btn.pack()
        window. mainloop()
        
                