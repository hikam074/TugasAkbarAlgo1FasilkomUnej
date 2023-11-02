import csv    # import csv
import os     # agar bisa clean terminal
import pandas as pd        # import pandas
from pathlib import Path   # import modul path

# <--pakai komen disamping untuk berkomunikasi, soalnya kodenya bakal ancur klo semua bisa ngetik

# fitur:

# # login page v
# # launch page v
# # main menu admin v
# # main menu employee v

# # ADMIN
# # -tambahkan orang v
# # --tambahkan admin v
# # --tambahkan karyawan v
# # -edit data
# # --edit data admin
# # --edit data karyawan
# # -edit presensi karyawan
# # -lihat data
# # --lihat data admin
# # --lihat data karyawan
# # --lihat presensi karyawan
# # -hapus data
# # --hapus data admin
# # --hapus data karyawan
# # --hapus presensi karyawan
# # -keluar

# # KARYAWAN
# # -presensi sekarang
# # --masukkan tanggal
# # ---shift pagi
# # ---shift siang
# # ---shift malam
# # ---kembali
# # -lihat jadwal shift
# # -lihat rekapitulasi presensi
# # -informasi mengenai shift
# # -keluar

# HALAMAN UTAMA ADMIN-----------------------------------------------------------------------------------------------------------------------------------------

def main_page_admin():
    os.system('cls')
    print('=============== ADMIN MENU ===============')    # mengucapkan selamat datang
    data_admin = []
    with open('admin_account_database.csv') as csvfile_admin:
        reader_Admin = csv.reader(csvfile_admin)
        for row in reader_Admin:
            data_admin.append(row)
    admin_column = [x[0] for x in data_admin]
    if launch_ID in admin_column:
        for x in range(0,len(data_admin)):
            if launch_ID == data_admin[x][0]:
                print(f'Selamat Datang, admin "{data_admin[x][1]}"!\n')

    print('\nMenu:\n[1] Tambahkan Orang\n[2] Edit Data\n[3] Edit Presensi Karyawan\n[4] Lihat Data\n[5] Hapus Data\n[6] Keluar')

    menu_choice = input("\nPilih menu : ")
    print()

    if menu_choice == '1':
        menu_choice_1 = input("[1]Tambahkan Admin\n[2]Tambahkan Karyawan\nPilih menu : ")
        if menu_choice_1 == '1':    # tambahkan admin
            os.system('cls')
            masukan_tambah_admin = input("admin>menu utama>tambahkan orang>\n=============== MENU TAMBAHKAN ADMIN ===============\n\nMasukkan data admin [ID,Nama,Posisi,Bidang] : ")
            file = open('admin_account_database.csv','a')   # menggunakan file handling untuk append data
            file.write(masukan_tambah_admin)
            file.write('\n')
            file.close
            print("Data admin berhasil ditambahkan!\nPress anykey to back to Main Menu")
            input()
            main_page_admin()
        elif menu_choice_1 == '2':    # tambahkan karyawan
            os.system('cls')
            masukan_tambah_karyawan = input("admin>menu utama>tambahkan orang>\n=============== MENU TAMBAHKAN KARYAWAN ===============\n\nMasukkan data karyawan [ID,Nama,Posisi,Shift 1,Shift 2,Shift 3] : ")
            file = open('employee_account_database.csv','a')   # menggunakan file handling untuk append data
            file.write(masukan_tambah_karyawan)
            file.write('\n')
            file.close
            print("Data karyawan berhasil ditambahkan!\nPress anykey to back to Main Menu")
            input()
            main_page_admin()
        else:
            main_page_admin()

    elif menu_choice == '2':
        menu_choice_2 = input("[1]Edit Data Admin\n[2]Edit Data Karyawan\nPilih menu : ")
        if menu_choice_2 == '1':    # edit data admin
            os.system('cls')
            masukan_edit_admin = input("admin>menu utama>edit data>\n=============== MENU EDIT DATA ADMIN ===============\n\nMasukkan ID admin yang hendak diubah : ")
           
            data_admin = []
            with open('admin_account_database.csv') as csvfile_admin:
                reader_Admin = csv.reader(csvfile_admin)
                for row in reader_Admin:
                    data_admin.append(row)
            admin_column = [x[0] for x in data_admin]
            if masukan_edit_admin in admin_column:
                for x in range(0,len(data_admin)):
                    if masukan_edit_admin == data_admin[x][0]:
                        print(f'Data yang hendak diubah : "{data_admin[x]}"\n')
            
            masukan_apa_edit_admin = input("Masukkan data yang baru [ID,Nama,Posisi,Bidang] : ")

            file = open('admin_account_database.csv', 'r')    # membuka file dengan tujuan 'read' (membaca)
            data = file.readlines()                 # mengambil data dari .csv berbentuk baris untuk digunakan ke python            
            file = open('admin_account_database.csv', 'w')    # membuka file dengan tujuan 'write' (menulis timpa)

            for line in data :                                  # perulangan agar tiap baris data dibaca, 
                if line.strip("\n") != data_admin[x]:          # data dari .csv dicocokkan degan inputan user 
                    file.write(line)
            file = open('admin_account_database.csv', 'a')
            file.write(masukan_apa_edit_admin)
            file.write('\n')
            file.close

            print(f'Data baru "{masukan_apa_edit_admin}" telah diubah!')


            print("Press anykey to back to Main Menu")
            input()
            main_page_admin()
        elif menu_choice_2 == '2':    # edit data karyawan

            print("Press anykey to back to Main Menu")
            main_page_admin()
        else:
            main_page_admin()

    elif menu_choice == '3':    # edit presensi karyawan
        print("Press anykey to back to Main Menu")
        return

    elif menu_choice == '4':
        menu_choice_4 = input("[1]Lihat Data Admin\n[2]Lihat Data Karyawan\n[3]Lihat Presensi Karyawan\nPilih menu : ")
        if menu_choice_4 == '1':    # lihat data admin

            print("Press anykey to back to Main Menu")
            return
        elif menu_choice_4 == '2':    # lihat data karyawan

            print("Press anykey to back to Main Menu")
            return
        elif menu_choice_4 == '3':    # lihat presensi karyawan

            print("Press anykey to back to Main Menu")
            return
        else:
            main_page_admin()

    elif menu_choice == '5':
        menu_choice_5 = input("[1]Hapus Data Admin\n[2]Hapus Data Karyawan\n[3]Hapus Presensi Karyawan\nPilih menu : ")
        if menu_choice_5 == '1':    # hapus data admin

            print("Press anykey to back to Main Menu")
            return
        elif menu_choice_5 == '2':    # hapus data karyawan

            print("Press anykey to back to Main Menu")
            return
        elif menu_choice_5 == '3':    # hapus presensi karyawan

            print("Press anykey to back to Main Menu")
            return
        else:
            main_page_admin()

    elif menu_choice == '6':    # kembali ke login page
        launch_page_condition = True
        return
    else:
        main_page_admin()    # salah input, kembali ke menu utama admin
    os.system('cls')
            
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# HALAMAN UTAMA PEKERJA---------------------------------------------------------------------------------------------------------------------------------------

def main_page_employee():
    os.system('cls')
    print('=============== EMPLOYEE MENU ===============')    # mengucapkan selamat datang
    data_employee = []
    with open('employee_account_database.csv') as csvfile_employee:
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:
            data_employee.append(row)
    employee_column = [x[0] for x in data_employee]
    if launch_ID in employee_column:
        for x in range(0,len(data_employee)):
            if launch_ID == data_employee[x][0]:
                print(f"Selamat Datang, karyawan {data_employee[x][1]}!\n")
    print('\nMenu:\n[1] PRESENSI SEKARANG!\n[2] Lihat Jadwal Shift\n[3] Lihat Rekapitulasi Presensi\n[4] Informasi Mengenai Shift\n[5] Keluar')

    menu_choice = input("Pilih menu : ")
    if menu_choice == '1':    # presensi sekarang

        tanggal_presensi = input("Masukkan Tanggal Hari Ini [yyyy-mm-dd] : ")
        
        repeat_menu_choice_1 = True
        while repeat_menu_choice_1 :
            menu_choice_1 = input("Pilih Shift:\n[1] Pagi\n[2] Siang\n[3] Malam\n[4] Kembali Ke Menu\nPilih menu : ")
            if menu_choice_1 == '1':            # shift pagi
                repeat_menu_choice_1 = False
                return
            elif menu_choice_1 == '2':          # shift siang
                repeat_menu_choice_1 = False
                return
            elif menu_choice_1 == '3':          # shift malam
                repeat_menu_choice_1 = False
                return
            elif menu_choice_1 == '4':          # kembali ke menu utama karyawan
                main_page_employee()
            else:                               # salah input, ulang lagi
                repeat_menu_choice_1 = True

    elif menu_choice == '2':
        #print jadwal shift
        input(print("Press anykey to continue"))
        main_page_employee()
    elif menu_choice == '3':
        #print rekap absen
        input(print("Press anykey to continue"))
        main_page_employee()
    elif menu_choice == '4':
        #print eula
        input(print("Press anykey to continue"))
        main_page_employee()
    elif menu_choice == '5':        # kembali ke login page
        launch_page_condition =True
        return
    else:
        main_page_employee()
    os.system('cls')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# MEMBUKA FILE UNTUK PERTAMA KALINYA--------------------------------------------------------------------------------------------------------------------------

os.system('cls')

# apabila database akun karyawan belum ada
if not(Path('employee_account_database.csv').is_file()):
    #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
    employee = open('employee_account_database.csv', 'w')
    employee.close()

# apabila database presensi belum ada
if not(Path('presensi_database.csv').is_file()):
    #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
    presensi = open('presensi_database.csv', 'w')
    presensi.close()

# apabila database admin belum ada
if not(Path('admin_account_database.csv').is_file()):
    #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu

    first_account_ID     = str(input("Anda adalah admin pertama. Masukkan ID anda : "))
    first_account_nama   = str(input("Masukkan Nama anda : "))
    first_account_posisi = str(input("Masukkan Posisi anda : "))
    first_account_bidang = str(input("Masukkan bidang divisi anda : "))

    first_input = f"{first_account_ID},{first_account_nama},{first_account_posisi},{first_account_bidang}"

    with open('admin_account_database.csv', 'w', newline='') as fileAdmincsv:
        admin_list = csv.DictWriter(fileAdmincsv, fieldnames=[first_input],  delimiter='/') 
        admin_list.writeheader()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# HALAMAN LOGIN-----------------------------------------------------------------------------------------------------------------------------------------------

launch_page_condition = True
while launch_page_condition:
    kolom_admin = ['ID','Nama','Posisi','Bidang']
    kolom_employee = ['ID','Nama','Posisi','Shift 1','Shift 2','Shift 3']
    kolom_presensi = ['Tanggal','ID', 'Nama','Shift']

    os.system('cls')
    print("=============== WELCOME TO LAUNCH PAGE ===============")
    launch_menu = input("Press [enter] to login, Press [Q] to quit the app : ")
    if launch_menu == '':
        launch_ID = input("Masukkan ID anda : ")
        with open('admin_account_database.csv','r') as fileAdmincsv:
            admin_list = fileAdmincsv.read()
        with open('employee_account_database.csv', 'r') as fileEmployeecsv:
            employee_list = fileEmployeecsv.read()   

            if launch_ID in admin_list:
                data_admin = []
                with open('admin_account_database.csv') as csvfile_admin:
                    reader_Admin = csv.reader(csvfile_admin)
                    for row in reader_Admin:
                        data_admin.append(row)
                admin_column = [x[0] for x in data_admin]
                if launch_ID in admin_column:
                    for x in range(0,len(data_admin)):
                        if launch_ID == data_admin[x][0]:
                            launch_page_condition = False
                            main_page_admin()
                        else:
                            launch_page_condition = True
                else:
                    launch_page_condition : True
            elif launch_ID in employee_list:
                data_employee = []
                with open('employee_account_database.csv') as csvfile_employee:
                    reader_employee = csv.reader(csvfile_employee)
                    for row in reader_employee:
                        data_employee.append(row)
                employee_column = [x[0] for x in data_employee]
                if launch_ID in employee_column:
                    for x in range(0,len(data_employee)):
                        if launch_ID == data_employee[x][0]:
                            launch_page_condition = False
                            main_page_employee()
                        else:
                            launch_page_condition = True
                else:
                    launch_page_condition = True
            else:
                launch_page_condition = True
    elif launch_menu in 'Qq':
        break
    else:
        launch_page_condition = True

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
