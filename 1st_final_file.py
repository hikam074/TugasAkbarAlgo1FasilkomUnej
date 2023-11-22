
import csv                              # import csv
import os                               # agar bisa clean terminal
import pandas as pd                     # import pandas
import numpy as np                      # import numpy
from pathlib import Path                # import modul path
import tabulate                         # import nice table
import datetime                         # import time and date
from datetimerange import DateTimeRange # import range waktu
from datetime import timedelta          # melakukan operasi matematika pada objek datetime
import calendar                         # import kalender untuk melakukan operasi kalender

# HALAMAN LOGIN DAN LAUNCH PAGE ------------------------------------------------------------------------------------------------------------------------------
def launchPage():

    # WELCOME PAGE
    os.system('cls')
    print(logoLaunch)
    input("\n\nTekan [enter] untuk melanjutkan")

    launch_page_condition = True
    while launch_page_condition:

        # LOADING PAGE
        os.system('cls')
        print(logoBorder)
        print(launchInterface)
        launch_menu = input("Tekan [enter] untuk login, tekan [Q] untuk keluar program : ")
        if launch_menu == '':
            os.system('cls')
            print(logoBorder)
            print(loginInterface)
            global launch_ID
            launch_ID = input("Masukkan ID anda : ")
            global launchPass
            launchPass = input("Masukkan Passcode anda : ")
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
                            if launch_ID == data_admin[x][0] and launchPass == data_admin[x][4]:
                                launch_page_condition = False
                                main_page_admin()
                    else:
                        input("\nPERHATIAN : ID atau Passcode salah, silahkan tekan [enter] untuk coba lagi")
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
                            if launch_ID == data_employee[x][0] and launchPass == data_employee[x][6]:
                                launch_page_condition = False
                                main_page_employee()
                    else:
                        input("\nPERHATIAN : ID atau Passcode salah, silahkan tekan [enter] untuk coba lagi")
                        launch_page_condition = True
                else:
                    input("\nPERHATIAN : ID atau Passcode salah, silahkan tekan [enter] untuk coba lagi")
                    launch_page_condition = True

        elif launch_menu in 'Qq':
            os.system('cls')
            print(f"{logoLaunch}\nTerimakasih telah memakai program ini\n\nMenutup program ... Done\n\n\n©Kelompok 2 Tugas Akhir Algo 1\n2023\n\n")
            launch_page_condition = False
            break

        else:
            launch_page_condition = True

# LAUNCH PAGE SELESAI

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# HALAMAN UTAMA ADMIN ----------------------------------------------------------------------------------------------------------------------------------------

def main_page_admin():
    os.system('cls')
    print(f'admin>menu utama\n=============== ADMIN MENU ===============\nWaktu : {now_time.strftime("\r%A, %d %B %Y | %H:%M:%S")}\n')    # mengucapkan selamat datang

    data_employee = []
    with open('employee_account_database.csv') as csvfile_employee:
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:
            data_employee.append(row)
    employee_column = [y[0] for y in data_employee]

    data_admin = []
    with open('admin_account_database.csv') as csvfile_admin:       # mendeteksi nama kita untuk ditampilkan di ucapan selamat datang
        reader_Admin = csv.reader(csvfile_admin)
        for row in reader_Admin:
            data_admin.append(row)
    admin_column = [x[0] for x in data_admin]
    if launch_ID in admin_column:
        for x in range(0,len(data_admin)):
            if launch_ID == data_admin[x][0]:
                print(f'Selamat Datang, admin "{data_admin[x][1]}"! Apa yang ingin anda lakukan saat ini?\n')
    print('\nMenu:\n[1] Tambahkan Orang\n[2] Edit Data\n[3] Edit Presensi Karyawan\n[4] Lihat Data\n[5] Hapus Data\n[6] Keluar')    # pilihan menu
    menu_choice = input("\nPilih menu : ")
    print()

    if menu_choice == '1':          # FITUR 1 TAMBAHKAN ORANG
        menu_choice_1 = input("[1] Tambahkan Admin\n[2] Tambahkan Karyawan\nPilih menu : ")
        if menu_choice_1 == '1':    # FITUR 1.1 TAMBAHKAN ORANG>TAMBAHKAN ADMIN
            os.system('cls')
            print("admin>menu utama>tambahkan orang>tambahkan admin\n=============== MENU TAMBAHKAN ADMIN ===============\n")
            masukkanAdminID = input("Masukkan ID admin : ")
            if masukkanAdminID not in admin_column:
                masukkanAdminNama = input("Masukkan nama admin : ")
                masukkanAdminPosisi = input("Masukkan posisi admin : ")
                masukkanAdminBidang = input("Masukkan bidang admin : ")
                masukkanAdminPass = input("Masukkan passcode admin (case sensitive) : ")
                masukan_tambah_admin = [masukkanAdminID.upper(),masukkanAdminNama.upper(),masukkanAdminPosisi.upper(),masukkanAdminBidang.upper(),masukkanAdminPass]
                # Menambahkan data baru ke dalam list data admin
                data_admin.append(masukan_tambah_admin)
                # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                with open('admin_account_database.csv', 'w', newline='') as csvfile_admin:
                    writer_admin = csv.writer(csvfile_admin)
                    writer_admin.writerows(data_admin)
                input(f'\nData baru : {masukkanAdminID.upper()},{masukkanAdminNama.upper()},{masukkanAdminPosisi.upper()},{masukkanAdminBidang.upper()},{masukkanAdminPass}\nPERHATIAN : Data admin berhasil ditambahkan!\n\nTekan [enter] untuk kembali ke menu utama')
            else:
                input(f'\nPERHATIAN : Data admin "{masukkanAdminID}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
            main_page_admin()
        # FITUR 1.1 SELESAI

        elif menu_choice_1 == '2':  # FITUR 1.2 TAMBAHKAN ORANG>TAMBAHKAN KARYAWAN
            os.system('cls')
            print("admin>menu utama>tambahkan orang>tambahkan karyawam\n=============== MENU TAMBAHKAN KARYAWAN ===============\n")
            shiftPagiKasir  = [i for i in range(len(data_employee)) if ((data_employee[i][3] == 'True') and (data_employee[i][2] == 'KASIR'))]
            shiftSiangKasir = [i for i in range(len(data_employee)) if ((data_employee[i][4] == 'True') and (data_employee[i][2] == 'KASIR'))]
            shiftMalamKasir = [i for i in range(len(data_employee)) if ((data_employee[i][5] == 'True') and (data_employee[i][2] == 'KASIR'))]

            shiftPagiStaf  = [i for i in range(len(data_employee)) if (data_employee[i][3] == 'True' and (data_employee[i][2] == 'STAF TOKO'))]
            shiftSiangStaf = [i for i in range(len(data_employee)) if (data_employee[i][4] == 'True' and (data_employee[i][2] == 'STAF TOKO'))]
            shiftMalamStaf = [i for i in range(len(data_employee)) if (data_employee[i][5] == 'True' and (data_employee[i][2] == 'STAF TOKO'))]

            shiftKasir = [i for i in range(len(data_employee)) if data_employee[i][2] == 'KASIR']
            shiftStaf = [i for i in range(len(data_employee)) if data_employee[i][2] == 'STAF TOKO']

            masukkanKaryawanID = input("Masukkan ID karyawan : ")
            if masukkanKaryawanID not in employee_column :
                masukkanKaryawanNama = input("Masukkan nama karyawan : ")
                ulangAdmin1_2Posisi = True
                while ulangAdmin1_2Posisi:
                    masukkanKaryawanPosisiNo = input("[1] Kasir [2] Staf Toko\nMasukkan posisi karyawan : ")
                    if masukkanKaryawanPosisiNo == '1':
                        if len(shiftKasir)<3:
                            ulangAdmin1_2Posisi = False
                            masukkanKaryawanPosisi = 'KASIR'
                            masukkanKaryawanShift1 = input("\nMasukkan apakah karyawan bertugas Shift 1 (True/False) : ")
                            if (masukkanKaryawanShift1.capitalize() == 'True' and len(shiftPagiKasir)<1):
                                    masukkanKaryawanShift1 = 'True'
                                    masukkanKaryawanShift2 = 'False'
                                    masukkanKaryawanShift3 = 'False'
                            elif ((masukkanKaryawanShift1.capitalize() == 'True' and len(shiftPagiKasir)>=1)) or (masukkanKaryawanShift1.capitalize() == 'False'): 
                                input("Shift Pagi sudah penuh atau anda tidak memilih shift Pagi! plih shift yang lain...")
                                masukkanKaryawanShift2 = input("Masukkan apakah karyawan bertugas Shift 2 (True/False) : ")
                                if masukkanKaryawanShift2.capitalize() == 'True' and len(shiftSiangKasir)<1:
                                    masukkanKaryawanShift1 = 'False'
                                    masukkanKaryawanShift2 = 'True'
                                    masukkanKaryawanShift3 = 'False'
                                elif (masukkanKaryawanShift2.capitalize() == 'True' and len(shiftSiangKasir)>=1) or (masukkanKaryawanShift2.capitalize() == 'False'):
                                    input("Shift Pagi dan Siang sudah penuh atau anda tidak memilih shift siang! mengarahkan ke Shift Malam...")
                                    if len(shiftMalamKasir)<1:
                                        input("Kasir diarahkan ke shift malam!")
                                        masukkanKaryawanShift1 = 'False'
                                        masukkanKaryawanShift2 = 'False'
                                        masukkanKaryawanShift3 = 'True'
                                    elif len(shiftMalamKasir)>=1:
                                        print("Semua shift penuh! tidak dapat menambahkan data...")
                                        input('Tekan [enter] untuk kembali ke menu utama')
                                        main_page_admin()
                        else:
                            print("\nPosisi untuk Kasir sudah penuh!Tidak bisa menambahkan data...")
                            input('Tekan [enter] untuk kembali ke menu utama')
                            main_page_admin()
                    elif masukkanKaryawanPosisiNo == '2':
                        if len(shiftStaf)<6:
                            ulangAdmin1_2Posisi = False
                            masukkanKaryawanPosisi = 'STAF TOKO'
                            masukkanKaryawanShift1 = input("\nMasukkan apakah karyawan bertugas Shift 1 (True/False) : ")
                            if (masukkanKaryawanShift1.capitalize() == 'True' and len(shiftPagiStaf)<2):
                                    masukkanKaryawanShift1 = 'True'
                                    masukkanKaryawanShift2 = 'False'
                                    masukkanKaryawanShift3 = 'False'
                            elif ((masukkanKaryawanShift1.capitalize() == 'True' and len(shiftPagiStaf)>=2)) or (masukkanKaryawanShift1.capitalize() == 'False'): 
                                input("Shift Pagi sudah penuh atau anda tidak memilih shift Pagi! plih shift yang lain...")
                                masukkanKaryawanShift2 = input("Masukkan apakah karyawan bertugas Shift 2 (True/False) : ")
                                if masukkanKaryawanShift2.capitalize() == 'True' and len(shiftSiangStaf)<2:
                                    masukkanKaryawanShift1 = 'False'
                                    masukkanKaryawanShift2 = 'True'
                                    masukkanKaryawanShift3 = 'False'
                                elif (masukkanKaryawanShift2.capitalize() == 'True' and len(shiftSiangStaf)>=2) or (masukkanKaryawanShift2.capitalize() == 'False'):
                                    input("Shift Pagi dan Siang sudah penuh atau anda tidak memilih shift Shiang! mengarahkan ke Shift Malam...")
                                    if len(shiftMalamStaf)<2:
                                        input("Staf toko diarahkan ke shift malam!")
                                        masukkanKaryawanShift1 = 'False'
                                        masukkanKaryawanShift2 = 'False'
                                        masukkanKaryawanShift3 = 'True'
                                    elif len(shiftMalamStaf)>=2:
                                        print("Semua shift penuh! tidak dapat menambahkan data...")
                                        input('Tekan [enter] untuk kembali ke menu utama')
                                        main_page_admin()
                        else:
                            print("\nPosisi untuk Staf Toko sudah penuh!Tidak bisa menambahkan data...")
                            input('Tekan [enter] untuk kembali ke menu utama')
                            main_page_admin()
                    else:
                        input("\nMasukan tidak valid, coba lagi...")
                        ulangAdmin1_2Posisi = True

                masukkanKaryawanPass = input("Masukkan passcode karyawan (case sensitive) : ")
                masukan_tambah_karyawan = [masukkanKaryawanID.upper(),masukkanKaryawanNama.upper(),masukkanKaryawanPosisi.upper(),masukkanKaryawanShift1.capitalize(),masukkanKaryawanShift2.capitalize(),masukkanKaryawanShift3.capitalize(),masukkanKaryawanPass]
                # Menambahkan data baru ke dalam list data karyawan
                data_employee.append(masukan_tambah_karyawan)
                # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya

                with open('employee_account_database.csv', 'w', newline='') as csvfile_employee:
                    writer_employee = csv.writer(csvfile_employee)
                    writer_employee.writerows(data_employee)
                input(f'\nData baru : {masukkanKaryawanID.upper()},{masukkanKaryawanNama.upper()},{masukkanKaryawanPosisi.upper()},{masukkanKaryawanShift1.capitalize()},{masukkanKaryawanShift2.capitalize()},{masukkanKaryawanShift3.capitalize()},{masukkanKaryawanPass}\nPERHATIAN : Data karyawan berhasil ditambahkan!\n\nTekan [enter] untuk kembali ke menu utama')
            else:
                input(f'\nPERHATIAN : Data karyawan "{masukkanKaryawanID}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
            main_page_admin()
        # FITUR 1.2 SELESAI

        else:                       # FITUR 1.3 BILA SALAH KEMBALI KE MENU UTAMA KARYAWAN
            main_page_admin()
    # FITUR 1 SELESAI

    elif menu_choice == '2':        # FITUR 2 EDIT DATA 
        menu_choice_2 = input("[1] Edit Data Admin\n[2] Edit Data Karyawan\nPilih menu : ")
        if menu_choice_2 == '1':    # FITUR 2.1 EDIT DATA>EDIT DATA ADMIN
            os.system('cls')
            data_admin = []
            with open('admin_account_database.csv') as csvfile_admin:       # membuka data admin dari csv ke list
                reader_Admin = csv.reader(csvfile_admin)
                for row in reader_Admin:
                    data_admin.append(row)
            df = pd.DataFrame(data_admin, columns=kolom_admin) 
            masukan_edit_admin = input(f"admin>menu utama>edit data>edit data admin\n=============== MENU EDIT DATA ADMIN ===============\ndata saat ini:\n\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n\nMasukkan ID admin yang hendak diubah : ")
            if masukan_edit_admin in df['ID'].values:
                baris_admin = df[df['ID'] == masukan_edit_admin]  # Menemukan baris yang sesuai dengan ID
                print(f"\nData yang akan diedit : \n{baris_admin.to_string(index=False, header=False)}\n")
                IDBaru     = input("Masukkan ID baru: ")
                namaBaru   = input("Masukkan nama baru: ")
                posisiBaru = input("Masukkan posisi baru: ")
                bidangBaru = input("Masukkan bidang baru: ")
                passBaru   = input("Masukkan passcode baru: ")
                if IDBaru == '':
                    pass
                else:
                    df.iloc[baris_admin.index, 0] = IDBaru.upper()
                if namaBaru == '':
                    pass
                else:
                    df.iloc[baris_admin.index, 1] = namaBaru.upper()
                if posisiBaru == '':
                    pass
                else:
                    df.iloc[baris_admin.index, 2] = posisiBaru.upper()
                if bidangBaru == '':
                    pass
                else:
                    df.iloc[baris_admin.index, 3] = bidangBaru.upper()
                if passBaru == '':
                    pass
                else:
                    df.iloc[baris_admin.index, 4] = passBaru
                np.savetxt('admin_account_database.csv',df,delimiter=',',fmt='%s')
                print(f'\nData baru "{masukan_edit_admin}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n')
            else:
                print(f'PERHATIAN : "{masukan_edit_admin}" tidak ada dalam database!')
            input("Tekan [enter] untuk kembali ke menu utama")    # back to main menu
            main_page_admin()
        # FITUR 2.1 SELESAI

        elif menu_choice_2 == '2':  # FITUR 2.2 EDIT DATA>EDIT DATA KARYAWAN
            os.system('cls')
            data_employee = []
            with open('employee_account_database.csv') as csvfile_employee:       # membuka data employee dari csv ke list
                reader_employee = csv.reader(csvfile_employee)
                for row in reader_employee:
                    data_employee.append(row)
            df = pd.DataFrame(data_employee, columns=kolom_employee) 
            masukan_edit_employee = input(f"admin>menu utama>edit data>edit data karyawan\n=============== MENU EDIT DATA KARYAWAN ===============\n\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n\nMasukkan ID karyawan yang hendak diubah : ")
            if masukan_edit_employee in df['ID'].values:
                baris_employee = df[df['ID'] == masukan_edit_employee]  # Menemukan baris yang sesuai dengan ID
                edit_employee_profil = input(f"\nData yang akan diedit : \n{baris_employee.to_string(index=False, header=False)}\n\nPilih [1] untuk mengedit data profil karyawan atau [2] untuk mengubah shift karyawan : ")
                if edit_employee_profil == '1':     # FITUR 2.2.1 EDIT DATA>EDIT DATA KARYAWAN>EDIT DATA PROFIL
                    IDBaru = input("Masukkan ID baru: ")
                    namaBaru = input("Masukkan nama baru: ")
                    posisiBaru = input("Masukkan posisi baru: ")
                    passBaru = input("Masukkan passcode baru: ")
                    if IDBaru == '':
                        pass
                    else:
                        df.iloc[baris_employee.index, 0] = IDBaru.upper()
                    if namaBaru == '':
                        pass
                    else:
                        df.iloc[baris_employee.index, 1] = namaBaru.upper()
                    if posisiBaru == '':
                        pass
                    else:
                        df.iloc[baris_employee.index, 2] = posisiBaru.upper()
                    if passBaru == '':
                        pass
                    else:
                        df.iloc[baris_employee.index, 6] = passBaru
                    np.savetxt('employee_account_database.csv',df,delimiter=',',fmt='%s')
                    print(f'\nData baru untuk "{df.iloc[baris_employee.index, 0:3].to_string(header=False,index=False)}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n')
                # FITUR 2.2.1 SELESAI

                elif edit_employee_profil == '2':   # FITUR 2.2.2 EDIT DATA>EDIT DATA KARYAWAN>EDIT DATA SHIFT
                    shift1Baru = input("Masukkan shift 1 baru: ")
                    shift2Baru = input("Masukkan shift 2 baru: ")
                    shift3Baru = input("Masukkan shift 3 baru: ")
                    if shift1Baru == '':
                        pass
                    else:
                        df.iloc[baris_employee.index, 3] = shift1Baru.capitalize()
                    if shift2Baru == '':
                        pass
                    else:
                        df.iloc[baris_employee.index, 4] = shift2Baru.capitalize()
                    if shift3Baru == '':
                        pass
                    else:
                        df.iloc[baris_employee.index, 5] = shift3Baru.capitalize()
                    np.savetxt('employee_account_database.csv',df,delimiter=',',fmt='%s')
                    print(f'\nData baru untuk "{df.iloc[baris_employee.index, 0:3].to_string(header=False,index=False)}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n')
                # FITUR 2.2.2 SELESAI

                else:
                    print("kesalahan input, silahkan coba lagi")
        # FITUR 2.2 SELESAI

            else:
                print("PERHATIAN : Kesalahan input atau data tidak ada...")
            input("Tekan [enter] untuk kembali ke menu utama")    # back to main menu
            main_page_admin()

        else:
            input("Tekan [enter] untuk kembali ke menu utama")    # back to main menu
            main_page_admin()
    # FITUR 2 SELESAI

    elif menu_choice == '3':        # FITUR 3 EDIT DATA PRESENSI
        os.system('cls')
        data_presensi = []
        with open('presensi_database.csv') as csvfile_presensi:       # membuka data admin dari csv ke list
            reader_presensi = csv.reader(csvfile_presensi)
            for row in reader_presensi:
                data_presensi.append(row)
        df = pd.DataFrame(data_presensi, columns=kolom_presensi) 
        masukan_edit_presensi_id = input("admin>menu utama>edit presensi karyawan\n=============== MENU EDIT PRESENSI KARYAWAN ===============\n\nMasukkan ID karyawan yang hendak diubah : ")
        if masukan_edit_presensi_id in df['ID'].values:     
            masukan_edit_presensi_tanggal = input("Masukkan tanggal yang dicari : ")
            filtered_df = df.loc[df['ID'].str.contains(masukan_edit_presensi_id)]
            filtered_df = filtered_df.loc[df['Tanggal'].str.contains(masukan_edit_presensi_tanggal)]
            # del filtered_df['index']
            if len(filtered_df) == 0 :
                print("\nData yang anda cari tidak ditemukan...\n")
            else :
                print(f'\nHasil pencarian :\n\n{tabulate.tabulate(filtered_df, headers="keys", tablefmt="github")}')
                masukan_edit_presensi_index = int(input("\npilih index yang akan diedit: "))

                if masukan_edit_presensi_index == filtered_df.index :
                    print(f"\nData yang akan diedit : \n{tabulate.tabulate((df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]), headers="keys", tablefmt="github", showindex=False)}\n\nTekan [enter] untuk melewati perubahan\n")
                    masukanEditPresensiTanggalBaru = input("Masukkan tanggal baru : ")  
                    masukanEditPresensiWaktuBaru = input("Masukkan waktu baru : ")
                    masukanEditPresensiIDBaru = input("Masukkan ID baru : ")
                    masukanEditPresensiNamaBaru = input("Masukkan Nama baru : ") 
                    masukanEditPresensiShiftBaru = input("Masukkan Shift baru : ")
                    masukanEditPresensiStatusBaru = input("Masukkan Status kehadiran baru : ")
                    if masukanEditPresensiTanggalBaru == '':
                        pass
                    else:
                        df.iloc[masukan_edit_presensi_index, 0] = masukanEditPresensiTanggalBaru.upper()
                    if masukanEditPresensiWaktuBaru == '':
                        pass
                    else:
                        df.iloc[masukan_edit_presensi_index, 5] = masukanEditPresensiWaktuBaru.upper()
                    if masukanEditPresensiIDBaru == '':
                        pass
                    else:
                        df.iloc[masukan_edit_presensi_index, 1] = masukanEditPresensiIDBaru.upper()
                    if masukanEditPresensiNamaBaru == '':
                        pass
                    else:
                        df.iloc[masukan_edit_presensi_index, 2] = masukanEditPresensiNamaBaru.upper()
                    if masukanEditPresensiShiftBaru == '':
                        pass
                    else:
                        df.iloc[masukan_edit_presensi_index, 3] = masukanEditPresensiShiftBaru.upper()
                    if masukanEditPresensiStatusBaru == '':
                        pass
                    else:
                        df.iloc[masukan_edit_presensi_index, 4] = masukanEditPresensiStatusBaru.upper()
                    np.savetxt('presensi_database.csv',df,delimiter=',',fmt='%s')
                    print(f'\nData baru "{masukan_edit_presensi_id}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate((df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]), headers="keys", tablefmt="github", showindex=False)}\n')
                else:
                    print("Input anda tidak dalam range yang hendak diedit!\n")
        else:
            print(f"{masukan_edit_presensi_id} tidak ada dalam database.")
 
        input("Tekan [enter] untuk kembali ke menu utama")  # back to main menu
        main_page_admin()
    # FITUR 3 SELESAI

    elif menu_choice == '4':        # FITUR 4 LIHAT DATA
        menu_choice_4 = input("[1] Lihat Data Admin\n[2] Lihat Data Karyawan\n[3] Lihat Presensi Karyawan\nPilih menu : ")
        if menu_choice_4 == '1':    # FITUR 4.1 LIHAT DATA>LIHAT DATA ADMIN
            os.system('cls')
            print("admin>menu utama>lihat data>lihat data admin\n=============== MENU LIHAT DATA ADMIN ===============\n")
            data_admin = []
            with open('admin_account_database.csv') as csvfile_admin:       # membuka data admin dari csv ke list
                reader_Admin = csv.reader(csvfile_admin)
                for row in reader_Admin:
                    data_admin.append(row)
            df = pd.DataFrame(data_admin, columns=kolom_admin)              # memasukkan data list ke pandas
            print(tabulate.tabulate(df, headers="keys", tablefmt="grid", showindex=False))  
            
            search_ID = input("\nMasukkan ID yang hendak dicari : ")

            with open('admin_account_database.csv', 'r') as csvfile_admin:
                data_admin_s = csvfile_admin.readlines()
            df = pd.DataFrame([entry.strip().split(',') for entry in data_admin_s],columns=kolom_admin)

            if search_ID in df['ID'].values:     
                os.system('cls')
                print("admin>menu utama>lihat data>lihat data admin>cari ID\n=============== MENU LIHAT DATA ADMIN ===============") 
                filtered_df = df.loc[df['ID'].str.contains(search_ID)]
                print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')
                print(tabulate.tabulate(filtered_df, headers='keys', tablefmt='grid', showindex=False))

            else:
                print("\nData yang anda cari tidak ada...")
            
            input("\nTekan [enter] untuk kembali ke menu utama")  # back to main menu
            main_page_admin()
        # FITUR 4.1 SELESAI

        elif menu_choice_4 == '2':    # FITUR 4.2 LIHAT DATA>LIHAT DATA KARYAWAN
            os.system('cls')
            print("admin>menu utama>lihat data>lihat data karyawan\n=============== MENU LIHAT DATA KARYAWAN ===============\n\njadwal minggu ini\n")
            data_employee = []
            with open('employee_account_database.csv') as csvfile_employee: # membuka data karyawan dari csv ke list
                reader_employee = csv.reader(csvfile_employee)
                for row in reader_employee:
                    data_employee.append(row)
            df = pd.DataFrame(data_employee, columns=kolom_employee)        # memasukkan data list ke pandas
            df['Shift 1'] = df["Shift 1"].str.replace('True','PAGI')
            df['Shift 2'] = df["Shift 2"].str.replace('True','SIANG')
            df['Shift 3'] = df["Shift 3"].str.replace('True','MALAM')
            df['Shift 1'] = df["Shift 1"].str.replace('False','-')
            df['Shift 2'] = df["Shift 2"].str.replace('False','-')
            df['Shift 3'] = df["Shift 3"].str.replace('False','-')
            print(tabulate.tabulate(df, headers="keys", tablefmt="grid", showindex=False))                                                       # menampilkan data

            search_ID = input("\nMasukkan ID yang hendak dicari : ")

            with open('employee_account_database.csv', 'r') as csvfile_employee:
                data_employee = csvfile_employee.readlines()
            df = pd.DataFrame([entry.strip().split(',') for entry in data_employee],columns=kolom_employee)

            if search_ID in df['ID'].values:     
                os.system('cls')
                print("admin>menu utama>lihat data>lihat data karyawan>cari ID\n=============== MENU LIHAT DATA KARYAWAN ===============") 
                filtered_df = df.loc[df['ID'].str.contains(search_ID)]
                print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')
                print(tabulate.tabulate(filtered_df, headers='keys', tablefmt='grid', showindex=False))

            else:
                print("\nData yang anda cari tidak ada...")

            input("\nTekan [enter] untuk kembali ke menu utama")  # back to main menu
            main_page_admin()
        # FITUR 4.2 SELESAI

        elif menu_choice_4 == '3':    # FITUR 4.3 LIHAT DATA>LIHAT PRESENSI KARYAWAN
            os.system('cls')
            print("admin>menu utama>lihat data>lihat presensi karyawan\n=============== MENU LIHAT PRESENSI KARYAWAN ===============\n\nrekapitulasi total\n")
            data_presensi = []
            with open('presensi_database.csv') as csvfile_presensi:         # membuka data presensi karyawan dari csv ke list
                reader_presensi = csv.reader(csvfile_presensi)
                for row in reader_presensi:
                    data_presensi.append(row)
            df = pd.DataFrame(data_presensi, columns=kolom_presensi)        # memasukkan data list ke pandas
            df = df.sort_values(by='Tanggal',ascending=True)
            print(tabulate.tabulate(df, headers='keys', tablefmt='github', showindex=False))  # menampilkan data

            search_ID = input("\nMasukkan ID yang hendak dicari : ")

            with open('presensi_database.csv', 'r') as presensi_file:
                data_presensi = presensi_file.readlines()
            df = pd.DataFrame([entry.strip().split(',') for entry in data_presensi],columns=["Tanggal", "ID", "Nama", "Shift","kehadiran","Waktu"])

            if search_ID in df['ID'].values:     
                os.system('cls')
                print("admin>menu utama>lihat data>lihat presensi karyawan>cari ID\n=============== MENU LIHAT PRESENSI KARYAWAN ===============") 
                filtered_df = df.loc[df['ID'].str.contains(search_ID)]
                print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')
                print(tabulate.tabulate(filtered_df, headers='keys', tablefmt='github', showindex=False))

                search_date = input("\nMasukkan Tanggal yang hendak dicari [yyyy-mm-dd] : ")
                if search_date in df['Tanggal'].values:     
                    os.system('cls')
                    print("admin>menu utama>lihat data>lihat presensi karyawan>cari ID>cari tanggal\n=============== MENU LIHAT PRESENSI KARYAWAN ===============") 
                    filtered_df = df.loc[df['ID'].str.contains(search_ID)]
                    filtered_df = filtered_df.loc[df['Tanggal'].str.contains(search_date)]
                    print(f'\nHasil Pencarian untuk tanggal "{search_date}"\n')
                    print(tabulate.tabulate(filtered_df, headers='keys', tablefmt='github', showindex=False))
                else:
                    print("\nData yang anda cari tidak ada...")

            else:
                print("\nData yang anda cari tidak ada...")

            input("\nTekan [enter] untuk kembali ke menu utama")  # back to main menu
            main_page_admin()
        # FITUR 4.3 SELESAI

        else:
            main_page_admin()
    # FITUR 4 SELESAI

    elif menu_choice == '5':        # FITUR 5 HAPUS DATA
        menu_choice_5 = input("[1] Hapus Data Admin\n[2] Hapus Data Karyawan\n[3] Hapus Presensi Karyawan\nPilih menu : ")
        if menu_choice_5 == '1':    # FITUR 5.1 HAPUS DATA>HAPUS DATA ADMIN
            os.system('cls')
            print("admin>menu utama>hapus data>\n=============== MENU HAPUS DATA ADMIN ===============\nmenampilkan keseluruhan data...\n")
            data_admin = []
            with open('admin_account_database.csv') as csvfile_admin:
                reader_Admin = csv.reader(csvfile_admin)
                for row in reader_Admin:
                    data_admin.append(row)
            df = pd.DataFrame(data_admin, columns=kolom_admin)
            print(tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False))
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
                            print(f"\nID deleted : {menghapus_file}\nHasil data : \n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}")     # menampilkan data yang dihapus
                            input("\nPress [enter] to back to Main Menu")
                            main_page_admin()
                        else:
                            input("\nMembatalkan ... Press [enter] to back to Main Menu")
                            main_page_admin()
            else:
                input("\nData tidak ada ... Press [enter] to back to Main Menu")
                main_page_admin()
        # FITUR 5.1 SELESAI

        elif menu_choice_5 == '2':    # FITUR 5.2 HAPUS DATA>HAPUS DATA KARYAWAN

            os.system('cls')
            print("admin>menu utama>hapus data>\n=============== MENU HAPUS DATA KARYAWAN ===============\nmenampilkan keseluruhan data...\n")
            data_employee = []
            with open('employee_account_database.csv') as csvfile_employee:
                reader_employee = csv.reader(csvfile_employee)
                for row in reader_employee:
                    data_employee.append(row)
            df = pd.DataFrame(data_employee, columns=kolom_employee)
            print(tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False))

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
                            print(f"\nID deleted : {menghapus_file}\nHasil data : \n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}")     # menampilkan data yang dihapus
                            input("\nPress [enter] to back to Main Menu")
                            main_page_admin()
                        else:
                            input("\nMembatalkan ... Press [enter] to back to Main Menu")
                            main_page_admin()
            else:
                input("\nData tidak ada ... Press [enter] to back to Main Menu")
                main_page_admin()  
        # FITUR 5.2 SELESAI

        elif menu_choice_5 == '3':    # FITUR 5.3 HAPUS PRESENSI KARYAWAN
            os.system('cls')
            print("admin>menu utama>hapus presensi karyawan>\n=============== MENU HAPUS PRESENSI KARYAWAN ===============\nmenampilkan keseluruhan data...\n")
            data_presensi = []
            with open('presensi_database.csv') as csvfile_presensi:
                reader_presensi = csv.reader(csvfile_presensi)
                for row in reader_presensi:
                    data_presensi.append(row)
            df = pd.DataFrame(data_presensi, columns=kolom_presensi)
            print(tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)) #Menampilkan data presensi dengan tabulate agar terlihat rapi
            masukkan_tanggal_presensi = str(input("\nMasukkan tanggal yang dicari :"))

            filtered_df = df.loc[df['Tanggal'].str.contains(masukkan_tanggal_presensi)]        
            print(tabulate.tabulate(filtered_df, headers="keys", tablefmt="github"))

            masukkan_hapus_presensi = input("\nMasukkan index yang hendak dihapus : ")
            if int(masukkan_hapus_presensi) in range(len(df)):
                df = df.drop(int(masukkan_hapus_presensi))

                # Konversi semua kolom ke dalam string sebelum menyimpan
                df = df.astype(str)

                # Simpan DataFrame yang telah diubah ke dalam file CSV
                np.savetxt("presensi_database.csv",df,delimiter=',',fmt='% s')
                print(f"\nData {masukkan_hapus_presensi} berhasil dihapus!\nData saat ini :\n\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}")
            else:
                input("Kesalahan input atau data tidak ada")
            input("Tekan [enter] untuk kembali ke Main Menu")
            main_page_admin()
        # FITUR 5.3 SELESAI

        else:
            main_page_admin()
    # FITUR 5 SELESAI

    elif menu_choice == '6':    # kembali ke login page
        launch_page_condition = True
        return
    # FITUR 6 SELESAI

    else:
        main_page_admin()    # salah input, kembali ke menu utama admin
    os.system('cls')
            
# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# HALAMAN UTAMA PEKERJA --------------------------------------------------------------------------------------------------------------------------------------

def main_page_employee():   # FITUR KARYAWAN
    os.system('cls')
    print(f'karyawan>menu utama\n=============== MENU UTAMA KARYAWAN ===============\nwaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n')    # mengucapkan selamat datang
    data_employee = []
    with open('employee_account_database.csv') as csvfile_employee:
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:
            data_employee.append(row)
    employee_column = [x[0] for x in data_employee]
    if launch_ID in employee_column:
        for x in range(0,len(data_employee)):
            if launch_ID == data_employee[x][0]:
                global tujuan
                tujuan = x
                print(f'Selamat Datang, karyawan "{data_employee[x][1]}"! Apa yang ingin anda lakukan saat ini?\n')
    data_presensi = []
    with open('presensi_database.csv') as csvfile_presensi:
        reader_presensi = csv.reader(csvfile_presensi)
        for row in reader_presensi:
            data_presensi.append(row)
    data_presensi_cond = []
    g=0
    with open('presensi_database.csv') as csvfile_presensi:
        reader_presensi = csv.reader(csvfile_presensi)
        for row in reader_presensi:
            data_presensi_cond.append(row)
            data_presensi_cond[g][-1] = ""
            g+=1
    print('\nMenu:\n[1] PRESENSI SEKARANG!\n[2] Lihat Jadwal Shift\n[3] Lihat Rekapitulasi Presensi\n[4] Lihat Data Presensi Anda\n[5] Informasi Mengenai Program\n[6] Keluar')
    menu_choice = input("Pilih menu : ")

    if menu_choice == '1':    # FITUR 1 PRESENSI SEKARANG
        os.system('cls')
        tanggal_presensi = datetime.datetime.now().strftime("%Y-%m-%d")
        repeat_menu_choice_1 = True
        while repeat_menu_choice_1 :
            os.system('cls')
            menu_choice_1 = input(f'karyawan>menu utama>presensi sekarang!\n=============== PRESENSI SEKARANG! ===============\nwaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\nPilih Shift:\n[1] Pagi\n[2] Siang\n[3] Malam\n[4] Kembali Ke Menu\nPilih menu : ')
            if menu_choice_1 == '1':            # FITUR 1.1 PRESENSI SEKARANG>SHIFT PAGI
                if data_employee[tujuan][3] == 'True':
                    repeat_menu_choice_1 = False
                    time_range = DateTimeRange("04:00:00", "05:00:00")
                    x = datetime.datetime.now().strftime("%H:%M:%S")
                    if x in DateTimeRange("04:00:00","23:59:59"):
                        if x in time_range :
                            status_kehadiran = "HADIR"
                        elif x in timeRangePagi:
                            status_kehadiran = "TERLAMBAT"
                        else :
                            status_kehadiran = "TIDAK HADIR"
                        data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1],'PAGI',status_kehadiran,now_time.strftime("%H:%M:%S")]
                        data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', 'PAGI', f'{status_kehadiran}', '']
                        if data_baru_cond not in data_presensi_cond:
                            # Menambahkan data baru ke dalam list data_presensi
                            data_presensi.append(data_baru)
                            # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                                writer_presensi = csv.writer(csvfile_presensi)
                                writer_presensi.writerows(data_presensi)
                            input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},PAGI,{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')
                        else:
                            input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},PAGI,{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
                    elif x in DateTimeRange("00:00:00", "03:59:59"):
                        input("\nPERHATIAN : Waku belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")
                else:
                    input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk melanjutkan")
                    repeat_menu_choice_1 = True
            # FITUR 1.1 SELESAI

            elif menu_choice_1 == '2':          # FITUR 1.2 PRESENSI SEKARANG>SHIFT SIANG
                if data_employee[tujuan][4] == 'True':
                    repeat_menu_choice_1 = False
                    time_range = DateTimeRange("10:00:00", "11:00:00")
                    x = datetime.datetime.now().strftime("%H:%M:%S")
                    if x in DateTimeRange("10:00:00","23:59:59"):
                        if x in time_range :
                            status_kehadiran = "HADIR"
                        elif x in timeRangeSiang:
                            status_kehadiran = "TERLAMBAT"
                        else :
                            status_kehadiran = "TIDAK HADIR"
                        data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1],'SIANG',status_kehadiran,now_time.strftime("%H:%M:%S")]
                        data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', 'SIANG', f'{status_kehadiran}', '']
                        if data_baru_cond not in data_presensi_cond:
                            # Menambahkan data baru ke dalam list data_presensi
                            data_presensi.append(data_baru)
                            # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                                writer_presensi = csv.writer(csvfile_presensi)
                                writer_presensi.writerows(data_presensi)
                            input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},SIANG,{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')
                        else:
                            input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},SIANG,{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
                    elif x in DateTimeRange("00:00:00", "09:59:59"):
                        input("\nPERHATIAN : Waku belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")
                else:
                    input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk melanjutkan")
                    repeat_menu_choice_1 = True
            # FITUR 1.2 SELESAI

            elif menu_choice_1 == '3':          # FITUR 1.3 PRESENSI SEKARANG>SHIFT MALAM
                if data_employee[tujuan][5] == 'True':
                    repeat_menu_choice_1 = False
                    time_range = DateTimeRange("16:00:00", "17:00:00")  

                    x = datetime.datetime.now().strftime("%H:%M:%S")
                    if x in DateTimeRange("16:00:00","23:59:59"):
                        if x in time_range :
                            status_kehadiran = "HADIR"
                        elif x in timeRangeMalam:
                            status_kehadiran = "TERLAMBAT"
                        else :
                            status_kehadiran = "TIDAK HADIR"
                        data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1],'MALAM',status_kehadiran,now_time.strftime("%H:%M:%S")]
                        data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', 'MALAM', f'{status_kehadiran}', '']
                        if data_baru_cond not in data_presensi_cond:
                            # Menambahkan data baru ke dalam list data_presensi
                            data_presensi.append(data_baru)
                            # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                                writer_presensi = csv.writer(csvfile_presensi)
                                writer_presensi.writerows(data_presensi)
                            input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},MALAM,{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')
                        else:
                            input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},MALAM,{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
                    elif x in DateTimeRange("00:00:00", "15:59:59"):
                        input("\nPERHATIAN : Waku belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")
                else:
                    input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk melanjutkan")
                    repeat_menu_choice_1 = True
            # FITUR 1.3 SELESAI

            elif menu_choice_1 == '4':          # FITUR 1.4 PRESENSI SEKARANG>KEMBALI KE MENU UTAMA
                repeat_menu_choice_1 = False
            # FITUR 1.4 SELESAI

            else:                               # SALAH INPUT, COBA LAGI
                repeat_menu_choice_1 = True

        main_page_employee()
    # FITUR 1 

    elif menu_choice == '2':  # FITUR 2 LIHAT JADWAL SHIFT ANDA
        os.system('cls')  # Membersihkan layar konsol
        print("karyawan>menu utama>lihat jadwal shift>\n=============== MENU LIHAT JADWAL SHIFT ANDA ===============\n")
        print("Shift anda minggu ini:\n")
        df = pd.DataFrame(data_employee,columns=kolom_employee)
        # Filter DataFrame berdasarkan ID yang sudah login
        filtered_df = df.loc[df['ID'] == launch_ID]
        if filtered_df.loc[0, 'Shift 1'] == 'True':
            print('"PAGI"\n04:00:00 - 10:00:00')
            if filtered_df.loc[0, 'Shift 2'] == 'True':
                print('"SIANG"\n10:00:00 - 16:00:00')
                if filtered_df.loc[0, 'Shift 3'] == 'True':
                    print('"MALAM"\n16:00:00 - 22:00:00')
            statShift = False
        elif filtered_df.loc[0, 'Shift 2'] == 'True':
            print('"SIANG"\n10:00:00 - 16:00:00')
            if filtered_df.loc[0, 'Shift 3'] == 'True':
                print('"MALAM"16:00:00 - 22:00:00')
            statShift = False
        elif filtered_df.loc[0, 'Shift 3'] == 'True':
            print('"MALAM"16:00:00 - 22:00:00')
            statShift = False

        if statShift == True:
            print('"TIDAK ADA"')
        input("\n\nTekan [enter] untuk kembali ke Main Menu")
        main_page_employee()
    # FITUR 2 SELESAI DAN UI

    elif menu_choice == '3':  # FITUR 3 REKAPITULASI PRESENSI
        ulangEmployee3 = True
        while ulangEmployee3:
            os.system('cls')
            print("karyawan>menu utama>rekapitulasi presensi>\n=============== MENU REKAPITULASI PRESENSI ===============")
            with open('presensi_database.csv', 'r') as presensi_file:
                data_presensi = presensi_file.readlines()

            # Membuat DataFrame Pandas dari data presensi
            df = pd.DataFrame([entry.strip().split(',') for entry in data_presensi], columns=kolom_presensi)

            # Filter DataFrame berdasarkan ID yang sudah login
            filtered_df = df.loc[df['ID'] == launch_ID]

            # Pilihan untuk rekap mingguan atau bulanan
            rekap_choice = input("\nPilih jenis rekapitulasi\n[1] Minggu Ini\n[2] Minggu Lalu\n[3] Bulan Ini\n[4] Bulan Lalu\n[5] Kembali ke menu utama\n\nMasukkan pilihan : ")

            now = datetime.datetime.now()

            if rekap_choice == '1':  # Minggu Ini
                rekap_choice_word = "minggu ini"
                ulangEmployee3 = False
                start_date = (now - timedelta(days=now.weekday())).strftime('%Y-%m-%d')
                end_date = (now + timedelta(days=(6 - now.weekday()))).strftime('%Y-%m-%d')
                total_days = 7

            elif rekap_choice == '2':  # Minggu Lalu
                rekap_choice_word = "minggu lalu"
                ulangEmployee3 = False
                start_date = (now - timedelta(days=(now.weekday() + 7))).strftime('%Y-%m-%d')
                end_date = (now - timedelta(days=now.weekday() + 1)).strftime('%Y-%m-%d')
                total_days = 7

            elif rekap_choice == '3':  # Bulan Ini
                rekap_choice_word = "bulan ini"
                ulangEmployee3 = False
                start_date = f'{now.year}-{now.month:02d}-01'
                last_day = calendar.monthrange(now.year, now.month)[1]
                end_date = f'{now.year}-{now.month:02d}-{last_day}'
                total_days = last_day

            elif rekap_choice == '4':  # Bulan Lalu
                rekap_choice_word = "bulan lalu"
                ulangEmployee3 = False
                last_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
                start_date = f'{last_month.year}-{last_month.month:02d}-01'
                last_day = calendar.monthrange(last_month.year, last_month.month)[1]
                end_date = f'{last_month.year}-{last_month.month:02d}-{last_day}'
                total_days = last_day
            elif rekap_choice == '5':
                input("\nTekan [enter] untuk kembali ke menu utama")
                main_page_employee()
            else:
                input('Pilihan yang anda berikan tidak ada!\nCoba lagi')
                ulangEmployee3 = True
        
        # Filter DataFrame berdasarkan tanggal
        filtered_df = filtered_df.loc[(filtered_df['Tanggal'] >= start_date) & (filtered_df['Tanggal'] <= end_date)]

        # Menghitung statistik kehadiran
        total_kehadiran_tepat_waktu = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'HADIR'])
        total_terlambat = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TERLAMBAT'])
        total_kehadiran = total_kehadiran_tepat_waktu + total_terlambat
        total_tidak_hadir = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TIDAK HADIR'])

        total_hari_kerja = total_kehadiran + total_tidak_hadir  # Total hari kerja dihitung berdasarkan jumlah data presensi

        # Menampilkan statistik kehadiran
        os.system('cls')
        print(f'karyawan>menu utama>rekapitulasi presensi>{rekap_choice_word}>\n=============== MENU REKAPITULASI PRESENSI ===============\n\nMenampilkan rekapitulasi "{rekap_choice_word.upper()}"\n{start_date} | {end_date}\n\n\nTOTAL HADIR : {total_kehadiran}')

        # Rincian Total Kehadiran
        print("    Rincian:")
        print(f"      -Total Hadir Tepat Waktu: {total_kehadiran_tepat_waktu}")
        print(f"      -Total Terlambat: {total_terlambat}")

        print(f"\nTOTAL TIDAK HADIR : {total_tidak_hadir}")

        # Persentase Kehadiran
        print(f"\nPERSENTASE KEHADIRAN: {total_kehadiran / total_days * 100:.2f}% dari 100%  ({total_kehadiran} dari {total_days} hari)")

        input("\n\n\nTekan [enter] untuk kembali ke Main Menu")
        main_page_employee()
    # FITUR 3 SELESAI DAN UI

    elif menu_choice == '4':  # FITUR 4 LIHAT DATA PRESENSI ANDA

        os.system('cls')  # Membersihkan layar konsol
        print("karyawan>menu utama>lihat data presensi anda\n=============== MENU LIHAT DATA PRESENSI ANDA ===============\n")
        with open('presensi_database.csv', 'r') as presensi_file:
            data_presensi = presensi_file.readlines()
        df = pd.DataFrame([entry.strip().split(',') for entry in data_presensi],columns=["Tanggal", "ID", "Nama", "Shift","kehadiran","Waktu"])
        
        filtered_df = df.loc[df['ID'] == launch_ID]
        rekap_choice = input("\nPilih jenis rekapitulasi\n[1] Minggu Ini\n[2] Minggu Lalu\n[3] Bulan Ini\n[4] Bulan Lalu\n[5] Lihat data keseluruhan\nSilahkan pilih menu : ")
        os.system('cls')
        now = datetime.datetime.now()

        if rekap_choice == '1':  # Minggu Ini
            rekap_choice_word = 'minggu Ini'
            start_date = (now - timedelta(days=now.weekday())).strftime('%Y-%m-%d')
            end_date = (now + timedelta(days=(6 - now.weekday()))).strftime('%Y-%m-%d')

        elif rekap_choice == '2':  # Minggu Lalu
            rekap_choice_word = 'minggu Lalu'
            start_date = (now - timedelta(days=(now.weekday() + 7))).strftime('%Y-%m-%d')
            end_date = (now - timedelta(days=now.weekday() + 1)).strftime('%Y-%m-%d')

        elif rekap_choice == '3':  # Bulan Ini
            rekap_choice_word = 'bulan Ini'
            start_date = f'{now.year}-{now.month:02d}-01'
            last_day = calendar.monthrange(now.year, now.month)[1]
            end_date = f'{now.year}-{now.month:02d}-{last_day}'

        elif rekap_choice == '4':  # Bulan Lalu
            rekap_choice_word = 'bulan Lalu'
            last_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
            start_date = f'{last_month.year}-{last_month.month:02d}-01'
            last_day = calendar.monthrange(last_month.year, last_month.month)[1]
            end_date = f'{last_month.year}-{last_month.month:02d}-{last_day}'
            
        elif rekap_choice == '5' :
            rekap_choice_word = 'semua'
            start_date = '...'
            end_date = '...'

        else :
            print("Input yang anda masukan salah")
            input("Tekan enter untuk kembali ke menu")
            main_page_employee()
        
        print(f'karyawan>menu utama>lihat data presensi anda>{rekap_choice_word}\n=============== MENU LIHAT DATA PRESENSI ANDA ===============\n\nMenampilkan data presensi "{rekap_choice_word.upper()}"\n{start_date} | {end_date}\n')
        if rekap_choice in '1234':
            filtered_df = filtered_df.loc[(filtered_df['Tanggal'] >= start_date) & (filtered_df['Tanggal'] <= end_date)]
            print(tabulate.tabulate(filtered_df, headers="keys", tablefmt="github", showindex=False))
        elif rekap_choice == '5':
            print (tabulate.tabulate(filtered_df, headers="keys", tablefmt="github", showindex=False))

        input("\nTekan [enter] untuk kembali ke Main Menu")
        main_page_employee()
    # FITUR 4 SELESAI DAN UI

    elif menu_choice == '5':  # FITUR 5 EULA
        os.system('cls')
        print(eula_text)
        input("\nTekan [enter] untuk kembali ke menu utama")
        main_page_employee()
    # FITUR 5 SELESAI DAN UI

    elif menu_choice == '6':  # FITUR 6 KELUAR
        launch_page_condition = True
        launchPage()
    # FITUR 6 SELESAI DAN UI

    else:       # BILA SALAH INPUT
        main_page_employee()
    os.system('cls')

# FITUR KARYAWAN 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# MEMBUKA FILE UNTUK PERTAMA KALINYA--------------------------------------------------------------------------------------------------------------------------

def akun_pertama():
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
        first_Account_pass   = str(input("Masukkan passkey anda : "))

        first_input = f"{first_account_ID.upper()},{first_account_nama.upper()},{first_account_posisi.upper()},{first_account_bidang.upper()},{first_Account_pass}"

        with open('admin_account_database.csv', 'w', newline='') as fileAdmincsv:
            admin_list = csv.DictWriter(fileAdmincsv, fieldnames=[first_input],  delimiter='/') 
            admin_list.writeheader()
# FITUR AKUN PERTAMA SELESAI

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# PERKOLOMAN DAN DESAIN---------------------------------------------------------------------------------------------------------------------------------------

kolom_admin = ['ID','Nama','Posisi','Bidang','Password']
kolom_employee = ['ID','Nama','Posisi','Shift 1','Shift 2','Shift 3','Password']
kolom_presensi = ["Tanggal", "ID", "Nama", "Shift", "Kehadiran", "Waktu"]

logoPart1 = (r"  _    _       _____                      ")
logoPart2 = (r" | |  | |     / ____|                     ")
logoPart3 = (r" | |  | |_ __| (___   ___ _ __   ___ ___  ")
logoPart4 = (r" | |  | | '_ \____ \ / _ \ '_ \ / __/ _ \ ")
logoPart5 = (r" | |__| | |_) |___) |  __/ | | | (_|  __/ ")
logoPart6 = (r"  \____/| .__/_____/ \___|_| |_|\___\___| ")
logoPart7 = (r"        | |                               ")
logoPart8 = (r"        |_|                               ")

logo = f'{logoPart1}\n{logoPart2}\n{logoPart3}\n{logoPart4}\n{logoPart5}\n{logoPart6}\n{logoPart7}\n{logoPart8}'
logoLaunch = f'++{'='*50}++\n||{' '*50}||\n||{' '*4}{logoPart1}{' '*4}||\n||{' '*4}{logoPart2}{' '*4}||\n||{' '*4}{logoPart3}{' '*4}||\n||{' '*4}{logoPart4}{' '*4}||\n||{' '*4}{logoPart5}{' '*4}||\n||{' '*4}{logoPart6}{' '*4}||\n||{' '*4}{logoPart7}{' '*4}||\n||{' '*4}{logoPart8}{' '*4}||\n||{' '*50}||\n||{' '*4}UpSence : Aplikasi Presensi Berbasis Python{' '*3}||\n||{' '*50}||\n||{' '*13}by ©Kelompok 2 TA Algo1{' '*14}||\n++{'='*50}++'
logoBorder = f'++{'='*86}++\n||{' '*22}{logoPart1}{' '*22}||\n||{' '*22}{logoPart2}{' '*22}||\n||{' '*22}{logoPart3}{' '*22}||\n||{' '*22}{logoPart4}{' '*22}||\n||{' '*22}{logoPart5}{' '*22}||\n||{' '*22}{logoPart6}{' '*22}||\n||{' '*22}{logoPart7}{' '*22}||\n||{' '*22}{logoPart8}{' '*22}||\n||{' '*86}||\n||{' '*27}Aplikasi Presensi Berbasis Python{' '*26}||\n++{'='*86}++'

launchInterface = f"+{'='*88}+\n|{' '*88}|\n|{' '*20}SELAMAT DATANG DI LAUNCH PAGE APLIKASI PRESENSI{' '*21}|\n|{' '*88}|\n+{'='*88}+\n"
loginInterface = f"+{'='*88}+\n|{' '*30}SELAMAT DATANG DI MENU LOGIN{' '*30}|\n|{' '*25}silahkan masukkan kredensial LOGIN anda{' '*24}|\n+{'='*88}+"

eula_text = f"""\n{logoBorder}

                            END USER LICENSE AGREEMENT (EULA)

Selamat datang di Program UpSence, program sistem presensi karyawan toko berbasis terminal.
UpSence dibuat menggunakan bahasa pemrograman Python.

Sebelum menggunakan Program UpSence harap baca ketentuan penggunaan program kami berikut: 
        
    1. Program ini hanya boleh digunakan oleh karyawan yang telah terdaftar dalam sistem.
    2. Dilarang menggunakan program ini untuk tujuan selain yang telah ditentukan.
    3. Setiap aktivitas yang direkam oleh pengguna dalam program berkaitan dengan
       pengguna yang bersangkutan menjadi tanggung jawab yang bersangkutan.
    4. Kami akan menyimpan data yang terkait dengan penggunaan program ini sesuai dengan
       kebijakan.
    5. DILARANG mengubah dan memodifikasi program ini kemudian mendistribusikannya
       tanpa seizin kami
    6. Pengguna bisa menggunakan Program ini pada perangkat komputer dengan sistem operasi
       Windows dan MacOS
    7. Jika program ini akan digunakan pada sistem operasi Mac, maka perlu mengubah
       perintah 'cls' menjadi 'clear'
        
Dengan melanjutkan, Anda menyetujui semua syarat dan ketentuan diatas.


        Setelah anda menyetujui ketentuan diatas, berikut adalah fitur UpSence:

-Fitur Admin
    1. Admin dapat menambah dan mengurangi pengguna yang dapat menggunakan program ini.
    2. Admin dapat melihat dan mengedit Data Karyawan dan Presensi Karyawan,
       kemudian bisa melihat rekap atas presensi tersebut.
        
-Fitur Karyawan
    1. Karyawan dapat melakukan presensi sesuai dengan ketentuan yang dibuat oleh admin
    2. Apabila Karyawan melakukan presensi diluar jam presensi namun masih di jam shift
       maka akan tercatat sebagai terlambat, namun apabila sudah keluar dari jam shift,
       maka akan tercatat sebagai tidak hadir.
    3. Karyawan dapat melakukan pengecekan terhadap presensinya sendiri,
       seperti shift dan rekapitulasi presensi miliknya sendiri.

-Informasi tambahan
    1. Pada menu rekapitulasi presensi terdapat fitur rekapitulasi,
       yang terdiri dari mingguan, bulanan, dan seluruh data presensi yang bisa dilihat.
    2. Karyawan hanya dapat melihat rekapitulasi presensinya sendiri,
       sedangkan Admin dapat melihat seluruh Presensi Karyawan.
        

                    Terima kasih telah menggunakan program UpSence


©Kelompok 2 TA Algo1
"""

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# PERWAKTUAN--------------------------------------------------------------------------------------------------------------------------------------------------

now_time = datetime.datetime.now()
waktuReal = now_time.strftime("\r%A, %d %B %Y | %H:%M:%S")
waktuRealTanggal = now_time.strftime("%Y-%m-%d")
waktuRealJam = now_time.strftime("%H:%M:%S")

timeRangePagi = DateTimeRange("04:00:00", "09:59:59")
timeRangeSiang = DateTimeRange("10:00:00", "15:59:59")
timeRangeMalam = DateTimeRange("16:00:00", "21:59:59")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# PERKALENDERAN-----------------------------------------------------------------------------------------------------------------------------------------------

def calculate_percentage(present_days, total_days):
    if total_days != 0:
        return present_days / total_days * 100
    else:
        return 0.0 #biar gak 0

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# EKSEKUSI----------------------------------------------------------------------------------------------------------------------------------------------------

akun_pertama()
launchPage()
