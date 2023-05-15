print("***Hoşgeldiniz***")
kullaniciAdmin = ["admin"]
sifreAdmin = ["12345"]
asamaList = ['Dolap üzerlerinde yer alan malzemelerin, kayıp düşmesini engellemek adına plastik tutucu malzemeler ve/veya yapıştırıcı kullanınız.',
             'Kullandığınız ısıtıcılar mutlaka yere veya duvara sabitleyiniz.',
             'Devrilebilecek ağır eşyalar ve dolaplar mutlaka birbirine ve duvara sabitleyiniz.',
             'İçlerinde ağır eşyalar barındıran dolapların kapakları, mekanik kilitler yardımı ile güvenli hale getiriniz.',
             'Zehirli, patlayıcı, yanıcı maddeler düşmeyecek bir konumda sabitlenmeli ve kırılmayacak bir şekilde depolanmalıdır. Bu maddelerin üzerlerine fosforlu, belirleyici etiketler koyunuz.']
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
        if (kullaniciAdi == kullaniciAdmin[0] and sifre == sifreAdmin[0]):
            print("Hoşgeldin admin")
            while True:
                adminMenu = int(input("""Devam etmek için rakamları tuşlayınız

    Yeni aşama girişi yapmak için 1'e
    Varolan aşamayı değiştirmek için 2'ye
    Çıkış yapmak için 3'e  basınız.\n"""))
                if(adminMenu == 1):
                    yeniAsama = input("Yeni aşamayı giriniz.\n")
                    asamaList += [yeniAsama]
                    print(asamaList)
                elif(adminMenu == 2):
                    degisecekAsama = input("Değişecek olan aşamayı yazınız.\n")
                    degisecekIndex = asamaList.index(degisecekAsama)
                    yeniAsama = input("Yeni aşamayı giriniz.\n")
                    asamaList.insert(degisecekIndex,yeniAsama)
                    print(asamaList)                
                elif(adminMenu == 3):
                    break
                
                else:
                    continue
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
    