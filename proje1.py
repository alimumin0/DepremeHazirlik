print("***Hoşgeldiniz***")
kullaniciAdmin = ["admin"]
sifreAdmin = ["12345"]

while True:
    menuSecim = int(input("""Devam etmek için rakamları tuşlayınız

    Sisteme giriş yapmak için 1'e
    Sisteme üye olmak için 2'ye
    Şifre değişikliği için 3'e  basınız.\n"""))



    if (menuSecim == 1):
        while(True):
            kullaniciAdi = input("Kullanici Adinizi girininiz.\n")
            sifre = (input("Şifrenizi giriniz.\n"))
            if ((kullaniciAdi == kullaniciAdmin[0] and sifre == sifreAdmin[0]) or (kullaniciAdi == kullanici[0] and sifre == sifreKullanici[0])):
                break
            elif ((kullaniciAdi == kullaniciAdmin[0] and sifre != sifreAdmin[0]) or (kullaniciAdi == kullanici[0] and sifre != sifreKullanici[0])):
                print("şifreniz yanlış")
                continue
            elif ((kullaniciAdi != kullaniciAdmin[0] and sifre == sifreAdmin[0]) or (kullaniciAdi != kullanici[0] and sifre == sifreKullanici[0])):
                print("Kullanıcı adınız yanlış")
                continue
            else:
                print("Kullanıcı adı ve şifre hatalı")
                continue
        print("Başarıyla giriş yaptınız.")
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
        kullanici = [kullaniciAdiKayit]
        sifreKullanici = [sifre1]
        continue          
    elif(menuSecim ==3):
        check = input("Şifre değiştirmek için kullanıcı adınızı girin.\n")
        if(kullanici[0] == check):
            while True:
                resetSifre1 = input("Yeni şifrenizi girin.\n")
                resetSifre2 = input("Yeni şifrenizi tekrar girin.\n")
                if(resetSifre1 == resetSifre2):
                    break
                else:
                    print("Şifreler uyuşmuyor lütfen tekrar deneyin.")
                    continue
            sifreKullanici[0] = resetSifre1
            print("Şifreniz Başarıyla Değiştirildi.\n\n")
            continue
    else:
        print("Yanlış değer girdiniz tekrar deneyin.\n\n")
        continue              