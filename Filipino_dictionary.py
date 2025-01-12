from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("800x400")

window.title("Filipino Dictionary.")

entry = Entry(window)
entry.pack()

result = StringVar()
result_label = Label(window, textvariable=result)

filipino_dictionary = {'go': 'pumunta ka',
                       'have': 'mayroon',
                       'she': 'siya',
                       'know': 'alam',
                       'well': 'mabuti',
                       'we': 'tayo',
                       'but': 'ngnuit',
                       'can': 'pwede',
                       'want': 'gusto',
                       'say': 'sabihin',
                       'with': 'kasama',
                       'black': 'itim',
                       'blue': 'asul',
                       'small': 'maliit',
                       'give': 'magbigay',
                       'arrive': 'dumating',
                       'never': 'kailanman',
                       'water': 'tubig',
                       'blood': 'dugo',
                       'full': 'puno na',
                       'month': 'buwan',
                       'against': 'iaban sa',
                       'under': 'sa ilalim',
                       'during': 'habang',
                       'better': 'mas mabuti',
                       'whore': 'ang',
                       'write': 'magsulat',
                       'upset': 'nagagalit',
                       'stay': 'manatili',
                       'serve': 'maglingkod',
                       'some': 'ilang',
                       'gate': 'labasan',
                       'today': 'ngayon',
                       'history': 'kasaysayn',
                       'drink': 'inumin',
                       'white': 'puti',
                       'speak': 'magsalita',
                       'thank you': 'salamat po',
                       'good morning': 'magandang umaga',
                       'meet': 'makipagkita',
                       'land': 'lupa', }

def search_word(word):
    if word in filipino_dictionary:
        result.set(filipino_dictionary[word])
        print(filipino_dictionary[word])

    else:
        result.set("Not found")
        print("not found")

        search_btn.pack()
        window.mainloop()

