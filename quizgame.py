print("Selamat datang di Quiz Game")

bermain = input("Apakah kamu ingin bermain? (Main/tidak) ")

if bermain.lower() != "Main":
    quit()

print("Oke, mari kita mulai!")

jawaban = input("Siapa presiden indonesia sekarang ")
if jawaban == "Joko Widodo":
    print("Selamat, kamu benar!")
else:
    print("Maaf, kamu salah!")

jawaban = input("Siapa calon presiden Indonesia tahun 2024 nomor 1? ")
if jawaban == "Anies Baswedan":
    print("Selamat, kamu benar!")
else:
    print("Maaf, kamu salah!")

jawaban = input("Siapa calon presiden Indonesia tahun 2024 nomor 2? ")
if jawaban == "Prabowo Subianto":
    print("Selamat, kamu benar!")
else:
    print("Maaf, kamu salah!")

jawaban = input("Siapa calon presiden Indonesia tahun 2024 nomor 3? ")
if jawaban == "Ganjar Pranowo":
    print("Selamat, kamu benar!")
else:
    print("Maaf, kamu salah!")

