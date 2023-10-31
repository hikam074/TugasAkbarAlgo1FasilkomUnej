import csv
import os 
import pandas as pd
from pathlib import Path  # import modul path
import dat
# KOREKSI : UBAH PAKAI MODULE PANDAS

def getData():
    df = pd.read_csv("presensi_databse.csv")
    df.index = range (1,len(df)+1)
    print(df)

def main_page_admin():
    def admin_tambah_karyawan(): #FAUZUL 
        os.system('cls')
        with open('employee_account_database.csv', 'a', newline='') as admin_menu_1:
            tambah_fileEmployeecsv = csv.write(admin_menu_1)
            ID      = int  (input("Masukkan ID karyawan baru: "))
            Nama    = input("Masukkan nama lengkap karyawan baru: ")
            Posisi  = input("Masukkan posisi karyawan baru: ")
            Shift   = input("Masukkan shift karyawan baru: ")
            tambah_fileEmployeecsv.writerow([
                ID, Nama, Posisi, Shift
            ])
            admin_menu_1.close()
            os.system('cls')
            print("Data Karyawan Baru Berhasil Ditambahkan!! \n")
            input("\nEnter untuk lanjutkan")
            os.system('cls')
            main_page_admin()
              
    def admin_edit_data_karyawan() : #Raihan
        os.system ("cls") 
        getData()
        df          = pd.read_csv('employee_account_databse.csv')
        edit        = int(input("pilih jadwal nomor karyawan yang ingin untuk diedit : "))
        ID_karyawan = int(input("Masukkan ID baru  karyawan : "))
        Nama        = input("Masukkan nama baru karyawan : ")
        Shift1      = input("masukan shift baru :")
        Shift2      = input("masukan shift baru :")
        Shift3      = input("masukan shift baru :")
        
        df.at[edit-1, "ID karyawan"]    = ID_karyawan
        df.at[edit-1, "Nama"]           = Nama
        df.at[edit-1, "Shift 1"]        = Shift1
        df.at[edit-1, "Shift 2"]        = Shift2
        df.at[edit-1, "Shift 3"]        = Shift3

        df.to_csv("presensi_databse.csv", index = False)
        print("data berhasil diedit")
        input("\n tekan enter untuk lanjutkan")
        main_page_admin()
        

    def admin_lihat_kehadiran_karyawan():
        os.system("cls")
        presence_df = pd.read_csv('presensi_database.csv'),['ID','Nama','Shift 1','Shift 2','Shift 3']
        summary_df  = presence_df.groupby('Id').agg({'Nama': 'first', 'Shift 1': 'count', 'Shift 2': 'count', 'Shift 3': 'count'})
        summary_df['Jumlah Hari Kerja'] = summary_df['Shift 1'] + summary_df['Shift 2'] + summary_df['Shift 3']
        summary_df['Total Jam Kerja']   = summary_df['Jumlah Jam Kerja'] * 8
        summary_df['Rata-Rata Jam Kerja Per Hari '] = summary_df['Total Jam Kerja'] / summary_df['Jumlah Hari Kerja']
        summary_df = summary_df[['nama', 'Jumlah Hari Kerja', 'Total Jam Kerja','Rata-Rata Jam Kerja Per Hari']]
        os.system("cls")

    def admin_hapus_data_karyawan():
        o.system('cls')
        employee_df  = pd.read_csv('employee account database', names=['ID', 'Nama', ' Shift'])
        nama         = input("Masukkan Nama Karyawan Yang Ingin Dihapus: ")
        employee_row = employee_df.loc[employee_df['Nama']==nama]
        employee_df  = employee_df.drop(employee_row.index)
        employee_df.to_csv('employee_account_database'.csv, index=False)
        os.system('cls')

    def admin_lihat_data_karyawan():
        os.system('cls')
        employee_df = pd.read_csv('employee_account_database,csv', names=['ID', 'Nama', 'Shift'])
        print(employee_df.to_markdown())

        cari = input("Masukkan nama, shift karyawan yang ingin dicari: ")
        hasil = employee_df.query("Nama == @cari or Shift == @cari")
        print(hasil.to_markdown())

    while True:                 # HIKAM
        print("\nMenu Admin:")
        print("1. Tambahkan Karyawan")
        print("2. Edit Data Admin")
        print("3. Edit Data Karyawan")
        print("4. Edit Presensi Karyawan")
        print("5. Lihat Data Admin")
        print("6. Lihat Data Karyawan")
        print("7. Lihat Presensi Karyawan")
        print("8. Hapus Data Admin")
        print("9. Hapus Data Karyawan") 
        print("10. Keluar") # Keluar dari menu admin

        pilihan_admin = input("Pilih menu (1/2/3/4/5): ")
                                                            #PAKAI SUBMENU!!!!
        if pilihan_admin == "1":
            admin_tambah_karyawan()
        elif pilihan_admin == "2":

        elif pilihan_admin == "3":
            admin_edit_shift_karyawan()

        elif pilihan_admin == "4":
            admin_

        elif pilihan == "5":
            os.system('cls')
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
        os.system('cls')

# Membuka file untuk pertama kalinya
if not(Path('admin_account_database.csv').is_file()):
    #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
    with open('admin_account_database.csv', 'w', newline='') as fileAdmincsv:
        admin_list = csv.DictWriter(fileAdmincsv, fieldnames=['ID','Nama','Posisi','Bidang'],  delimiter=',') 
        admin_list.writeheader()
    adding_first_account()

def adding_first_account():
    first_account_ID     = input("Anda adalah admin pertama. Masukkan ID admin pertama : ")
    first_account_nama   = input("Masukkan Nama anda : ")
    first_account_posisi = input("Masukkan Posisi anda : ")
    first_account_bidang = input("Masukkan bidang divisi anda : ")
    
    first_account = pd.DataFrame()
    first_account.concate

        
    
if not(Path('employee_account_database.csv').is_file()):
    #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
    with open('employee_account_database.csv', 'w', newline='') as fileEmployeecsv:
        employee_list = csv.DictWriter(fileEmployeecsv, fieldnames=['ID','Nama','Posisi','Shift'],  delimiter=',') 
        employee_list.writeheader()
# apabila database presensi belum ada
if not(Path('presensi_database.csv').is_file()):
    #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
    with open('presensi_database.csv', 'w', newline='') as filePresencecsv:
        presence_list = csv.DictWriter(filePresencecsv, fieldnames=['ID','Nama','Posisi','Shift 1','Shift 2','Shift 3'],  delimiter=',') 
        presence_list.writeheader()

# HALAMAN LOGIN

login_page_condition = True
while login_page_condition:

    print("===LOGIN PAGE===")
    print("*Press enter to quit tne menu*\n")
    username = input("Masukkan ID anda : ")


    if username == '':
        break
    else:
        with open('admin_account_database.csv','r') as fileAdmincsv:
            admin_list = fileAdmincsv.read()
            if username in admin_list:
                main_page_admin()
                login_page_condition = False
            else:
                login_page_condition = True

        with open('employee_account_database.csv', 'r') as fileEmployeecsv:
            employee_list = fileEmployeecsv.read()              
            if username in employee_list:
                main_page_employee()
                login_page_condition = False
            else:
                login_page_condition = True


# # Inisialisasi data absensi
# absensi_karyawan = pd.DataFrame(columns=["Nama", "Tanggal", "Shift"])
# absensi_admin = pd.DataFrame(columns=["Nama", "Tanggal", "Shift"])

# # Data admin (contoh, ganti sesuai kebutuhan)
# admin_username = "Admin Toko Berkah"
# admin_password = "123"

# # Data karyawan (ganti sesuai kebutuhan)
# karyawan_data = {}  # Kosong pada awalnya

# # Fungsi untuk login admin
# def login_admin():
#     os.system('cls')
#     username = input("Masukkan username admin: ")
#     password = input("Masukkan password admin: ")
#     if username == admin_username and password == admin_password:
#         print("Login berhasil!")
#         menu_admin()
#     else:
#         print("Login gagal. Coba lagi.")
#         os.system('cls')

# # Fungsi untuk menu admin
# def menu_admin():
#     os.system('cls')
#     while True:
#         print("\nMenu Admin:")
#         print("1. Daftar Karyawan")
#         print("2. Edit Shift")
#         print("3. Lihat Kehadiran")
#         print("4. Hapus Karyawan")
#         print("5. Keluar") # Pilihan baru
#         pilihan = input("Pilih menu (1/2/3/4/5): ")

#         if pilihan == "1":
#             daftar_karyawan()
#         elif pilihan == "2":
#             edit_shift()
#         elif pilihan == "3":
#             lihat_kehadiran()
#         elif pilihan == "4": # Pilihan baru
#             nama = input("Masukkan nama karyawan yang ingin dihapus: ")
#             hapus_karyawan(nama) # Memanggil fungsi hapus_karyawan()
#         elif pilihan == "5":
#             break
        
#         else:
#             print("Pilihan tidak valid. Silakan pilih menu yang benar.")
#         os.system('cls')

# # Fungsi untuk mendaftarkan karyawan baru
# def daftar_karyawan():
#     os.system('cls')
#     nama = input("Masukkan nama karyawan: ")
#     shift = input("Masukkan shift (pagi/siang/malam): ")
#     karyawan_data[nama] = {"nama": nama, "shift": shift}
#     absensi_karyawan.loc[len(absensi_karyawan)] = [nama, "", ""]
#     print(f"Karyawan {nama} berhasil didaftarkan.")
#     os.system('cls')

# def edit_shift():
#     os.system('cls')
#     nama = input("Masukkan nama karyawan: ")
#     if nama in karyawan_data:
#         shift = input("Masukkan shift (pagi/siang/malam): ")
#         karyawan_data[nama]["shift"] = shift
#         absensi_karyawan.loc[absensi_karyawan["Nama"] == nama, "Shift"] = shift
#         print(f"Shift karyawan {nama} berhasil diupdate.")
#     else:
#         print(f"Karyawan {nama} tidak ditemukan.")
#     os.system('cls')

# def lihat_kehadiran():
#     os.system('cls')
#     print(absensi_karyawan)

# # Fungsi untuk menghapus data karyawan
# def hapus_karyawan(nama):
#     if nama in karyawan_data:
#         absensi_karyawan.drop(index=nama, inplace=True)
#         karyawan_data.pop(nama)
#         print(f"Karyawan {nama} berhasil dihapus.")
#     else:
#         print(f"Karyawan {nama} tidak ditemukan.")

# login_admin()

