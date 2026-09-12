# MiniProject1_DDP_Rakhmat Nur Alif Abdillah

Nama : RAKHMAT NUR ALIF ABDIILAH <br>
NIM : 2609116100

# FLOWCHART Sistem Pendataan Unit Kerja Dokter & Perawat
<img width="758" height="1197" alt="Flowchart MiniProjectDDP3 drawio" src="https://github.com/user-attachments/assets/2be0b9f9-49a2-46a1-a9c2-c5c9402be23f" />

- Flowchart ini menggambarkan alur kerja sistem pendataan dokter dan perawat. Program dimulai dengan menampilkan menu, kemudian pengguna memilih proses yang diinginkan. Setiap pilihan memiliki proses yang berbeda, yaitu tambah, tampil, ubah, dan hapus data. Setelah proses selesai, program kembali ke menu utama. Jika pengguna memilih keluar, maka program akan berhenti.

# INPUT & OUTPUT
<img width="1366" height="728" alt="● MINI_PROJECT1_DDP py - Downloads - Visual Studio Code 9_12_2026 10_53_19 AM" src="https://github.com/user-attachments/assets/131dca81-7235-41b0-bac7-0397744bfc5d" />

- Pada gambar pertama, program dimulai dengan membuat sebuah list kosong yaitu list data []. Ini digunakan sebagai tempat penyimpanan data. while True digunakan agar menu terus berjalan. Pengguna dapat memilih 5 menu. Pada menu Tambah Data, pengguna memasukkan nama, profesi, dan unit kerja. Data kemudian disimpan ke dalam list menggunakan append().

<img width="1366" height="728" alt="● MINI_PROJECT1_DDP py - Downloads - Visual Studio Code 9_12_2026 10_55_21 AM" src="https://github.com/user-attachments/assets/61672ec0-7605-4959-85d6-b621f7307d1a" />

- Pada menu Tampilkan Data, program mengecek jumlah data menggunakan len(data). Jika data tersedia, data ditampilkan menggunakan for dan enumerate() sehingga setiap data memiliki nomor.
- Pada menu Ubah Data, pengguna memilih nomor data yang ingin diubah. Setelah itu memasukkan nama, profesi, dan unit kerja yang baru. Data lama kemudian diganti dengan data baru menggunakan data[nomor - 1].

<img width="1366" height="728" alt="● MINI_PROJECT1_DDP py - Downloads - Visual Studio Code 9_12_2026 10_55_34 AM" 
  src="https://github.com/user-attachments/assets/ce58d376-cf36-4576-908a-62a1f648a3a6" />
  
- Pada menu Hapus Data, program menampilkan data terlebih dahulu, kemudian pengguna memilih nomor data yang ingin dihapus. Data dihapus menggunakan pop(nomor - 1).
- Pada  menu Keluar, program menampilkan "Program Selesai". lalu menggunakan break untuk menghentikan while True. Jika pengguna memasukkan pilihan selain 1-5, program menampilkan "Pilihan menu tidak tersedia".

<img width="1366" height="728" alt="● MINI_PROJECT1_DDP py - Downloads - Visual Studio Code 9_12_2026 10_51_50 AM" src="https://github.com/user-attachments/assets/b28553c6-1fdb-4ac8-b784-8d38a074b51c" />

<img width="1366" height="728" alt="● MINI_PROJECT1_DDP py - Downloads - Visual Studio Code 9_12_2026 10_52_27 AM" src="https://github.com/user-attachments/assets/3a1c6773-2bdf-45ec-8100-ccfee703189f" />

<img width="1366" height="728" alt="● MINI_PROJECT1_DDP py - Downloads - Visual Studio Code 9_12_2026 10_52_37 AM" src="https://github.com/user-attachments/assets/899813e5-3c83-43d8-ba54-d4b7fcb534e6" />

- BERIKUT ADALAH CONTOH OUTPUTNYA.
