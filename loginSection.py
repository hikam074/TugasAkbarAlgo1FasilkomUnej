import pandas as pd
import csv
import os 

# Inisialisasi data absensi
absensi_karyawan = pd.DataFrame(columns=["Nama", "Tanggal", "Shift"])
absensi_admin = pd.DataFrame(columns=["Nama", "Tanggal", "Shift"])

# Data admin (contoh, ganti sesuai kebutuhan)
admin_username = "Admin Toko Berkah"
admin_password = "123"

# Data karyawan (ganti sesuai kebutuhan)
karyawan_data = {}  # Kosong pada awalnya

# Fungsi untuk login admin
def login_admin():
    os.system('cls')
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    if username == admin_username and password == admin_password:
        print("Login berhasil!")
        menu_admin()
    else:
        print("Login gagal. Coba lagi.")
        os.system('cls')

# Fungsi untuk menu admin
def menu_admin():
    os.system('cls')
    while True:
        print("\nMenu Admin:")
        print("1. Daftar Karyawan")
        print("2. Edit Shift")
        print("3. Lihat Kehadiran")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            daftar_karyawan()
        elif pilihan == "2":
            edit_shift()
        elif pilihan == "3":
            lihat_kehadiran()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
        os.system('cls')

# Fungsi untuk mendaftarkan karyawan baru
def daftar_karyawan():
    os.system('cls')
    nama = input("Masukkan nama karyawan: ")
    shift = input("Masukkan shift (pagi/siang/malam): ")
    karyawan_data[nama] = {"nama": nama, "shift": shift}
    absensi_karyawan.loc[len(absensi_karyawan)] = [nama, "", ""]
    print(f"Karyawan {nama} berhasil didaftarkan.")
    os.system('cls')

def edit_shift():
    os.system('cls')
    nama = input("Masukkan nama karyawan: ")
    if nama in karyawan_data:
        shift = input("Masukkan shift (pagi/siang/malam): ")
        karyawan_data[nama]["shift"] = shift
        absensi_karyawan.loc[absensi_karyawan["Nama"] == nama, "Shift"] = shift
        print(f"Shift karyawan {nama} berhasil diupdate.")
    else:
        print(f"Karyawan {nama} tidak ditemukan.")
    os.system('cls')

def lihat_kehadiran():
    os.system('cls')
    print(absensi_karyawan)

login_admin()
