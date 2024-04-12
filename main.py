import datetime

def cek_matahari_terbenam(waktu_terbenam, waktu_terbit):
    #waktu saat ini dalam zona waktu lokal pake modul datetime now
    waktu_sekarang = datetime.datetime.now()

    #merubah format modul jadi string lalu dicetak ke output
    print("Waktu saat ini:", waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S"))
    print("Waktu matahari terbenam:", waktu_terbenam.strftime("%H:%M:%S"))
    print("Waktu matahari terbit:", waktu_terbit.strftime("%H:%M:%S"))
    
    #membandingkan untuk hasil nilai true ato false
    return waktu_terbenam.time() > waktu_sekarang.time() < waktu_terbit.time()


def main():
    #waktu matahari terbenam dan terbit (bisadiubah sesuai kebutuhan)
    waktu_sekarang = datetime.datetime.now()
    waktu_terbenam = waktu_sekarang.replace(hour=18, minute=0, second=0)
    waktu_terbit = waktu_sekarang.replace(hour=6, minute=0, second=0)

    if cek_matahari_terbenam(waktu_terbenam, waktu_terbit):
        print("matahari sudah terbenam dan belum terbit, nyalakan lampu taman!!")    
    else:
        print("matahari sudah terbit, matikan lampu taman")


main()
