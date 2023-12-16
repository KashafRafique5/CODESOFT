import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Improved function to get item recommendations for a given user
def recommend_items(user, user_item_matrix, user_similarity, genre_filter):
    # Check if the user exists
    if user not in user_item_matrix.index:
        return f"User '{user}' not found in the dataset."

    # Get the index of the user
    user_index = user_item_matrix.index.get_loc(user)
    
    similar_users = user_similarity[user_index]
    user_ratings = user_item_matrix.loc[user]
    
    # Initialize recommendations
    recommendations = []
    
    # Iterate through items using items() for cleaner iteration
    for item, user_rating in user_ratings.items():
        # Skip items the user has already interacted with
        if user_rating == 0:
            # Calculate the weighted average of ratings from similar users using enumerate
            weighted_sum = sum(sim * user_item_matrix.iloc[i][item] for i, sim in enumerate(similar_users))
            weighted_average = weighted_sum / (sum(similar_users) + 1e-10)  # Add a small value to avoid division by zero
            
            recommendations.append((item, weighted_average))
    
    # Sort recommendations by predicted rating
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    # Filter recommendations based on the selected genre
    filtered_recommendations = [(item, rating) for item, rating in recommendations if genre_filter.lower() in item.lower()]
    
    return filtered_recommendations

# Sample data for movie ratings
data = {
    'User': ['User1', 'User2', 'User3', 'User4'],
    'Item': ['Friends to Enemies Trope Books', 'Marriage of Convenience Books', 'Second Chance Trope Books', 'The Secret Identity Trope'],
    'Rating': [5, 4, 3, 2]
}

df = pd.DataFrame(data)

# Create a user-item matrix
user_item_matrix = df.pivot_table(index='User', columns='Item', values='Rating', fill_value=0)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Sample data for book recommendations
# Sample data for book recommendations
# Sample data for book recommendations
# Sample data for book recommendations
# Sample data for book recommendations
genres = {
    1: {
        'name': 'Friends to Enemies Trope',
        'books': [
            {
                'name': 'The Kite Runner',
                'author': 'Khaled Hosseini',
                'description': 'A powerful and emotional story of two childhood friends whose lives take different paths, leading to a complex relationship filled with guilt and redemption.',
                'rating': 4.8
            },
            {
                'name': 'Eleanor Oliphant Is Completely Fine',
                'author': 'Gail Honeyman',
                'description': 'An isolated woman\'s life transforms through unlikely connections, blurring the lines between enemies and friends.',
                'rating': 4.31
            },
            {
                'name': 'The Flatshare',
                'author': 'Beth O\'Leary',
                'description': 'In this contemporary romance, two strangers who initially dislike each other decide to share a flat, leading to unexpected and heartwarming connections as they navigate their unique living arrangement.',
                'rating': 4.01
            },
            # Add more books as needed
        ]
    },
    2: {
        'name': 'Marriage of Convenience',
        'books': [
            {
                'name': 'The Rosie Project',
                'author': 'Graeme Simsion',
                'description': 'An unconventional love story unfolds as a socially awkward professor searches for a life partner.',
                'rating': 4.5
            },
            {
                'name': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'description': 'Societal expectations and evolving feelings are explored in this classic tale that touches on elements of a marriage of convenience.',
                'rating': 4.28
            },
            {
                'name': 'Anne of Green Gables',
                'author': 'L.M. Montgomery',
                'description': 'The classic novel explores chosen family and the enduring bond between Anne Shirley and Gilbert Blythe.',
                'rating': 4.25
            },
            # Add more books as needed
        ]
    },
    3: {
        'name': 'Second Chance Trope',
        'books': [
            {
                'name': 'Me Before You',
                'author': 'Jojo Moyes',
                'description': 'A poignant love story explores the impact of a second chance at life on the characters, challenging perceptions and evoking profound emotions.',
                'rating': 4.26
            },
            {
                'name': 'One Day by David Nicholls',
                'author': 'David Nicholls',
                'description': 'Dexter and Emma\'s lives are revisited on the same day over the years, highlighting second chances and the complexities of timing in relationships.',
                'rating': 3.80
            },
            {
                'name': 'The Time Traveler\'s Wife by Audrey Niffenegger',
                'author': 'Audrey Niffenegger',
                'description': 'This unique love story involves time travel, allowing the characters multiple chances to connect and rediscover each other throughout their lives.',
                'rating': 3.96
            },
            # Add more books as needed
        ]
    },
    4: {
        'name': 'The Secret Identity Trope',
        'books': [
            {
                'name': 'Superman: Red Son by Mark Millar',
                'author': 'Mark Millar',
                'description': 'In this graphic novel, Superman\'s origin is reimagined as he lands in Soviet Russia instead of Smallville, exploring the consequences of his secret identity on a global scale.',
                'rating': 4.09
            },
            {
                'name': 'Alias Grace by Margaret Atwood',
                'author': 'Margaret Atwood',
                'description': 'Based on a true story, this historical fiction novel follows the convicted murderess Grace Marks as she reveals her past, leaving readers questioning the truth of her identity.',
                'rating': 4.02
            },
            {
                'name': 'Vicious by V.E. Schwab',
                'author': 'V.E. Schwab',
                'description': 'This novel explores the complex relationship between two former friends turned enemies, both possessing supernatural abilities and hidden identities that shape their rivalry.',
                'rating': 4.26
            },
            # Add more books as needed
        ]
    }
}

# Display available genres with IDs
genre_ids = {i: genre_info['name'] for i, genre_info in genres.items()}
print("Available Genres:")
for genre_id, genre_name in genre_ids.items():
    print(f"{genre_id}: {genre_name}")

# Ask the user if they want recommendations in another trope
while True:
    selected_genre_id = int(input("Enter the ID of your preferred genre: "))
    selected_genre = genre_ids.get(selected_genre_id)

    # Validate the selected genre ID
    if selected_genre:
        print(f"\nRecommendations for {selected_genre}:")
        for i, book in enumerate(genres[selected_genre_id]['books'], start=1):
            print(f"\n{i}. {book['name']} by {book.get('author', 'Unknown Author')}")
            print(f"   Description: {book['description']}")
            print(f"   Rating: {book['rating']}")
    else:
        print("Invalid genre ID. Please select a valid genre ID.")

    another_trope = input("Do you want recommendations in another trope? (yes/no): ")
    if another_trope.lower() != 'yes':
        print("It was great to be at your service.")
        break