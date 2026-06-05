listFilm = [
  {
    "judul" : "The Doom",
    "genre" : "Horror",
    "rating" : 8.30,
    "tahun" : 2018
  },
  {
    "judul" : "Spiderman",
    "genre" : "Adventure",
    "rating" : 9.52,
    "tahun" : 2020
  },
  {
    "judul" : "Z Town",
    "genre" : "Zombie",
    "rating" : 7.53,
    "tahun" : 2008
  },
  ]

def tampilkan_film(data) :
  for film in data :
    print("="*30)
    print(f"Judul : {film["judul"]}")
    print(f"Genre : {film["genre"]}")
    print(f"Rating : {film["rating"]}")
    print(f"Tahun : {film["tahun"]}")
    print("="*30)

def film_terbaik(data):
  rating_tertinggi = data[0]
  for film in data :
    if film["rating"] > rating_tertinggi["rating"] :
      rating_tertinggi = film
  return rating_tertinggi

def cari_genre(data) :
  pilihanGenre = input("Pilih Genre : ")
  ketemu = False
  for film in data :
    if film["genre"] == pilihanGenre :
      ketemu = True
      print(f"Film dengan genre {film["genre"]}, adalah : {film["judul"]}")

  if not ketemu :
      print("tidak ada film dengan genre tersebut")

print("="*30)
print("----Data film----")
print("="*30)
tampilkan_film(listFilm)
rating_tertinggi = film_terbaik(listFilm)
print(f"Film dengan rating tertinggi adalah :{rating_tertinggi["judul"]}")
print(f"Ratingnya adalah : {rating_tertinggi["rating"]}")
print("="*30)
cari_genre(listFilm)
print("="*30)


  