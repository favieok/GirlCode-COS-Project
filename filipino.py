from tkinter import Tk, Entry, Button, Label, StringVar




window = Tk()
window.geometry("800x400")

window.title("Filipino Dictionary.") 




entry= Entry(window)
entry.pack()


result = StringVar()
result_label=Label(window,textvariable=result)



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
    if word in filipino_dictionary:
        result.set(filipino_dictionary[word])
        print(filipino_dictionary[word])
        
    else:
        result.set("Not found")
        print("not found")
        
        
        
        
        search_btn = Button(window, text='search', command=lambda:search_word(entry()))
        search_btn.pack()
        window. mainloop()
        
                
