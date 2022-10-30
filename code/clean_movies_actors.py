import csv

DATA_LOC = "../data/"
SEP = ","

rels_file = open(DATA_LOC + "d-movies_actors.csv")
movies_file = open(DATA_LOC + "d-movies.csv")
actors_file = open(DATA_LOC + "d-actors.csv")

rels = rels_file.readlines()[1:]
movies = movies_file.readlines()[1:]
actors = actors_file.readlines()[1:]

rels_file.close()
movies_file.close()
actors_file.close()
data = []
for rel in rels:
    movie_id, actor_id = rel.split(sep=SEP)
    movie_id = int(movie_id) - 2
    actor_id = int(actor_id) - 2

    movie = movies[movie_id].split(sep=SEP)[1]
    actor = actors[actor_id].split(sep=SEP)[1]
    
    data.append([movie,actor[:len(actor)-1]])
    
fixed_rels = open(DATA_LOC + "cast_rels.csv","w",newline='', encoding='utf-8')

rels_file = csv.writer(fixed_rels)
rels_file.writerow(["movie","actor"])
rels_file.writerows(data)

fixed_rels.close()    