from antares_http import antares
from time import sleep

ANTARES_KEY = 'e75aca9711895ddc:9d6d5c89265bee66' #Key yang di Profile

space = 100
print("Nama kamu siapa? :")
nama = input()
print("Jarak kamu sama aku berapa meter ya? :")
jarak = input()
jarak = int(jarak)

non_organic = 30
organic = 20

while 1:
    if jarak > 1:
        print("TRASHSCAN CLOSE!")
        jarak = jarak - 1
        sleep(1)
        continue
    elif jarak == 1 and space > 0:
        print("TRASHSCAN OPEN!")
        print("Seberapa besar Volume Sampah kamu? (MAX=100)")
        volume = input()
        volume = int(volume)
        if space - volume > 0:
            print("Ini ada daftar jenis sampah ")
            print("1. Kaca")
            print("2. Plastik")
            print("3. Nasi")
            print("4. Tumbuhan")
            print("5. Kaleng")
            print("6. Kertas")
            print("7. Karet")
            print("8. Daging")

            print("Jenis sampah kamu apa yaa? (1/2/3) ")
            jenis_sampah = input()
            jenis_sampah = int(jenis_sampah)
            
            #kategori organik atau non organik
            if jenis_sampah ==1:
                sampah = 'NON_ORGANIC'
                non_organic +=  volume
                break
            elif jenis_sampah ==2:
                sampah = 'NON_ORGANIC'
                non_organic +=  volume
                break
            elif jenis_sampah ==3:
                sampah = 'ORGANIC'
                organic +=  volume
                break
            elif jenis_sampah ==4:
                sampah = 'ORGANIC'
                organic +=  volume
                break
            elif jenis_sampah ==5:
                sampah = 'NON_ORGANIC'
                non_organic +=  volume
                break
            elif jenis_sampah ==6:
                sampah = 'NON_ORGANIC'
                non_organic +=  volume
                break
            elif jenis_sampah ==7:
                sampah = 'NON_ORGANIC'
                non_organic +=  volume
                break
            elif jenis_sampah ==8:
                sampah = 'ORGANIC'
                organic +=  volume
                break
            else:
                sampah = 'Sampah tidak berkategori silahkan pilih sesuai jenis sampah'
                break

        elif space > 0:
            print("Aduh Volume sampah kamu bikin TRASHSCAN penuh nih ")
            print("TRASHSCAN kasih tau petugas dulu yah.. ")

        else:
            print("Aduh TRASHSCAN udah penuh nih coba cari kotak yg lain yaa.. ")
            break
    else:
        print("Aduh TRASHSCAN udah penuh nih coba cari kotak yg lain yaa.. ")
        break
print("Kamu buang sampah dengan kategori "+sampah)
print("TRASHSCAN Volume ORGANIC: ",organic,"% dan NON_ORGANIC :",non_organic,"%")
print("Terima kasih yaa..")

def sensor_send():
    while 1:
        dataKapasitif = {
        'ORGANIC' : 32,
        'NON_ORGANIC' : 50,
        }
        dataUltrasonic = {
        'VOLUME_ORGANIC' : '20%',
        'VOLUME_NON_ORGANIC' : '20%',
        }
        antares.setAccessKey(ANTARES_KEY)
        antares.send(dataKapasitif, 'TRASHSCAN', 'SensorProximityKapasitif')
        print("==== SEND DATA ====")
        print(" Sensor ProximityKapasitif", dataKapasitif)
        print(" Sensor Ultrasonic", dataUltrasonic)
        print("===================")
        sleep(10)
    

