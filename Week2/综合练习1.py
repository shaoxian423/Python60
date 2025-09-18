import json
import os
from datetime import datetime

FILE_NAME = "movies.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        movies = json.load(f)
else:
    movies = []


def save_movies():
    with open(FILE_NAME, "W")as f:
        json.dump(movies, f, indent=4, ensure_ascii=False)


def valid_date(year_str):
    current_year = datetime.now().year
    if not year_str.isdigit():
        return False, "year must be a number"
    year = int(year_str)
    if year < 1888 or year > current_year:
        s
