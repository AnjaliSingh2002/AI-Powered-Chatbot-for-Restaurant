import discord
from discord.ext import commands
import json
import random
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Import functions from GustoBot.py
from GustoBot import (preprocess_input, search_menu, greet, get_user_info)

# Initialize intents
intents = discord.Intents.default()
intents.messages = True

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Load menu data from JSON file
with open('menu.json', 'r') as menu_file:
    menu_data = json.load(menu_file)

GREETINGS = ["hello", "hi", "hey", "greetings", "sup", "what's up"]
MENU_INQUIRY_KEYWORDS = ["show me the menu", "food", "dishes", "cuisine"]
RESERVATION_KEYWORDS = ["can i have reservation", "book", "table"]
SPECIAL_OFFER_KEYWORDS = ["do you have any special offer", "discount", "promotion"]
CUISINE_PREFERENCE_KEYWORDS = ["what is the most prefer dish", "like", "love", "dish", "cuisine"]
RESTAURANT_INFO_KEYWORDS = ["where is it located", "hours", "contact", "ambiance"]
EVENT_PLANNING_KEYWORDS = ["do you organise event", "party"]
WINE_BEVERAGE_KEYWORDS = ["wine", "beverage", "what type of breverage do you have", "drink"]
FEEDBACK_KEYWORDS = ["any feedback for improvement", "improvement"]



@bot.command()
async def greet(ctx):
    greetings = ['Hi!', 'Hello!', 'Hey there!', "Greetings"]
    await ctx.send(random.choice(greetings))

# Define an event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} is now running on Discord!')


@bot.event

async def on_message(message):

    if message.author == bot.user:
        return

    if any(keyword in message.content.lower() for keyword in GREETINGS):
        await greet(message.channel)
        await message.channel.send("Ciao! I'm GustoBot, your Italian restaurant assistant. How can assist you? ",)

    elif any(keyword in message.content.lower() for keyword in MENU_INQUIRY_KEYWORDS):
        await display_menu(message.channel)


    elif any(keyword in message.content.lower() for keyword in RESERVATION_KEYWORDS):
        await assist_with_reservation(message.channel)


    elif any(keyword in message.content.lower() for keyword in SPECIAL_OFFER_KEYWORDS):
        await provide_special_offers(message.channel)

    elif any(keyword in message.content.lower() for keyword in CUISINE_PREFERENCE_KEYWORDS):
        await inquire_cuisine_preference(message.channel)

    elif any(keyword in message.content.lower() for keyword in RESTAURANT_INFO_KEYWORDS):
        await provide_restaurant_info(message.channel)

    elif any(keyword in message.content.lower() for keyword in EVENT_PLANNING_KEYWORDS):
        await assist_with_event_planning(message.channel)

    elif any(keyword in message.content.lower() for keyword in FEEDBACK_KEYWORDS):
        await collect_feedback(message.channel)

    elif any(keyword in message.content.lower() for keyword in WINE_BEVERAGE_KEYWORDS):
        await recommend_wine_beverages(message.channel)

    else:
        await bot.process_commands(message)


# Define a command to display the restaurant menu
async def display_menu(channel):
    response = "Here is our menu:\n"
    for category, items in menu_data.items():
        response += f"\n**{category.capitalize()}**:\n"
        for item in items:
            response += f"{item['name']} - ${item['price']}\n"
    await channel.send(response)



# Define a command to assist with making reservations
async def assist_with_reservation(channel):
    await channel.send("Would you like to make a reservation? If yes, please provide the details (date, time, number of guests, etc.).")


# Define a command to provide information about special offers
async def provide_special_offers(channel):
    await channel.send("We currently have special offers available. Would you like to know more about them?")


# Define a command to inquire about cuisine preferences
async def inquire_cuisine_preference(channel):
    await channel.send("Do you have any favorite Italian dishes or specific cuisine preferences?")


# Define a command to provide information about the restaurant
async def provide_restaurant_info(channel):
    await channel.send("Sure! Our restaurant is located at Seymor 4th avneue, and we are open 11am-10pm. For more details, you can contact us at +54810492940.(https://www.google.com/maps/place/Seymour+at+4th+Ave/@50.6748955,-120.3416957,15z/data=!4m6!3m5!1s0x537e2dab67e547cf:0xb155f637aa755899!8m2!3d50.674896!4d-120.331396!16s%2Fg%2F1234f6514?entry=ttu)!")

 #Load the image file
    with open('restaurant_location.jpg', 'rb') as file:
        location_image = discord.File(file)
        # Send the image along with the text information
        await channel.send(file=location_image)
# Define a command to assist with event planning
async def assist_with_event_planning(channel):
    await channel.send("Are you interested in hosting an event or party at our restaurant? We'd be happy to assist you with the arrangements.")


# Define a command to collect user feedback
async def collect_feedback(channel):
    await channel.send("We value your feedback! Please share any comments, suggestions, or ideas for improvement with us.")


# Define a command to recommend wine and beverages
async def recommend_wine_beverages(channel):
    await channel.send("Would you like recommendations for wine pairings or specialty beverages to complement your meal?")


# Run the bot with the Discord bot token
bot.run('MTIyMTg4MDc3OTUwMDY4NzQwMA.GN4Hje.P09_HUu4M1lpKdljuLhrPmunqPYOq0XLvkit74')
