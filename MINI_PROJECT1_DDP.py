data = []

while True:
    print("\nSISTEM PENDATAAN DOKTER & PERAWAT")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama: ")
        profesi = input("Profesi (Dokter/Perawat): ")
        unit = input("Unit Kerja: ")

        data.append((nama, profesi, unit))
        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        if len(data) == 0:
            print("Belum ada data.")
        else:
            print("\nDATA DOKTER & PERAWAT")
            for i, item in enumerate(data, 1):
                print(i, ".", item[0], "-", item[1], "-", item[2])

    elif pilihan == "3":
        if len(data) == 0:
            print("Belum ada data.")
        else:
            for i, item in enumerate(data, 1):
                print(i, ".", item[0], "-", item[1], "-", item[2])

            nomor = int(input("Nomor data yang ingin diubah: "))

            if 1 <= nomor <= len(data):
                nama = input("Nama baru: ")
                profesi = input("Profesi baru: ")
                unit = input("Unit kerja baru: ")

                data[nomor - 1] = (nama, profesi, unit)
                print("Data berhasil diubah.")
            else:
                print("Nomor data tidak ditemukan.")

    elif pilihan == "4":
        if len(data) == 0:
            print("Belum ada data.")
        else:
            for i, item in enumerate(data, 1):
                print(i, ".", item[0], "-", item[1], "-", item[2])

            nomor = int(input("Nomor data yang ingin dihapus: "))

            if 1 <= nomor <= len(data):
                data.pop(nomor - 1)
                print("Data berhasil dihapus.")
            else:
                print("Nomor data tidak ditemukan.")

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan menu tidak tersedia.")