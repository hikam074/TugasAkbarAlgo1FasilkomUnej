import csv                  # import csv
import os                   # agar bisa clean terminal
import pandas as pd         # import pandas
import numpy as np          # import numpy
from pathlib import Path    # import modul path

# HALAMAN UTAMA ADMIN-----------------------------------------------------------------------------------------------------------------------------------------

def main_page_admin():
    os.system('cls')
    print('admin>menu utama\n=============== ADMIN MENU ===============')    # mengucapkan selamat datang
    data_admin = []
    with open('admin_account_database.csv') as csvfile_admin:       # mendeteksi nama kita untuk ditampilkan di ucapan sepamat datang
        reader_Admin = csv.reader(csvfile_admin)
        for row in reader_Admin:
            data_admin.append(row)
    admin_column = [x[0] for x in data_admin]
    if launch_ID in admin_column:
        for x in range(0,len(data_admin)):
            if launch_ID == data_admin[x][0]:
                print(f'Selamat Datang, admin "{data_admin[x][1]}"!\n')
    print('\nMenu:\n[1] Tambahkan Orang\n[2] Edit Data\n[3] Edit Presensi Karyawan\n[4] Lihat Data\n[5] Hapus Data\n[6] Keluar')    # pilihan menu
    menu_choice = input("\nPilih menu : ")
    print()

    if menu_choice == '1':          # menu tambahkan orang, terdiri dari tambahkan admin, tambahkan karyawan
        menu_choice_1 = input("[1]Tambahkan Admin\n[2]Tambahkan Karyawan\nPilih menu : ")
        if menu_choice_1 == '1':    # submenu tambahkan admin
            os.system('cls')
            masukan_tambah_admin = input("admin>menu utama>tambahkan orang>tambahkan admin\n=============== MENU TAMBAHKAN ADMIN ===============\n\nMasukkan data admin [ID,Nama,Posisi,Bidang] : ")
            file = open('admin_account_database.csv','a')       # file handling untuk append data
            file.write(masukan_tambah_admin)
            file.write('\n')
            file.close
            input("Data admin berhasil ditambahkan!\nPress [enter] to back to Main Menu")      # back to main menu
            main_page_admin()
        elif menu_choice_1 == '2':  # submenu tambahkan karyawan
            os.system('cls')
            masukan_tambah_karyawan = input("admin>menu utama>tambahkan orang>tambahkan karyawan\n=============== MENU TAMBAHKAN KARYAWAN ===============\n\nMasukkan data karyawan [ID,Nama,Posisi,Shift 1,Shift 2,Shift 3] : ")
            file = open('employee_account_database.csv','a')    # file handling untuk append data
            file.write(masukan_tambah_karyawan)
            file.write('\n')
            file.close
            input("Data karyawan berhasil ditambahkan!\nPress [enter] to back to Main Menu")   # back to main menu
            main_page_admin()
        else:                       # submenu : salah input jadi balik ke menu
            main_page_admin()

    elif menu_choice == '2':        # menu edit data, terdiri dari edit data admin, edit data karyawan
        menu_choice_2 = input("[1]Edit Data Admin\n[2]Edit Data Karyawan\nPilih menu : ")
        if menu_choice_2 == '1':    # edit data admin
            os.system('cls')
            masukan_edit_admin = input("admin>menu utama>edit data>edit data admin\n=============== MENU EDIT DATA ADMIN ===============\n\nMasukkan ID admin yang hendak diubah : ")
           
            # tulis kode disini

            input("Press [enter] to back to Main Menu")    # back to main menu
            main_page_admin()
        elif menu_choice_2 == '2':  # edit data karyawan
            os.system('cls')
            masukan_edit_employee = input("admin>menu utama>edit data>edit data karyawan\n=============== MENU EDIT DATA KARYAWAN ===============\n\nMasukkan ID karyawan yang hendak diubah : ")

            # tulis kode disini

            input("Press [enter] to back to Main Menu")    # back to main menu
            main_page_admin()
        else:
            main_page_admin()

    elif menu_choice == '3':    # edit presensi karyawan
            os.system('cls')
            masukan_edit_presensi = input("admin>menu utama>edit presensi karyawan\n=============== MENU EDIT PRESENSI KARYAWAN ===============\n\nMasukkan ID karyawan yang hendak diubah : ")

        # tulis kode disini
 
        input("Press [enter] to back to Main Menu")  # back to main menu
        main_page_admin()

    elif menu_choice == '4':
        menu_choice_4 = input("[1]Lihat Data Admin\n[2]Lihat Data Karyawan\n[3]Lihat Presensi Karyawan\nPilih menu : ")
        if menu_choice_4 == '1':    # lihat data admin
            os.system('cls')
            print("admin>menu utama>lihat data>lihat data admin\n=============== MENU LIHAT DATA ADMIN ===============\n")
            data_admin = []
            with open('admin_account_database.csv') as csvfile_admin:       # membuka data admin dari csv ke list
                reader_Admin = csv.reader(csvfile_admin)
                for row in reader_Admin:
                    data_admin.append(row)
            df = pd.DataFrame(data_admin, columns=kolom_admin)              # memasukkan data list ke pandas
            print(df)                                                       # menampilkan data
            input("Press [enter] to back to Main Menu")  # back to main menu
            main_page_admin()
        elif menu_choice_4 == '2':    # lihat data karyawan
            os.system('cls')
            print("admin>menu utama>lihat data>lihat data karyawan\n=============== MENU LIHAT DATA KARYAWAN ===============\n")
            data_employee = []
            with open('employee_account_database.csv') as csvfile_employee: # membuka data karyawan dari csv ke list
                reader_employee = csv.reader(csvfile_employee)
                for row in reader_employee:
                    data_employee.append(row)
            df = pd.DataFrame(data_employee, columns=kolom_employee)        # memasukkan data list ke pandas
            print(df)                                                       # menampilkan data
            input("Press [enter] to back to Main Menu")  # back to main menu
            main_page_admin()
        elif menu_choice_4 == '3':    # lihat presensi karyawan
            os.system('cls')
            print("admin>menu utama>lihat data>lihat presensi karyawan\n=============== MENU LIHAT PRESENSI KARYAWAN ===============\n")
            data_presensi = []
            with open('presensi_database.csv') as csvfile_presensi:         # membuka data presensi karyawan dari csv ke list
                reader_presensi = csv.reader(csvfile_presensi)
                for row in reader_presensi:
                    data_presensi.append(row)
            df = pd.DataFrame(data_presensi, columns=kolom_presensi)        # memasukkan data list ke pandas
            print(df)                                                       # menampilkan data
            input("Press [enter] to back to Main Menu)  # back to main menu
            main_page_admin()
        else:
            main_page_admin()

    elif menu_choice == '5':
        menu_choice_5 = input("[1] Hapus Data Admin\n[2] Hapus Data Karyawan\n[3] Hapus Presensi Karyawan\nPilih menu : ")
        if menu_choice_5 == '1':    # hapus data admin
            os.system('cls')
            print("admin>menu utama>hapus data>\n=============== MENU HAPUS DATA ADMIN ===============\nmenampilkan keseluruhan data...\n")
            data_admin = []
            with open('admin_account_database.csv') as csvfile_admin:
                reader_Admin = csv.reader(csvfile_admin)
                for row in reader_Admin:
                    data_admin.append(row)
            df = pd.DataFrame(data_admin, columns=kolom_admin)
            print(df)
            menghapus_file = input("\nMasukkan ID admin yang mau dihapus : ")      # user memasukkan data yang ingin dihapus
            admin_column = [x[0] for x in data_admin]
            if menghapus_file in admin_column:
                for x in range(0,len(data_admin)):
                    if menghapus_file == data_admin[x][0]:
                        print(f'Data admin yang akan dihapus : "{data_admin[x]}"!\n')
                        pilihan_admin_hapus = input("Anda yakin?\nTekan [1] untuk menghapus\nTekan [2] atau [tombol lain] untuk membatalkan : ")
                        if pilihan_admin_hapus == '1':
                            df = pd.DataFrame(data_admin, columns=kolom_admin)
                            df = df.drop(x)
                            np.savetxt('admin_account_database.csv',df,delimiter=',',fmt='% s')
                            print(f"\nID deleted : {menghapus_file}\nHasil data : \n{df}")     # menampilkan data yang dihapus
                            input("\nPress [enter] to back to Main Menu")
                            main_page_admin()
                        else:
                            input("\nMembatalkan ... Press [enter] to back to Main Menu")
                            main_page_admin()
            else:
                input("\nData tidak ada ... Press [enter] to back to Main Menu")
                main_page_admin()

        elif menu_choice_5 == '2':    # hapus data karyawan

            os.system('cls')
            print("admin>menu utama>hapus data>\n=============== MENU HAPUS DATA KARYAWAN ===============\nmenampilkan keseluruhan data...\n")
            data_employee = []
            with open('employee_account_database.csv') as csvfile_employee:
                reader_employee = csv.reader(csvfile_employee)
                for row in reader_employee:
                    data_employee.append(row)
            df = pd.DataFrame(data_employee, columns=kolom_employee)
            print(df)

            menghapus_file = input("\nMasukkan ID admin yang mau dihapus : ")      # user memasukkan data yang ingin dihapus
            employee_column = [x[0] for x in data_employee]
            if menghapus_file in employee_column:
                for x in range(0,len(data_employee)):
                    if menghapus_file == data_employee[x][0]:
                        print(f'Data karyawan yang akan dihapus : "{data_employee[x]}"!\n')
                        pilihan_employee_hapus = input("Anda yakin?\nTekan [1] untuk menghapus\nTekan [2] atau [tombol lain] untuk membatalkan : ")
                        if pilihan_employee_hapus == '1':
                            df = pd.DataFrame(data_employee, columns=kolom_employee)
                            df = df.drop(x)
                            np.savetxt('employee_account_database.csv',df,delimiter=',',fmt='% s')
                            print(f"\nID deleted : {menghapus_file}\nHasil data : \n{df}")     # menampilkan data yang dihapus
                            input("\nPress [enter] to back to Main Menu")
                            main_page_admin()
                        else:
                            input("\nMembatalkan ... Press [enter] to back to Main Menu")
                            main_page_admin()
            else:
                input("\nData tidak ada ... Press [enter] to back to Main Menu")
                main_page_admin()

        elif menu_choice_5 == '3':    # hapus presensi karyawan

            # tulis kode disini
 
            print("Press [enter] to back to Main Menu")
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
