'''Task 3: Favorite Movies Collection (Medium)'''
movies = (
    "Interstellar",
    "Inception",
    "The Dark Knight",
    "Avatar",
    "Titanic"
)
def show_movies():
    print("Favorite Movies:")
    for movie in movies:
        print(movie)
def total_movies():
    print("Total Number of Movies:", len(movies))
# Example usage
show_movies()
total_movies()