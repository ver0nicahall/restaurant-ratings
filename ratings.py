"""Restaurant rating lister."""
import sys

# Create a file variable by assigning index 1 from the command line 
filename = sys.argv[1]

# Initialize an empty dictionary to store restaurant: rating items
restaurant_ratings = {}
#create a list to hold all restaurants 
restaurants = []

# For loop to open file and iterate through each line of the file:
for restaurant_data in open(filename):
    # Tokenize each line by ":" delimiter
    restaurant_data = restaurant_data.rstrip()
    restaurant = restaurant_data.split(':')
    #add restaurant to restaurant list
    restaurants.append(restaurant)
    
# For each entry in restaurants
for item in restaurants: 
    # Update membership in dictionary by assigning value rating to key using .get()
    restaurant_ratings[item[0]] = item[1]

# Sort the dictionary
def sort_ratings(restaurant_ratings):
    sorted_ratings = sorted(restaurant_ratings.items())
    # Print in ascending order 
    print('Sorted ratings: ', sorted_ratings)
    for result in sorted_ratings:
        #print statement
        print(f"{result[0]} is rated at {result[1]}.")


# ask for input 
def add_input():
    """allow user to add ratings"""

    input_restaurant = input('What restaurant would you like to rate today? ')
    input_rating = input('What rating would you give this restaurant? ')
    # add to dictionary
    restaurant_ratings[input_restaurant] = input_rating 
    # sort function
    sort_ratings(restaurant_ratings)

#call functions
add_input()
