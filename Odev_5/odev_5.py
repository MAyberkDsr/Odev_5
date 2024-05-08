import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import filedialog

def giris():
    kullaniciAdi = kullaniciAdiGiris.get()
    sifre = sifreGiris.get()
    imlec.execute("SELECT * FROM kullanicilar WHERE kullaniciAdi=? AND sifre=?", (kullaniciAdi, sifre))
    if imlec.fetchall():
        messagebox.showinfo("Başarılı", "Giriş başarılı!") # Bilgi verildi
        menuAc()
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!") # Hata verildi

def kayitOl():
    kullaniciAdi = kullaniciAdiGiris.get()
    sifre = sifreGiris.get()
    imlec.execute("SELECT * FROM kullanicilar WHERE kullaniciAdi=? AND sifre=?", (kullaniciAdi,sifre))
    if imlec.fetchall():
        messagebox.showerror("Hata", "Bu kullanıcı zaten var!")
    else:
        imlec.execute("INSERT INTO kullanicilar (kullaniciAdi, sifre) VALUES (?, ?)", (kullaniciAdi, sifre))
        baglanti.commit()
        messagebox.showinfo("Başarılı", "Kayıt başarılı!")

def menuAc():
    anaPencere.destroy()
    menuPencere = tk.Tk() 
    menuPencere.geometry("400x250") 
    menuPencere.title("Metin Benzerliği Kıyaslama Uygulaması")
    menuCubugu = tk.Menu(menuPencere) # Menü çubuğu oluşturuldu
    menuPencere.config(menu=menuCubugu)
    karsilastir = tk.Menu(menuCubugu)
    islemler = tk.Menu(menuCubugu)
    cikis = tk.Menu(menuCubugu)
    menuCubugu.add_cascade(label="Karşılaştır",menu=karsilastir)
    menuCubugu.add_cascade(label="İşlemler",menu=islemler)
    menuCubugu.add_command(label="Çıkış",command=cikisYap)
    sifre = tk.Menu(islemler)
    islemler.add_cascade(label="Şifre",menu=sifre)
    degistir = tk.Menu(sifre)
    sifre.add_cascade(label="Değiştir",command=guncelleAc)
    jaccard = tk.Menu(karsilastir)
    karsilastir.add_cascade(label="Jaccard",command=jaccardAc)
    sorensenDice = tk.Menu(karsilastir)
    karsilastir.add_cascade(label="Sorensen Dice",command=sorensenDiceAc)
    
    menuPencere.mainloop()

def cikisYap():
    anaPencere.quit()
    
def jaccardAc():
    def dosyaAc():
        dosya1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        dosya2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        dosya1Giris.insert(0,dosya1)
        dosya2Giris.insert(0,dosya2)

    def jaccard():
        with open(dosya1Giris.get(), 'r') as file:
            metin1 = file.read()
        with open(dosya2Giris.get(), 'r') as file:
            metin2 = file.read()
        küme1 = set(metin1)
        küme2 = set(metin2)

        kesisim = len(küme1.intersection(küme2))
        birlesim = len(küme1.union(küme2))

        benzerlikKatsayisi1 = kesisim / birlesim

        sonuc.config(text=benzerlikKatsayisi1)

    jaccardPencere = tk.Tk()
    jaccardPencere.geometry("400x250") 
    jaccardPencere.title("Metin Benzerliği Kıyaslama Uygulaması")
    dosya1Etiket = tk.Label(jaccardPencere,text="Dosya Adı") 
    dosya1Etiket.pack()
    dosya1Giris = tk.Entry(jaccardPencere) 
    dosya1Giris.pack()
    dosya2Etiket = tk.Label(jaccardPencere,text="Dosya Adı") 
    dosya2Etiket.pack()
    dosya2Giris = tk.Entry(jaccardPencere) 
    dosya2Giris.pack()
    dosyaSecButon = tk.Button(jaccardPencere,text="Dosya Seç",command=dosyaAc) 
    dosyaSecButon.pack()
    karsilastirButon = tk.Button(jaccardPencere,text="Karşılaştır",command=jaccard) 
    karsilastirButon.pack()
    sonuc = tk.Label(jaccardPencere,text="")
    sonuc.pack()

    jaccardPencere.mainloop()

def sorensenDiceAc():
    def dosyaAc():
        dosya1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        dosya2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        dosya1Giris.insert(0,dosya1)
        dosya2Giris.insert(0,dosya2)

    def sorensenDice():
        with open(dosya1Giris.get(), 'r') as file:
            metin1 = file.read()
        with open(dosya2Giris.get(), 'r') as file:
            metin2 = file.read()
        metin1 = set(metin1)
        metin2 = set(metin2)

        benzerlikKatsayisi2 = (2 * len(metin1.intersection(metin2))) / (len(metin1) + len(metin2))

        sonuc.config(text=benzerlikKatsayisi2)

    sorensenDicePencere = tk.Tk()
    sorensenDicePencere.geometry("400x250") 
    sorensenDicePencere.title("Metin Benzerliği Kıyaslama Uygulaması")
    dosya1Etiket = tk.Label(sorensenDicePencere,text="Dosya Adı") 
    dosya1Etiket.pack()
    dosya1Giris = tk.Entry(sorensenDicePencere) 
    dosya1Giris.pack()
    dosya2Etiket = tk.Label(sorensenDicePencere,text="Dosya Adı") 
    dosya2Etiket.pack()
    dosya2Giris = tk.Entry(sorensenDicePencere) 
    dosya2Giris.pack()
    dosyaSecButon = tk.Button(sorensenDicePencere,text="Dosya Seç",command=dosyaAc) 
    dosyaSecButon.pack()
    karsilastirButon = tk.Button(sorensenDicePencere,text="Karşılaştır",command=sorensenDice) 
    karsilastirButon.pack()
    sonuc = tk.Label(sorensenDicePencere,text="")
    sonuc.pack()

    sorensenDicePencere.mainloop()

    
def guncelleAc():
    def guncelle():
        yeniSifre = yeniSifreGiris.get()
        imlec.execute("UPDATE kullanicilar SET sifre = ?",(yeniSifre,))
        baglanti.commit()
        messagebox.showinfo("Başarılı", "Şifreniz güncellendi!")
        guncellePencere.destroy()

    guncellePencere = tk.Tk()
    guncellePencere.geometry("400x250")
    guncellePencere.title("Metin Benzerliği Kıyaslama Uygulaması")
    yeniSifreEtiket = tk.Label(guncellePencere,text="Yeni Şifre") 
    yeniSifreEtiket.pack() 
    yeniSifreGiris = tk.Entry(guncellePencere) 
    yeniSifreGiris.pack()
    guncelleButon = tk.Button(guncellePencere,text="Güncelle",command=guncelle)
    guncelleButon.pack()
    
    guncellePencere.mainloop()

baglanti = sqlite3.connect("kullanicilar.db") # Bağlantı sağlandı.
imlec = baglanti.cursor() # İmleç oluşturuldu.

imlec.execute('CREATE TABLE IF NOT EXISTS kullanicilar(kullaniciAdi TEXT , sifre TEXT)') # Tablo oluşturuldu.


anaPencere = tk.Tk() # Pencere oluşturuldu.
anaPencere.geometry("400x250") # Pencere boyutu
anaPencere.title("Metin Benzerliği Kıyaslama Uygulaması") # Pencerenin başlık metni

kullaniciAdiEtiket = tk.Label(anaPencere,text="Kullanıcı Adı") # Etiket eklendi
kullaniciAdiEtiket.pack() # Pencerede gösterildi
kullaniciAdiGiris = tk.Entry(anaPencere) # Giriş alanı eklendi
kullaniciAdiGiris.pack() 

sifreEtiket = tk.Label(anaPencere,text="Şifre") 
sifreEtiket.pack() 
sifreGiris = tk.Entry(anaPencere) 
sifreGiris.pack() 

girisButon = tk.Button(anaPencere,text="Giriş",command=giris) # Buton eklendi
girisButon.pack() 
kayitButon = tk.Button(anaPencere,text="Kayıt Ol",command=kayitOl)
kayitButon.pack()

anaPencere.mainloop()

