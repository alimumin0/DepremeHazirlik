import pandas as pd
data = pd.DataFrame(pd.read_csv("database.csv"))
import sqlite3
vt = sqlite3.connect("userdata.db")
vtc = vt.cursor()
def tablo_olustur():
    vtc.execute("""CREATE TABLE IF NOT EXISTS kullanicilar (kullaniciadi TEXT, sifre TEXT) """)
def kullanici_ekle(e_kullanici,e_sifre):
    vtc.execute("""INSERT INTO kullanicilar VALUES (?,?)""",(e_kullanici,e_sifre))
    vt.commit()
def kullanici_al(a_kullanici,a_sifre):
    vtc.execute("""SELECT * FROM kullanicilar WHERE kullaniciadi = ? AND sifre= ? """,(a_kullanici,a_sifre))
    vt.commit()
def sifre_degis(d_sifre,d_kullanici):
    vtc.execute("""UPDATE kullanicilar SET sifre = ? WHERE kullaniciadi = ? """,(d_sifre,d_kullanici))
    vt.commit()
vt.commit()

tablo_olustur()
print("----***Hoşgeldiniz***----")
mobilOneri = ["AFAD ACİL AFAD Acil mobil uygulaması, tek tuşla acil çağrıyapabiliyor.", "DÜDÜĞÜM Enkaz veya acil durumlarda düdük sesi çıkartarak konumunuzun belirlenmesine yardımcı olur." ,"112 ACİL YARDIM BUTONU acil müdahale gerektiren birolayda acil servisi haberdar edebilir ve uygulamanın göndereceği konum bilgisiyle,size en kısa sürede ulaşılmasını sağlayabilirsiniz"]

while True:
    menuSecim = int(input("""Devam etmek için rakamları tuşlayınız

    Sisteme giriş yapmak için 1'e
    Sisteme üye olmak için 2'ye
    Şifre değişikliği için 3'e  basınız.\n"""))

    if (menuSecim == 1): 
        while(True):
            kullaniciAdi = input("Kullanici Adinizi girininiz.\n")
            sifre = (input("Şifrenizi giriniz.\n"))
            kullanici_al(kullaniciAdi,sifre)
            kullanicidata = vtc.fetchall()
            if kullanicidata:
                break
            else:
                print("Hatalı kullanici adi veya sifre girişi yaptınız.")
        print("Başarıyla giriş yaptınız.\n\n\n")
        if (kullaniciAdi == "admin" and sifre == "12345"):
            print("Hoşgeldin admin")
            while True:
                adminMenu = int(input("""Devam etmek için rakamları tuşlayınız

    Kullanıcıları görüntülemek için 1'e
    Kullanıcı5 silmek için 2'ye
    Çıkış yapmak için 3'e  basınız.\n"""))
                if(adminMenu == 1):
                    vtc.execute("SELECT * FROM kullanicilar")
                    vt.commit()
                    kullanici_list = vtc.fetchall()
                    print("\n")
                    for i in kullanici_list:
                        print(i)
                elif(adminMenu == 2):
                    silinecek_kullanici = input("Silinecek olan kullanıcıyı yazınız.\n")
                    vtc.execute("DELETE FROM kullanicilar WHERE kullaniciadi = ?",(silinecek_kullanici,))
                    vt.commit()            
                elif(adminMenu == 3):
                    break
                else:
                    continue
        print("Aşamalar Sırasıyla gelicektir.\n\n\n\n\n\n\n")
        for i in range(len(data)):
            while (True):
                print("{}. adım {}\n".format(i+1,data.loc[i,"Maddeler"]))
                asamaKontol = input("Bu aşamayı tamamladıysanız devam yazınız.\n")
                if(asamaKontol == "devam"):
                    break
                else:
                    continue  
        print("Tebrikler! Bütün aşamaları tamamladınız.\n\n\n")
        print("”Deprem öncesinde evinizdeki önlemleri aldınız. Geriye akıllı telefonlarınızda bulunması gereken uygulamalar kaldı.\n")
        for i in range(len(mobilOneri)):
            print(mobilOneri[i])     
        break

    elif(menuSecim == 2):
        while True:
            kullaniciAdiKayit = input("Kullanici adınızı giriniz.\n")
            sifre1 = input("Şifrenizi giriniz.\n")
            sifre2 = input("Şifrenizi tekrar giriniz.\n") 
            if(sifre1 != sifre2):
                print("Girdiğiniz şifreler uyuşmuyor. Lütfen tekrar deneyin")
                continue
            else:
                break
        print("Başarıyla kayıt oldunuz.\n\n")
        kullanici_ekle(kullaniciAdiKayit,sifre1)
        continue          
    
    elif(menuSecim ==3):
        check = input("Şifre değiştirmek için kullanıcı adınızı girin.\n")
        while True:
            resetSifre1 = input("Yeni şifrenizi girin.\n")
            resetSifre2 = input("Yeni şifrenizi tekrar girin.\n")
            if(resetSifre1 == resetSifre2):
                break
            else:
                print("Şifreler uyuşmuyor lütfen tekrar deneyin.")
                continue
        sifre_degis(resetSifre1,check)
        print("Şifreniz Başarıyla Değiştirildi.\n\n")
        continue
    else:
        print("Yanlış değer girdiniz tekrar deneyin.\n\n")
        continue              
vt.close()