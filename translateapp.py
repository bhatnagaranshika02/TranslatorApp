import tkinter as tk
root = tk.Tk()
canvas1 = tk.Canvas(root,width=400,height=300,relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Translate you sentence')
label1.config(font=('helvetica', 20))
canvas1.create_window(200, 25, window=label1)


label2 = tk.Label(root, text='Enter your sentence:')
label2.config(font=('helvetica', 11))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def translateToHindi():
    sent = entry1.get()
    from translate import Translator
    translator = Translator(to_lang="Hindi")
    translation = translator.translate(sent)


    label3 = tk.Label(root, text= 'The translation is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text= translation,font=('helvetica', 15, 'bold'))
    canvas1.create_window(200, 230, window=label4)

button1 = tk.Button(text='Translate', command=translateToHindi, bg='brown', fg='white', font=('helvetica', 11, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
