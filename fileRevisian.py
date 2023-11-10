import csv                  # import csv
import os                   # agar bisa clean terminal
import pandas as pd         # import pandas
import numpy as np          # import numpy
from pathlib import Path    # import modul path


# HALAMAN LOGIN DAN LAUNCH PAGE ------------------------------------------------------------------------------------------------------------------------------
def launchPage():
    launch_page_condition = True
    while launch_page_condition:

        os.system('cls')
        print("=============== WELCOME TO LAUNCH PAGE ===============")
        launch_menu = input("Press [enter] to login, Press [Q] to quit the app : ")
        if launch_menu == '':
            os.system('cls')
            print("=============== WELCOME TO LOGIN PAGE ===============")
            global launch_ID
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


# HALAMAN UTAMA ADMIN ----------------------------------------------------------------------------------------------------------------------------------------

def main_page_admin():
    os.system('cls')
    print('admin>menu utama\n=============== ADMIN MENU ===============')    # mengucapkan selamat datang

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
                print(f'Selamat Datang, admin "{data_admin[x][1]}"!\n')
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
                masukan_tambah_admin = [masukkanAdminID.upper(),masukkanAdminNama.upper(),masukkanAdminPosisi.upper(),masukkanAdminBidang.upper()]
                # Menambahkan data baru ke dalam list data admin
                data_admin.append(masukan_tambah_admin)
                # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                with open('admin_account_database.csv', 'w', newline='') as csvfile_admin:
                    writer_admin = csv.writer(csvfile_admin)
                    writer_admin.writerows(data_admin)
                input(f'\nData baru : {masukkanAdminID.upper()},{masukkanAdminNama.upper()},{masukkanAdminPosisi.upper()},{masukkanAdminBidang.upper()}\nPERHATIAN : Data admin berhasil ditambahkan!\n\nTekan [enter] untuk kembali ke menu utama')
            else:
                input(f'\nPERHATIAN : Data admin "{masukkanAdminID}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
            main_page_admin()
        # FITUR 1.1 SELESAI

        elif menu_choice_1 == '2':  # FITUR 1.2 TAMBAHKAN ORANG>TAMBAHKAN KARYAWAN
            os.system('cls')
            print("admin>menu utama>tambahkan orang>tambahkan karyawam\n=============== MENU TAMBAHKAN KARYAWAN ===============\n")
            masukkanKaryawanID = input("Masukkan ID karyawan : ")
            if masukkanKaryawanID not in employee_column :
                masukkanKaryawanNama = input("Masukkan nama karyawan : ")
                masukkanKaryawanPosisi = input("Masukkan posisi karyawan : ")
                masukkanKaryawanShift1 = input("Masukkan apakah karyawan bertugas Shift 1 (True/False) : ")
                masukkanKaryawanShift2 = input("Masukkan apakah karyawan bertugas Shift 2 (True/False) : ")
                masukkanKaryawanShift3 = input("Masukkan apakah karyawan bertugas Shift 3 (True/False) : ")
                masukan_tambah_karyawan = [masukkanKaryawanID.upper(),masukkanKaryawanNama.upper(),masukkanKaryawanPosisi.upper(),masukkanKaryawanShift1.capitalize(),masukkanKaryawanShift2.capitalize(),masukkanKaryawanShift3.capitalize()]
                # Menambahkan data baru ke dalam list data karyawan
                data_employee.append(masukan_tambah_karyawan)
                # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                with open('employee_account_database.csv', 'w', newline='') as csvfile_employee:
                    writer_employee = csv.writer(csvfile_employee)
                    writer_employee.writerows(data_employee)
                input(f'\nData baru : {masukkanKaryawanID.upper()},{masukkanKaryawanNama.upper()},{masukkanKaryawanPosisi.upper()},{masukkanKaryawanShift1.capitalize()},{masukkanKaryawanShift2.capitalize()},{masukkanKaryawanShift3.capitalize()}\nPERHATIAN : Data karyawan berhasil ditambahkan!\n\nTekan [enter] untuk kembali ke menu utama')
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
            masukan_edit_admin = input(f"admin>menu utama>edit data>edit data admin\n=============== MENU EDIT DATA ADMIN ===============\ndata saat ini:\n\n{df}\n\nMasukkan ID admin yang hendak diubah : ")
            if masukan_edit_admin in df['ID'].values:
                baris_admin = df[df['ID'] == masukan_edit_admin]  # Menemukan baris yang sesuai dengan ID
                print(f"\nData yang akan diedit : \n{baris_admin.to_string(index=False, header=False)}\n")
                IDBaru     = input("Masukkan ID baru: ")
                namaBaru   = input("Masukkan nama baru: ")
                posisiBaru = input("Masukkan posisi baru: ")
                bidangBaru = input("Masukkan bidang baru: ")
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
                np.savetxt('admin_account_database.csv',df,delimiter=',',fmt='%s')
                print(f'\nData baru "{masukan_edit_admin}" telah diubah!\n\nData saat ini :\n{df}\n')
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
            masukan_edit_employee = input(f"admin>menu utama>edit data>edit data karyawan\n=============== MENU EDIT DATA KARYAWAN ===============\n\n{df}\n\nMasukkan ID karyawan yang hendak diubah : ")
            if masukan_edit_employee in df['ID'].values:
                baris_employee = df[df['ID'] == masukan_edit_employee]  # Menemukan baris yang sesuai dengan ID
                edit_employee_profil = input(f"\nData yang akan diedit : \n{baris_employee.to_string(index=False, header=False)}\n\nPilih [1] untuk mengedit data profil karyawan atau [2] untuk mengubah shift karyawan : ")
                if edit_employee_profil == '1':     # FITUR 2.2.1 EDIT DATA>EDIT DATA KARYAWAN>EDIT DATA PROFIL
                    IDBaru = input("Masukkan ID baru: ")
                    namaBaru = input("Masukkan nama baru: ")
                    posisiBaru = input("Masukkan posisi baru: ")
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
                    np.savetxt('employee_account_database.csv',df,delimiter=',',fmt='%s')
                    print(f'\nData baru untuk "{df.iloc[baris_employee.index, 0:3].to_string(header=False,index=False)}" telah diubah!\n\nData saat ini :\n{df}\n')
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
                    print(f'\nData baru untuk "{df.iloc[baris_employee.index, 0:3].to_string(header=False,index=False)}" telah diubah!\n\nData saat ini :\n{df}\n')
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
        masukan_edit_presensi_tanggal = input("Masukkan tanggal yang dicari : ")
        print()
        if masukan_edit_presensi_id in df['ID'].values:     
            filtered_df = df.loc[df['ID'].str.contains(masukan_edit_presensi_id)]
            filtered_df = filtered_df.loc[df['Tanggal'].str.contains(masukan_edit_presensi_tanggal)]        
            print(filtered_df)
            masukan_edit_presensi_index = int(input("pilih index yang akan diedit: "))
            print(f"\nData yang akan diedit : \n{df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]}\nTekan [enter] untuk melewati perubahan\n")
            masukanEditPresensiTanggalBaru = input("Masukkan tanggal baru : ")  
            masukanEditPresensiIDBaru = input("Masukkan ID baru : ")
            masukanEditPresensiNamaBaru = input("Masukkan Nama baru : ") 
            masukanEditPresensiShiftBaru = input("Masukkan Shift baru : ") 
            if masukanEditPresensiTanggalBaru == '':
                pass
            else:
                df.iloc[masukan_edit_presensi_index, 0] = masukanEditPresensiTanggalBaru
            if masukanEditPresensiIDBaru == '':
                pass
            else:
                df.iloc[masukan_edit_presensi_index, 1] = masukanEditPresensiIDBaru
            if masukanEditPresensiNamaBaru == '':
                pass
            else:
                df.iloc[masukan_edit_presensi_index, 2] = masukanEditPresensiNamaBaru
            if masukanEditPresensiShiftBaru == '':
                pass
            else:
                df.iloc[masukan_edit_presensi_index, 3] = masukanEditPresensiShiftBaru
            np.savetxt('presensi_database.csv',df,delimiter=',',fmt='%s')
            print(f'\nData baru "{masukan_edit_presensi_id}" telah diubah!\n\nData saat ini :\n{df}\n')
        else:
            print(f"{masukan_edit_presensi_id} tidak ada dalam database.")
 
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
            input("Press [enter] to back to Main Menu")  # back to main menu
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
            os.system('cls')
            print("admin>menu utama>hapus presensi karyawan>\n=============== MENU HAPUS PRESENSI KARYAWAN ===============\nmenampilkan keseluruhan data...\n")
            data_presensi = []
            with open('presensi_database.csv') as csvfile_presensi:
                reader_presensi = csv.reader(csvfile_presensi)
                for row in reader_presensi:
                    data_presensi.append(row)
            df = pd.DataFrame(data_presensi, columns=kolom_presensi)
            print(df)
            masukkan_tanggal_presensi = str(input("\nMasukkan tanggal yang dicari :"))

            filtered_df = df.loc[df['Tanggal'].str.contains(masukkan_tanggal_presensi)]        
            print(filtered_df)

            masukkan_hapus_presensi = input("\nMasukkan index yang hendak dihapus : ")
            if int(masukkan_hapus_presensi) in range(len(df)):
                df = df.drop(int(masukkan_hapus_presensi))
                np.savetxt("presensi_database.csv",df,delimiter=',',fmt='% s')
                print(f"\nData {masukkan_hapus_presensi} berhasil dihapus!\nData saat ini :\n\n{df}")
            else:
                input("Kesalahan input atau data tidak ada")
            input("Tekan [enter] untuk kembali ke Main Menu")
        else:
            main_page_admin()

    elif menu_choice == '6':    # kembali ke login page
        launch_page_condition = True
        return

    else:
        main_page_admin()    # salah input, kembali ke menu utama admin
    os.system('cls')
            
# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# HALAMAN UTAMA PEKERJA --------------------------------------------------------------------------------------------------------------------------------------

def main_page_employee():
    os.system('cls')
    print('karyawan>menu utama\n=============== EMPLOYEE MENU ===============')    # mengucapkan selamat datang
    data_employee = []
    with open('employee_account_database.csv') as csvfile_employee:
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:
            data_employee.append(row)
    employee_column = [x[0] for x in data_employee]
    if launch_ID in employee_column:
        for x in range(0,len(data_employee)):
            if launch_ID == data_employee[x][0]:
                tujuan = x
                print(f'Selamat Datang, karyawan "{data_employee[x][1]}"!\n')
    data_presensi = []
    with open('presensi_database.csv') as csvfile_presensi:
        reader_presensi = csv.reader(csvfile_presensi)
        for row in reader_presensi:
            data_presensi.append(row)
    print('\nMenu:\n[1] PRESENSI SEKARANG!\n[2] Lihat Jadwal Shift\n[3] Lihat Rekapitulasi Presensi\n[4] Lihat Data Presensi Anda\n[5] Informasi Mengenai Shift\n[6] Keluar')
    menu_choice = input("Pilih menu : ")

    if menu_choice == '1':    # FITUR 1 PRESENSI SEKARANG
        tanggal_presensi = input("\nMasukkan Tanggal Hari Ini [yyyy-mm-dd] : ")
        repeat_menu_choice_1 = True
        while repeat_menu_choice_1 :
            
            menu_choice_1 = input("\nPilih Shift:\n[1] Pagi\n[2] Siang\n[3] Malam\n[4] Kembali Ke Menu\nPilih menu : ")
            if menu_choice_1 == '1':            # FITUR 1.1 PRESENSI SEKARANG>SHIFT PAGI
                repeat_menu_choice_1 = False
                data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1],'PAGI','HADIR']
                if data_baru not in data_presensi:
                    # Menambahkan data baru ke dalam list data_presensi
                    data_presensi.append(data_baru)
                    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                    with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                        writer_presensi = csv.writer(csvfile_presensi)
                        writer_presensi.writerows(data_presensi)
                    input(f'\nPresensi : {tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},PAGI,HADIR\nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')
                else:
                    input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},PAGI,HADIR" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
            elif menu_choice_1 == '2':          # FITUR 1.2 PRESENSI SEKARANG>SHIFT SIANG
                repeat_menu_choice_1 = False
                data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1], 'SIANG','HADIR']
                if data_baru not in data_presensi:
                    # Menambahkan data baru ke dalam list data_presensi
                    data_presensi.append(data_baru)
                    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                    with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                        writer_presensi = csv.writer(csvfile_presensi)
                        writer_presensi.writerows(data_presensi)
                    input(f'\nPresensi : {tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},SIANG,HADIR"\nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')
                else:
                    input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},SIANG,HADIR" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
            elif menu_choice_1 == '3':          # FITUR 1.3 PRESENSI SEKARANG>SHIFT MALAM
                repeat_menu_choice_1 = False
                data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1], 'MALAM','HADIR']
                if data_baru not in data_presensi:
                    # Menambahkan data baru ke dalam list data_presensi
                    data_presensi.append(data_baru)
                    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                    with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                        writer_presensi = csv.writer(csvfile_presensi)
                        writer_presensi.writerows(data_presensi)
                    input(f'\nPresensi : {tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},MALAM,HADIR"\nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')
                else:
                    input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},MALAM,HADIR" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')
            elif menu_choice_1 == '4':          # FITUR 1.4 PRESENSI SEKARANG>KEMBALI KE MENU UTAMA
                repeat_menu_choice_1 = False
            else:                               # SALAH INPUT, COBA LAGI
                repeat_menu_choice_1 = True

            main_page_employee()
    # FITUR 1 SELESAI

    elif menu_choice == '2':

        os.system('cls')  # Membersihkan layar konsol
        # print("karyawan>menu utama>lihat jadwal shift\n=============== MENU LIHAT JADWAL SHIFT ANDA ===============")
        # # Baca jadwal shift dari file atau sumber data lainnya
        # with open('presensi_database.csv', 'r') as jadwal_file:
        #     jadwal_shift = jadwal_file.read()
        #  # Cetak jadwal shift ke layar
        # print("Jadwal Shift Karyawan:")
        # print(jadwal_shift)

        input(print("Press anykey to continue"))
        main_page_employee()

    elif menu_choice == '3':

        # os.system('cls')
        # with open('presensi_database.csv', 'r') as presensi_file:
        #     data_presensi = presensi_file.readlines()

        # total_kehadiran = len(data_presensi)
        # total_hari_kerja = total_kehadiran  # Total hari kerja dihitung berdasarkan jumlah data presensi

        # persentase_kehadiran = (total_kehadiran / total_hari_kerja) * 100

        # print('\n================ REKAPITULASI ABSENSI ================')

        # # Membuat DataFrame Pandas dari data presensi
        # df = pd.DataFrame([entry.strip().split(',') for entry in data_presensi],
        # columns=["Tanggal", "ID", "Nama", "Shift"])

        # # Filter DataFrame berdasarkan ID yang sudah login
        # filtered_df = df.loc[df['ID'] == launch_ID]

        # # Menampilkan DataFrame yang sudah difilter sebagai tabel
        # print(filtered_df)

        # print(f"Total Kehadiran: {len(filtered_df)}")
        # print(f"Persentase Kehadiran: {persentase_kehadiran:.2f}%")

        input("Press any key to continue")
        main_page_employee()

    elif menu_choice == '5':
        os.system('cls')
        eula_text = """
    End User License Agreement (EULA)
    
    Terima kasih telah menggunakan program kami.
    Mohon baca dan pahami syarat-syarat berikut sebelum melanjutkan:
    
    1. Program ini hanya boleh digunakan oleh karyawan yang sah dan telah terdaftar dalam sistem kami.
    2. Penggunaan program ini untuk tujuan selain yang telah ditentukan dilarang.
    3. Setiap aktivitas yang terekam dalam program berkaitan dengan pengguna yang bersangkutan akan menjadi tanggung jawab yang bersangkutan.
    4. Kami akan menyimpan data yang terkait dengan penggunaan program ini sesuai dengan kebijakan kami.

    Tata Cara Pemakaian Admin:
    a. Masukkan ID admin dan password pada halaman login admin.
    b. Pilih menu yang sesuai dengan tugas admin (tambah karyawan, hapus karyawan, lihat rekap presensi, dll.)
    
    Tata Cara Pemakaian Karyawan:
    a. Masukkan ID karyawan dan password pada halaman login.
    b. Pilih menu yang diinginkan untuk melanjutkan (presensi, lihat jadwal, lihat rekap absensi, dll.).

    
    Dengan melanjutkan, Anda menyetujui semua syarat dan ketentuan diatas."""
        
        print(eula_text)
        input("\nTekan [enter] untuk kembali ke menu utama")
        main_page_employee()
    
    elif menu_choice == '6':        # kembali ke login page
        launch_page_condition =True
        launchPage()

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

kolom_admin = ['ID','Nama','Posisi','Bidang']
kolom_employee = ['ID','Nama','Posisi','Shift 1','Shift 2','Shift 3']
kolom_presensi = ['Tanggal','ID', 'Nama','Shift','kehadiran']

launchPage()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
