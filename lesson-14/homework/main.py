# import json
# import requests
# import pprint
# import random

# 1.Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.

# with open(file='students.json',mode='r') as file:
#     data = json.load(file)
# for i in data:
#     print(i)

# ---

# 2. Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

# api_key = '710a89b24d49749d2ea4c8c244952386' 
# city = 'Tashkent'
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# response = requests.get(url)
# data = response.json() 
# data_temp = data['main']['temp']
# data_humidity = data['main']['humidity']
# data_city = data['name']
# print(f'City:{data_city}, temprature:{data_temp}, humidity:{data_humidity}')

# ---

# 3. Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file. 

# with open(file='book.json', mode='r') as file:
#     data = json.load(file)

# def menu():
#     print('1. Add book')
#     print('2. Update book')
#     print('3. Delete book')
#     print('4. Show books')
#     print('5. Exit')


# def save_data():
#     with open('book.json', 'w') as file:
#         json.dump(data, file, indent=4)


# def add_book():
#     new_id = max(book['id'] for book in data) + 1 if data else 1
#     title = input('Enter book title: ')
#     author = input('Enter author: ')
#     genre = input('Enter genre: ')
#     year = int(input('Enter published year: '))
#     available = input('Is it available? (yes/no): ').strip().lower() == 'yes'
#     rating = float(input('Enter rating (e.g. 4.5): '))

#     new_book = {
#         "id": new_id,
#         "title": title,
#         "author": author,
#         "genre": genre,
#         "published_year": year,
#         "available": available,
#         "rating": rating
#     }

#     data.append(new_book)
#     save_data()
#     print(f'✅ Book "{title}" added successfully!')


# def update_book():
#     book_id = int(input('Enter the ID of the book to update: '))
#     for book in data:
#         if book['id'] == book_id:
#             print('Leave field empty to keep current value.')
#             title = input(f'Title [{book["title"]}]: ') or book["title"]
#             author = input(f'Author [{book["author"]}]: ') or book["author"]
#             genre = input(f'Genre [{book["genre"]}]: ') or book["genre"]
#             year = input(f'Published Year [{book["published_year"]}]: ') or book["published_year"]
#             available = input(f'Available (yes/no) [{book["available"]}]: ')
#             rating = input(f'Rating [{book["rating"]}]: ') or book["rating"]

#             book["title"] = title
#             book["author"] = author
#             book["genre"] = genre
#             book["published_year"] = int(year)
#             book["available"] = book["available"] if available == '' else available.strip().lower() == 'yes'
#             book["rating"] = float(rating)

#             save_data()
#             print('✅ Book updated successfully!')
#             return
#     print('❌ Book ID not found.')


# def delete_book():
#     book_id = int(input('Enter the ID of the book to delete: '))
#     for book in data:
#         if book['id'] == book_id:
#             data.remove(book)
#             save_data()
#             print('✅ Book deleted successfully!')
#             return
#     print('❌ Book ID not found.')


# def show_books():
#     print("\n--- All Books ---")
#     for book in data:
#         print(f'{book["id"]}: {book["title"]} by {book["author"]} ({book["published_year"]})')

 
# while True:
#     menu()
#     try:
#         command = int(input('Enter Command Number: '))
#     except ValueError:
#         print("❌ Invalid input. Please enter a number.")
#         continue

#     if command == 1:
#         add_book()
#     elif command == 2:
#         update_book()
#     elif command == 3:
#         delete_book()
#     elif command == 4:
#         show_books()
#     elif command == 5: 
#         break
#     else:
#         print('Unknown command. Please try again.')

# ---

# 4. Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.

# API_KEY = '6f2da472'
# BASE_URL = 'http://www.omdbapi.com/'

# def get_random_movie_by_genre(genre): 
#     search_url = f'{BASE_URL}?apikey={API_KEY}&s={genre}&type=movie&page=1'
#     response = requests.get(search_url)
    
#     if response.status_code != 200:
#         print('❌ Error contacting OMDb API')
#         return

#     search_data = response.json()
    
#     if search_data.get('Response') == 'False':
#         print('❌ No movies found for that genre.')
#         return

#     movies = search_data.get('Search', [])
#     if not movies:
#         print('❌ No movie results.')
#         return

#     movie = random.choice(movies)
#     movie_id = movie.get('imdbID')
 
#     details_url = f'{BASE_URL}?apikey={API_KEY}&i={movie_id}&plot=short'
#     details_response = requests.get(details_url)
#     details = details_response.json()
 
#     print('\n🎬 Movie Recommendation:')
#     print(f"Title: {details.get('Title')}")
#     print(f"Year: {details.get('Year')}")
#     print(f"Genre: {details.get('Genre')}")
#     print(f"Plot: {details.get('Plot')}")
#     print(f"IMDb Rating: {details.get('imdbRating')}")

 
# genre = input('Enter a movie genre (e.g. Action, Comedy, Horror): ')
# get_random_movie_by_genre(genre)
