print("Selamat datang di Quiz Game")

bermain = input("Apakah kamu ingin bermain? (main/tidak/mungkin) ")

if bermain.lower() != "main":
    quit()

print("Oke, mari kita mulai!")
skor = 0

jawaban = input("Siapa presiden indonesia sekarang? ")
if jawaban.lower() == "joko widodo":
    print("Selamat, kamu benar!")
    skor += 1
else:
    print("Maaf, kamu salah!")

jawaban = input("Siapa calon presiden Indonesia tahun 2024 nomor 1? ")
if jawaban.lower() == "anies baswedan":
    print("Selamat, kamu benar!")
    skor += 1
else:
    print("Maaf, kamu salah!")

jawaban = input("Siapa calon presiden Indonesia tahun 2024 nomor 2? ")
if jawaban.lower() == "prabowo subianto":
    print("Selamat, kamu benar!")
    skor += 1
else:
    print("Maaf, kamu salah!")

jawaban = input("Siapa calon presiden Indonesia tahun 2024 nomor 3? ")
if jawaban.lower() == "ganjar pranowo":
    print("Selamat, kamu benar!")
    skor += 1
else:
    print("Maaf, kamu salah!")

print("Kamu menjawab " + str(skor) + " pertanyaan dengan benar")
print("Kemampuan dalam menjawab quiz = " + str((skor / 4) * 100) + " %.")

