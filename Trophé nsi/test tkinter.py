from tkinter import *

fenetre = Tk()
fenetre.title("Test zbi")
fenetre.config(bg = "#000000")
fenetre.maxsize(1200,600)
fenetre.minsize(600,400)
decorp = PhotoImage(file="D-Corp-28-03-2023.png")
label2 = Label(fenetre, image= decorp,width="575", height="130")
label2.pack(pady = 50)
cadre1 = Frame(fenetre) 
cadre1.pack()
capcha= Button(cadre1, text="Générer un capcha", fg="red", background = "#000000", height = "4", width = "30")
capcha.pack()
FaceID= Button(cadre1, text="Tester la FaceID", fg="red", background = "#000000", height = "4", width = "30")
FaceID.pack()
fenetre.mainloop()




