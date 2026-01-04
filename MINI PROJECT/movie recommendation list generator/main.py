# main.py

from users import register_user, login_user, users
from recommendations import recommend_by_genre, search_movie

current_user = None

def show_menu():
    print("\n--- Movie Recommendation System ---")
    print("1. Register")
    print("2. Login")
    print("3. Search Movie")
    print("4. Get Recommendations by Genre")
    print("5. Save Movie to Watch Later")
    print("6. View Saved Movies")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if register_user(username, password):
            print("Registration successful!")
        else:
            print("User already exists.")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login_user(username, password):
            current_user = username
            print("Login successful!")
        else:
            print("Invalid credentials.")

    elif choice == "3":
        title = input("Enter movie title to search: ")
        results = search_movie(title)
        if results:
            for movie in results:
                print(movie)
        else:
            print("No movie found.")

    elif choice == "4":
        genre = input("Enter genre (Action/Drama/Comedy/Sci-Fi): ")
        recommendations = recommend_by_genre(genre)
        if recommendations:
            for movie in recommendations:
                print(movie)
        else:
            print("No recommendations found.")

    elif choice == "5":
        if not current_user:
            print("Please login first.")
            continue
        movie_title = input("Enter movie title to save: ")
        results = search_movie(movie_title)
        if results:
            users[current_user]["saved_movies"].append(results[0])
            print("Movie saved to Watch Later list.")
        else:
            print("Movie not found.")

    elif choice == "6":
        if not current_user:
            print("Please login first.")
            continue
        saved = users[current_user]["saved_movies"]
        if saved:
            print("\nYour Watch Later List:")
            for movie in saved:
                print(movie)
        else:
            print("No movies saved yet.")

    elif choice == "7":
        print("Exiting system. Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
