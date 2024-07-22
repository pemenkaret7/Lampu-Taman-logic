def main():
    # Input status cuaca, matahari, dan gerimis dari pengguna
    cuaca = input("Apakah cuaca saat ini mendung? (ya/tidak): ").lower()
    matahari = input("Apakah matahari sudah terbenam? (ya/tidak): ").lower()

    gerimis = input("Apakah saat ini sedang gerimis? (ya/tidak): ").lower()

    # Cek apakah cuaca mendung atau matahari telah terbenam atau sedang gerimis
    if cuaca == "ya" or matahari == "ya" or (matahari == "tidak" and cuaca == "tidak" and gerimis == "ya"):
        print("Lampu dinyalakan.")
    else:
        print("Lampu dimatikan.")

if __name__ == "__main__":
    main()
