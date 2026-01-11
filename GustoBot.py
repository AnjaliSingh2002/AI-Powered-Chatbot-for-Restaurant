import json
import random
import nltk

# Ensure that NLTK resources are downloaded only once and not during every execution
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_input(input_text):
    """
        Tokenizes the input text and filters out English stopwords.

        Parameters:
        - input_text (str): The text input by the user.

        Returns:
        - list: A list of filtered tokens from the input text.
        """
    tokens = word_tokenize(input_text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens

def search_menu(query, menu_data):
    """
       Searches the menu data for items matching the query terms.

       Parameters:
       - query (list): A list of preprocessed query terms.
       - menu_data (dict): The loaded menu data.

       Returns:
       - list: A list of dictionaries, each representing a matching menu item.
       """
    results = []
    for item_info in menu_data['menu']:
        item_description = item_info["name"] + " " + item_info["description"]
        if all(term.lower() in item_description.lower() for term in query):
            results.append(item_info)
    return results

def get_user_info():
    """
        Prompts the user for their name.

        Returns:
        - str: The name entered by the user.
        """
    name = input("Hi! What's your name? ")
    return name

def greet():
    """
        Generates a random greeting message.

        Returns:
        - str: A greeting message.
        """
    greetings = ['Buongiorno!', 'Hello!', 'Salve!']
    return random.choice(greetings)

def main():
    print(greet())
    print("Welcome to GustoBot, the Italian Restaurant Chatbot.")
    print("I can help you explore our delicious menu.")



    name = get_user_info()
    print(f"\nHello, {name}! Let's explore our menu.")


    print("\nHere's our menu:")
    with open('menu.json', 'r') as f:
       menu_data = json.load(f)

    while True:
        user_input = input("What would you like to know about our menu? ")
        if user_input.lower() == "quit":
            print("\nThankyou for using GustoBot! We hope to see you soon at our restaurant!")
            break

        query = preprocess_input(user_input)

        search_results = search_menu(query, menu_data)

        found_matching_items = False
        count = 0
        for result in search_results:
            count += 1
            print(f"\nMenu Item {count}:")
            print("ID:", result["id"])
            print("Name:", result["name"])
            print("Description:", result["description"])
            print("Price: ${:,.2f}".format(result["price"]))

        if not found_matching_items:
            print("\nSorry, we couldn't find any menu items matching your query.")

        choice = input("\nDo you have any other questions? (yes/no): ")
        if choice.lower() != "yes":
            print("\nIf you have any further questions or would like to make a reservation, feel free to reach out to us!")
            print("\nThank you for using GustoBot! We hope to see you soon at our restaurant!")
            break

if __name__ == '__main__':
    main()
