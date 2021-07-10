import tkinter as tk
from tkinter import messagebox
import string
import random

#Özellikler giriş

guess = [0]

def generator():
    guess[0]=random.randint(0,10)

generator()

skor = [0]

def islem():
    oyuncu = int(giris1.get())
    if oyuncu == guess[0]:
        messagebox.showinfo("Tebrikler!", "Siz kazandınız!\nYeni sayı oluşturuldu")
        giris1.delete(0, 'end')
        generator()
        skor[0]=skor[0]+1
        puan.config(text=skor[0])
    else:
        messagebox.showerror("Kaybettin!", "Tekrar dene!")
        giris1.delete(0, 'end')
#Özellikler bitiş

pencere = tk.Tk()
pencere.geometry("200x100")
pencere.title("Sayi Bulmaca")

yazi1 = tk.Label(text="Rakam girin:")

giris1 = tk.Entry()

buton1 = tk.Button(text="Tahmin", command=islem)

yazi2 = tk.Label(text="Skorunuz:")

puan = tk.Label()

yazi1.pack()
giris1.pack()
buton1.pack()
yazi2.pack()
puan.pack()
pencere.mainloop()