import datetime

# Data cuaca dari JSON
data_cuaca = [
    {
        "location": {
            "name": "Surabaya, Indonesia",
            "lat": "-7.243",
            "long": "112.741",
            "timezone": "8",
            "alert": "",
            "degreetype": "C",
            "imagerelativeurl": "http://blob.weather.microsoft.com/static/weather4/en-us/"
        },
        "current": {
            "temperature": "32",
            "skycode": "28",
            "skytext": "Mostly Cloudy",
            "date": "2024-04-18",
            "observationtime": "13:41:16",
            "observationpoint": "Surabaya, Indonesia",
            "feelslike": "39",
            "humidity": "68",
            "winddisplay": "16 km/h East",
            "day": "Thursday",
            "shortday": "Thu",
            "windspeed": "16 km/h",
            "imageUrl": "http://blob.weather.microsoft.com/static/weather4/en-us/law/28.gif"
        },
        "forecast": [
            {
                "low": "26",
                "high": "33",
                "skycodeday": "9",
                "skytextday": "Light Rain",
                "date": "2024-04-18",
                "day": "Thursday",
                "shortday": "Thu",
                "precip": "50"
            },
            {
                "low": "26",
                "high": "32",
                "skycodeday": "9",
                "skytextday": "Light Rain",
                "date": "2024-04-19",
                "day": "Friday",
                "shortday": "Fri",
                "precip": "46"
            },
            {
                "low": "27",
                "high": "33",
                "skycodeday": "9",
                "skytextday": "Light Rain",
                "date": "2024-04-20",
                "day": "Saturday",
                "shortday": "Sat",
                "precip": "37"
            },
            {
                "low": "26",
                "high": "32",
                "skycodeday": "11",
                "skytextday": "Rain Showers",
                "date": "2024-04-21",
                "day": "Sunday",
                "shortday": "Sun",
                "precip": "47"
            },
            {
                "low": "25",
                "high": "32",
                "skycodeday": "11",
                "skytextday": "Rain Showers",
                "date": "2024-04-22",
                "day": "Monday",
                "shortday": "Mon",
                "precip": "62"
            }
        ]
    }
]

def cek_matahari_terbenam(waktu_terbenam, waktu_terbit):
    waktu_sekarang = datetime.datetime.now()

    print("Waktu saat ini:", waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S"))
    print("Waktu matahari terbenam:", waktu_terbenam.strftime("%H:%M:%S"))
    print("Waktu matahari terbit:", waktu_terbit.strftime("%H:%M:%S"))
    
    return waktu_terbenam.time() > waktu_sekarang.time() < waktu_terbit.time()

def main():
    # Waktu matahari terbenam dan terbit (dapat disesuaikan)
    waktu_sekarang = datetime.datetime.now()
    waktu_terbenam = waktu_sekarang.replace(hour=18, minute=0, second=0)
    waktu_terbit = waktu_sekarang.replace(hour=6, minute=0, second=0)

    for cuaca in data_cuaca:
        # Ambil data cuaca saat ini
        current_weather = cuaca["current"]
        temperature = current_weather["temperature"]
        skytext = current_weather["skytext"]
        humidity = current_weather["humidity"]

        # Cetak informasi cuaca saat ini
        print(f"Cuaca saat ini di {cuaca['location']['name']}: {skytext}")
        print(f"Suhu: {temperature}°C")
        print(f"Kelembaban: {humidity}%")

        # Cek apakah matahari telah terbenam atau belum terbit
        if cek_matahari_terbenam(waktu_terbenam, waktu_terbit):
            print("Matahari sudah terbenam dan belum terbit, nyalakan lampu taman!!")
        else:
            print("Matahari sudah terbit, matikan lampu taman")

        # Cek apakah cuaca mendung
        if "Cloudy" in skytext:
            print("Cuaca mendung, nyalakan lampu!")
        
        print()  # Tambahkan baris kosong untuk memisahkan data cuaca berbeda

if __name__ == "__main__":
    main()
