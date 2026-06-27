'''Task 4: Movie Database (Intermediate)
Objective

Manage a movie collection using JSON.

JSON Example
[
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "rating": 9.5
    }
]
Features
Add Movie
Search Movie
Delete Movie
Update Rating
Show Top Rated Movies
Bonus
Filter by genre
Sort by rating
Find average rating'''

import json

def add_movie(title, genre, rating):
    movie_data = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    data.append(movie_data)
    
    with open('movies.json', 'w') as file:
        json.dump(data, file, indent=4)

def view_all_movies():
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
            for movie in data:
                print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
    except FileNotFoundError:
        print("No movies found.")

def search_movie_by_title(title):
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
            for movie in data:
                if movie['title'].lower() == title.lower():
                    print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
                    return
            print("Movie not found.")
    except FileNotFoundError:
        print("No movies found.")

def update_movie_rating(title, new_rating):
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
            for movie in data:
                if movie['title'].lower() == title.lower():
                    movie['rating'] = new_rating
                    break
        with open('movies.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("No movies found.")

def delete_movie(title):
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
            data = [movie for movie in data if movie['title'].lower() != title.lower()]
        with open('movies.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("No movies found.")

def show_top_rated_movies():
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
            top_movies = sorted(data, key=lambda x: x['rating'], reverse=True)[:5]
            for movie in top_movies:
                print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
    except FileNotFoundError:
        print("No movies found.")

def filter_movies_by_genre(genre):
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
            filtered_movies = [movie for movie in data if movie['genre'].lower() == genre.lower()]
            for movie in filtered_movies:
                print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
    except FileNotFoundError:
        print("No movies found.")

def sort_movies_by_rating():
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
            sorted_movies = sorted(data, key=lambda x: x['rating'], reverse=True)
            for movie in sorted_movies:
                print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
    except FileNotFoundError:
        print("No movies found.")

def calculate_average_rating():
    try:
        with open('movies.json', 'r') as file:
            data = json.load(file)
            if not data:
                print("No movies found.")
                return
            average_rating = sum(movie['rating'] for movie in data) / len(data)
            print(f"Average Rating: {average_rating:.2f}")
    except FileNotFoundError:
        print("No movies found.")

def main():
    while True:
        print("\nMovie Database Menu:")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie by Title")
        print("4. Update Movie Rating")
        print("5. Delete Movie")
        print("6. Show Top Rated Movies")
        print("7. Filter Movies by Genre")
        print("8. Sort Movies by Rating")
        print("9. Calculate Average Rating")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            rating = float(input("Enter movie rating (0-10): "))
            add_movie(title, genre, rating)
            print("Movie added successfully.")
        elif choice == '2':
            view_all_movies()
        elif choice == '3':
            title = input("Enter movie title to search: ")
            search_movie_by_title(title)
        elif choice == '4':
            title = input("Enter movie title to update rating: ")
            new_rating = float(input("Enter new rating (0-10): "))
            update_movie_rating(title, new_rating)
            print("Movie rating updated successfully.")
        elif choice == '5':
            title = input("Enter movie title to delete: ")
            delete_movie(title)
            print("Movie deleted successfully.")
        elif choice == '6':
            show_top_rated_movies()
        elif choice == '7':
            genre = input("Enter genre to filter movies: ")
            filter_movies_by_genre(genre)
        elif choice == '8':
            sort_movies_by_rating()
        elif choice == '9':
            calculate_average_rating()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()