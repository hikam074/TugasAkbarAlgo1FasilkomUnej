import csv
import os 
import pandas as pd
from pathlib import Path  # import modul path


# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# MEMBUKA FILE UNTUK PERTAMA KALINYA--------------------------------------------------------------------------------------------------------------------------

os.system('cls')

# apabila database akun karyawan
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

# apabila database admin belum ada
if not(Path('admin_account_database.csv').is_file()):
    #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
    with open('admin_account_database.csv', 'w', newline='') as fileAdmincsv:
        admin_list = csv.DictWriter(fileAdmincsv, fieldnames=['ID','Nama','Posisi','Bidang'],  delimiter=',') 
        admin_list.writeheader()

    first_account_ID     = str(input("Anda adalah admin pertama. Masukkan ID anda : "))
    first_account_nama   = str(input("Masukkan Nama anda : "))
    first_account_posisi = str(input("Masukkan Posisi anda : "))
    first_account_bidang = str(input("Masukkan bidang divisi anda : "))

    first_input = f"{first_account_ID},{first_account_nama},{first_account_posisi},{first_account_bidang}"
    fileAdmincsv = open('admin_account_database.csv', 'a') 
    fileAdmincsv.write(first_input)
    fileAdmincsv.close

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# HALAMAN LOGIN-----------------------------------------------------------------------------------------------------------------------------------------------

launch_page_condition = True
while launch_page_condition:

    print("=============== WELCOME TO LAUNCH PAGE ===============")
    launch_menu = input("Press [1] to login, Press [enter] to quit the app : ")
    launch_menu = input("Masukkan ID anda : ")

    if launch_menu == '':
        break
    else:
        with open('admin_account_database.csv','r') as fileAdmincsv:
            admin_list = fileAdmincsv.read()
            if launch_menu in admin_list:
                main_page_admin()
                launch_page_condition = False
            else:
                launch_page_condition = True

        with open('employee_account_database.csv', 'r') as fileEmployeecsv:
            employee_list = fileEmployeecsv.read()              
            if launch_menu in employee_list:
                main_page_employee()
                launch_page_condition = False
            else:
                launch_page_condition = True

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_page_admin():
    print("Selamat Datang,")




def main_page_employee()
