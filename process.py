import csv
import pandas as pd

def process_genre(param):
    param.strip("\n")
    genres = []
    temp = param.split(",")
    for t in temp:
        genres.append(t.lower())
    return genres


tsv_file = open("title.akas.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
set_us_titles = set()
for row in read_tsv:
    if row[3] == "US":
        set_us_titles.add(row[0])
print(len(set_us_titles))
movies = []
tsv_file = open("title.basics.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")

for row in read_tsv:
    if row[0] in set_us_titles and row[1] == "movie" and row[8] != "\\N":
        movies.append([row[2], process_genre(row[8])])
print(len(movies))
print(movies[:15])

df = pd.DataFrame(movies)
df.columns = ["movie_name","genres"]
df.to_csv('output.csv', index=False,)