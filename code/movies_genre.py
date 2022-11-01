import csv

DATA_LOC = "../data/"
SEP = ","

movies_file = open(DATA_LOC + "d-movies.csv")
genres_file = open(DATA_LOC + "d-genres.csv")

movies = csv.reader(movies_file)
genres = genres_file.readlines()[1:]

genres_file.close()

output = dict()
#make template
genre_list = []
for genre in genres:
    genre = genre.split(sep=SEP)[0]
    output[genre] = []

movie_data = []
for movie in movies:
    title = movie[1]
    if title == "title":
        continue
    genre_weight = movie[2]
    genre_weight = genre_weight[1:len(genre_weight)-1]
    genre_weight = genre_weight.split(sep=SEP)
    for genre in genre_weight:
        if genre > 0:
            output[genre].append(title)

movies_file.close()

movies_file = open(DATA_LOC + "movies_fixed.csv","w",newline='', encoding='utf-8')
movies = csv.writer(movies_file)
movies.writerow(genre_list)

movies.writerows(movie_data)
movies_file.close()