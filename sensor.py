from antares_http import antares
from time import sleep
import json
from datetime import date, datetime


ANTARES_KEY = 'e75aca9711895ddc:9d6d5c89265bee66' #Key yang di Profile

antares.setDebug(False)
antares.setAccessKey(ANTARES_KEY)

space1 = 100
space2 = 100

latestData = antares.get('TRASHSCAN', 'SensorUltrasonik')
x = json.dumps(latestData['content'])
x = json.loads(x)
non_organic = int(x['NON_ORGANIC'])
organic = int(x['ORGANIC'])

space1 = space1 - organic
space2 = space2 - non_organic

print("Nama kamu siapa? :")
nama = input()
print("Jarak kamu sama aku berapa meter ya? :")
jarak = input()
jarak = int(jarak)

while 1:
    if jarak > 1:
        print("TRASHSCAN CLOSE!")
        jarak = jarak - 1
        sleep(1)
        continue
    elif jarak == 1 and space1 > 0 and space2 > 0:
        print("TRASHSCAN OPEN!")
        print("TRASHSCAN Volume ORGANIC: ",organic,"% dan NON_ORGANIC :",non_organic,"%")
        # print("Ini ada daftar jenis sampah ")
        # print("1. Kaca")
        # print("2. Plastik")
        # print("3. Nasi")
        # print("4. Tumbuhan")
        # print("5. Kaleng")
        # print("6. Kertas")
        # print("7. Karet")
        # print("8. Daging")
        print("Jenis sampah kamu apa yaa? (1/2/3/4/5/6/7/8) ")
        jenis_sampah = input()
        jenis_sampah = int(jenis_sampah)
        print("Seberapa besar Volume Sampah kamu? (MAX=100)")
        volume = input()
        volume = int(volume)
        #kategori organik atau non organik
        if jenis_sampah ==1:
            sampah = 'NON_ORGANIC'
            jenis = 'Kaca'
            if space2 - volume >= 0:
                non_organic +=  volume
                status = 'success'
                print("Kamu berhasil buang sampah jenis "+jenis+" dengan kategori "+sampah)
                break
            elif space2 > 0:
                print("Maaf Volume sampah kamu bikin TRASHSCAN penuh nih ")
                print("coba cari kotak yg lain yaa..")
                status = 'failed'
                break
            else:
                print("Aduh TRASHSCAN udah penuh nih")
                print("TRASHSCAN kasih tau petugas dulu yah.. ")
                status = 'failed'
                break
        elif jenis_sampah ==2:
            sampah = 'NON_ORGANIC'
            jenis = 'Plastik'
            if space2 - volume >= 0:
                non_organic +=  volume
                status = 'success'
                print("Kamu berhasil buang sampah jenis "+jenis+" dengan kategori "+sampah)
                break
            elif space2 > 0:
                print("Maaf Volume sampah kamu bikin TRASHSCAN penuh nih ")
                print("coba cari kotak yg lain yaa..")
                status = 'failed'
                break
            else:
                print("Aduh TRASHSCAN udah penuh nih")
                print("TRASHSCAN kasih tau petugas dulu yah.. ")
                status = 'failed'
                break
        elif jenis_sampah ==3:
            sampah = 'ORGANIC'
            jenis = 'Nasi'
            if space1 - volume >= 0:
                organic +=  volume
                status = 'success'
                print("Kamu berhasil buang sampah jenis "+jenis+" dengan kategori "+sampah)
                break
            elif space2 > 0:
                print("Maaf Volume sampah kamu bikin TRASHSCAN penuh nih ")
                print("coba cari kotak yg lain yaa..")
                status = 'failed'
                break
            else:
                print("Aduh TRASHSCAN udah penuh nih")
                print("TRASHSCAN kasih tau petugas dulu yah.. ")
                status = 'failed'
                break
        elif jenis_sampah ==4:
            sampah = 'ORGANIC'
            jenis = 'Tumbuhan'
            if space1 - volume >= 0:
                organic +=  volume
                status = 'success'
                print("Kamu berhasil buang sampah jenis "+jenis+" dengan kategori "+sampah)
                break
            elif space2 > 0:
                print("Maaf Volume sampah kamu bikin TRASHSCAN penuh nih ")
                print("coba cari kotak yg lain yaa..")
                status = 'failed'
                break
            else:
                print("Aduh TRASHSCAN udah penuh nih")
                print("TRASHSCAN kasih tau petugas dulu yah.. ")
                status = 'failed'
                break
        elif jenis_sampah ==5:
            sampah = 'NON_ORGANIC'
            jenis = 'Kaleng'
            if space2 - volume >= 0:
                non_organic +=  volume
                status = 'success'
                print("Kamu berhasil buang sampah jenis "+jenis+" dengan kategori "+sampah)
                break
            elif space2 > 0:
                print("Maaf Volume sampah kamu bikin TRASHSCAN penuh nih ")
                print("coba cari kotak yg lain yaa..")
                status = 'failed'
                break
            else:
                print("Aduh TRASHSCAN udah penuh nih")
                print("TRASHSCAN kasih tau petugas dulu yah.. ")
                status = 'failed'
                break
        elif jenis_sampah ==6:
            sampah = 'NON_ORGANIC'
            jenis = 'Kertas'
            if space2 - volume >= 0:
                non_organic +=  volume
                status = 'success'
                print("Kamu berhasil buang sampah jenis "+jenis+" dengan kategori "+sampah)
                break
            elif space2 > 0:
                print("Maaf Volume sampah kamu bikin TRASHSCAN penuh nih ")
                print("coba cari kotak yg lain yaa..")
                status = 'failed'
                break
            else:
                print("Aduh TRASHSCAN udah penuh nih")
                print("TRASHSCAN kasih tau petugas dulu yah.. ")
                status = 'failed'
                break
        elif jenis_sampah ==7:
            sampah = 'NON_ORGANIC'
            jenis = 'Karet'
            if space2 - volume >= 0:
                non_organic +=  volume
                status = 'success'
                print("Kamu berhasil buang sampah jenis "+jenis+" dengan kategori "+sampah)
                break
            elif space2 > 0:
                print("Maaf Volume sampah kamu bikin TRASHSCAN penuh nih ")
                print("coba cari kotak yg lain yaa..")
                status = 'failed'
                break
            else:
                print("Aduh TRASHSCAN udah penuh nih")
                print("TRASHSCAN kasih tau petugas dulu yah.. ")
                status = 'failed'
                break
        elif jenis_sampah ==8:
            sampah = 'ORGANIC'
            jenis = 'Daging'
            if space1 - volume >=0:
                organic +=  volume
                print("Kamu berhasil buang sampah jenis "+jenis+" dengan kategori "+sampah)
                status = 'success'
                break
            elif space2 > 0:
                print("Maaf Volume sampah kamu bikin TRASHSCAN penuh nih ")
                print("coba cari kotak yg lain yaa..")
                status = 'failed'
                break
            else:
                print("Aduh TRASHSCAN udah penuh nih")
                print("TRASHSCAN kasih tau petugas dulu yah.. ")
                status = 'failed'
                break
        else:
            sampah = 'Sampah tidak berkategori silahkan pilih sesuai jenis sampah'
            status = 'failed'
            break
        
    else:
        print("Aduh TRASHSCAN udah penuh nih")
        print("TRASHSCAN kasih tau petugas dulu yah.. ")
        status = 'failed'
        break

print("TRASHSCAN Volume ORGANIC: ",organic,"% dan NON_ORGANIC :",non_organic,"%")
print("Terima kasih yaa..")

def sensor_send():
    while 1:
        dataKapasitif = { #Sensor Pemisah
        'ORGANIC' : 32,
        'NON_ORGANIC' : 50,
        }
        dataUltrasonic = {
        'ORGANIC' : organic,
        'NON_ORGANIC' : non_organic,
        }
        antares.setAccessKey(ANTARES_KEY)
        antares.send(dataUltrasonic, 'TRASHSCAN', 'SensorUltrasonik')
        print("==== SEND DATA ====")
        #print(" Sensor ProximityKapasitif", dataKapasitif)
        print(" Sensor Ultrasonic", dataUltrasonic)
        print("===================")
        break

def catatan():
    datapengguna ={
        'Nama' : nama,
        'Time' : datetime.now().strftime('%H:%M:%S'),
        'Jenis_sampah' : sampah,
        'Volume' : volume,
    }
    antares.setAccessKey(ANTARES_KEY)
    antares.send(datapengguna, 'TRASHSCAN', 'Pengguna')


if  status == 'success':
    sensor_send()
    catatan()
else:
    print(status)

