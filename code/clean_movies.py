import csv

DATA_LOC = "../data/"
SEP = ","

movies_file = open(DATA_LOC + "d-movies.csv")
genres_file = open(DATA_LOC + "d-genres.csv")

movies = csv.reader(movies_file)
genres = genres_file.readlines()[1:]

genres_file.close()

#make template
genre_list = []
for genre in genres:
    genre = genre.split(sep=SEP)[0]
    genre_list.append(genre)

movie_data = []
headers = []
for movie in movies:
    title = movie[1]
    if title == "title":
        headers.append(title)
    else:
        genre_weight = movie[2]
        genre_weight = genre_weight[1:len(genre_weight)-1]
        genre_weight = genre_weight.split(sep=SEP)
        data = [title] + genre_weight
        movie_data.append(data)

movies_file.close()

headers = headers + genre_list

movies_file = open(DATA_LOC + "movies_fixed.csv","w",newline='', encoding='utf-8')
movies = csv.writer(movies_file)
movies.writerow(headers)
movies.writerows(movie_data)
movies_file.close()