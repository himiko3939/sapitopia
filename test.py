import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil penjumlahan
def hitung_jumlah():
    try:
        angka1 = float(entry_angka1.get())
        angka2 = float(entry_angka2.get())
        hasil = angka1 + angka2
        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        messagebox.showerror("Input Error", "Mohon masukkan angka yang valid!")

# Membuat jendela utama
window = tk.Tk()
window.title("Penjumlahan Dua Angka")

# Menentukan ukuran jendela
window.geometry("300x200")

# Menambahkan label dan kotak input untuk angka pertama
label_angka1 = tk.Label(window, text="Angka Pertama:")
label_angka1.pack(pady=5)
entry_angka1 = tk.Entry(window)
entry_angka1.pack(pady=5)

# Menambahkan label dan kotak input untuk angka kedua
label_angka2 = tk.Label(window, text="Angka Kedua:")
label_angka2.pack(pady=5)
entry_angka2 = tk.Entry(window)
entry_angka2.pack(pady=5)

# Menambahkan tombol untuk menghitung
button_hitung = tk.Button(window, text="Hitung Jumlah", command=hitung_jumlah)
button_hitung.pack(pady=10)

# Menambahkan label untuk menampilkan hasil
label_hasil = tk.Label(window, text="Hasil: ")
label_hasil.pack(pady=5)

# Menjalankan aplikasi
window.mainloop()
