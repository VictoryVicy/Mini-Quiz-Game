import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.label_welcome = tk.Label(master, text="Selamat datang di Mini Quiz Game", font=("Helvetica", 14))
        self.label_welcome.pack(pady=10)

        self.label_main = tk.Label(master, text="Apakah kamu ingin bermain? (Main/Tidak)", font=("Helvetica", 12))
        self.label_main.pack(pady=5)

        self.entry_main = tk.Entry(master)
        self.entry_main.pack()

        self.button_start = tk.Button(master, text="Mulai", command=self.mulai_game)
        self.button_start.pack(pady=10)

        self.pertanyaan = [
            ("Siapa presiden Indonesia sekarang?", "joko widodo"),
            ("Siapa calon presiden Indonesia tahun 2024 nomor 1?", "anies baswedan"),
            ("Siapa calon presiden Indonesia tahun 2024 nomor 2?", "prabowo subianto"),
            ("Siapa calon presiden Indonesia tahun 2024 nomor 3?", "ganjar pranowo"),
        ]

        self.index_pertanyaan = 0

    def cek_jawaban(self):
        jawaban = self.entry_main.get().strip().lower()
        pertanyaan, jawaban_benar = self.pertanyaan[self.index_pertanyaan]

        if jawaban == jawaban_benar:
            messagebox.showinfo("Jawaban Benar", "Selamat, kamu benar!")
        else:
            messagebox.showerror("Jawaban Salah", "Maaf, kamu salah!")

        self.index_pertanyaan += 1

        if self.index_pertanyaan < len(self.pertanyaan):
            self.tampilkan_pertanyaan()
        else:
            self.tampilkan_skor()

    def mulai_game(self):
        bermain = self.entry_main.get().strip().lower()
        if bermain == "main":
            self.button_start.destroy()
            self.tampilkan_pertanyaan()

        else:
            messagebox.showerror("Keluar quiz", "Baiklah sampai berjumpa lain waktu")
            self.master.destroy()

    def tampilkan_pertanyaan(self):
        if hasattr(self, 'entry_main'):
            self.entry_main.destroy()
            del self.entry_main
        if hasattr(self, 'button_next'):
            self.button_next.destroy()
            del self.button_next

        pertanyaan, _ = self.pertanyaan[self.index_pertanyaan]
        self.label_main.config(text=pertanyaan)
        self.entry_main = tk.Entry(self.master)
        self.entry_main.pack()
        self.button_next = tk.Button(self.master, text="Selanjutnya", command=self.cek_jawaban)
        self.button_next.pack(pady=10)

    def tampilkan_skor(self):
        messagebox.showinfo("Skor Akhir", "Anda telah menyelesaikan " + str(self.index_pertanyaan) + " pertanyaan dengan benar")
        messagebox.showinfo("Skor Akhir", "Kemampuan anda dalam menjawab quiz = " + str((self.index_pertanyaan / len(self.pertanyaan)) * 100) + "%.")
        self.master.destroy()

root = tk.Tk()
app = QuizApp(root)

root.mainloop()