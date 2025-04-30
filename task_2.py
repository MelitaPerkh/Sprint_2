class Movies:
    def __init__(self):
        self.movies = []
    
    def add_movies(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def __init__(self):
        super().__init__()

    def add_movies(self, movie):
        super().add_movies(movie)
        return f"Комедии: {self.movies}"
    
class Drama(Movies):
    def __init__(self):
        super().__init__()

    def add_movies(self, movie):
        super().add_movies(movie)
        return f"Драмы: {self.movies}"
    

comedy = Comedy()
print(comedy.add_movies('Большой куш'))

drama = Drama()
print(drama.add_movies('Оружейный барон'))