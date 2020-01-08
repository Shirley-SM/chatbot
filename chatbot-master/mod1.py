
import random
import json
import requests
import spacy

weather_api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
norris_api = 'https://api.chucknorris.io/jokes/random'

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)
GREETING_RESPONSES = ["Sup", "Hey", "Salutations", "Heya", "Greeting", "Welcome"]
WEATHER_KEYWORDS = ["Weather", "wether", "weather"]
PUNCTUATIONS = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
CONFUSED = "I'm sorry but I'm not sure what you mean. If you're not sure what to say, " \
           "you're always  welcome to ask me for the weather or a joke. " \
           "Mind your language though ;)"
CURSES = ["skank",
          "arse",
          "bastard",
          "crap",
          "asshole",
          "stupid",
          "idiot",
          "ass",
          "bitch",
          "motherfucker",
          "prick",
          "cunt",
          "dick",
          "douchebag",
          "fart",
          "pussy",
          "slut",
          "whore",
          "fatass",
          "twat",
          "fuck",
          "horseshit",
          "shit",
          "shitass"
          "fatso",
          "biatch",
          ]


def analyze(sentence):
    if stock_analyze(sentence):
        return stock_analyze(sentence)
    else:
        return json.dumps({"animation": "confused", "msg": CONFUSED})


def stock_analyze(sentence):
    if check_if_greeting(sentence):
        return check_if_greeting(sentence)
    elif check_if_name(sentence):
        return check_if_name(sentence)
    elif check_if_greeting(sentence):
        return check_if_greeting(sentence)
    elif check_if_weather_request(sentence):
        return check_if_weather_request(sentence)
    elif check_if_joke_request(sentence):
        return get_joke()
    elif identify_lol(sentence):
        return identify_lol(sentence)
    elif find_curse(sentence):
        return find_curse(sentence)
    elif identify_city(sentence):
        return identify_city(sentence)
    elif check_if_name(sentence):
        return check_if_name(sentence)
    elif identify_bye(sentence):
        return identify_bye(sentence)


def remove_punct(my_str):
    no_punct = ""
    for char in my_str:
        if char not in PUNCTUATIONS:
            no_punct += char
    return no_punct


def check_if_name(sentence):
    if identify_city(sentence):
        return identify_city(sentence)
    else:
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(sentence)
        greet_back = random.choice(GREETING_RESPONSES)
        for ent in doc.ents:
            return json.dumps({"animation": "excited", "msg": f"{greet_back} {ent.text}"})


def check_if_greeting(sentence):
    words = sentence.split()
    for word in words:
        if word.lower() in GREETING_KEYWORDS:
            return send_greeting()


def send_greeting():
    greet_back = random.choice(GREETING_RESPONSES)
    return json.dumps({"animation": "dog", "msg": greet_back})


def check_if_weather_request(sentence):
    string = remove_punct(sentence)
    words = string.split()
    for word in words:
        if word.lower() in WEATHER_KEYWORDS:
            return json.dumps({"animation": "takeoff", "msg": "Enter 'my city is..' to get your weather prediction"})


def get_weather(input):
    city = input
    url = weather_api_address + city
    json_data = requests.get(url).json()
    weather_description = json_data['weather'][0]['description']
    weather_max_temp = json_data['main']['temp_max']
    weather_min_temp = json_data['main']['temp_min']
    weather_message = f"Expect {weather_description} with temperatures ranging from {weather_min_temp}° to {weather_max_temp}°."
    return json.dumps({"animation": "ok", "msg": str(weather_message)})


def identify_city(sentence):
    location_string = sentence.lower()
    sub_string = "city is"
    if str(sub_string) in location_string:
        s1 = sentence
        s2 = "is"
        city = s1[s1.index(s2) + len(s2):]
        return get_weather(city)


def check_if_joke_request(sentence):
    string = sentence.lower()
    substring = "joke"
    if substring in string:
        return True


def get_joke():
    url = norris_api
    json_data = requests.get(url).json()
    norris_joke = json_data['value']
    return json.dumps({"animation": "laughing", "msg": norris_joke})

def identify_lol(sentence):
    lol_string = sentence.lower()
    sub_string = "lol"
    sub_string2 = "haha"
    sub_string3 = "ha"
    if sub_string in lol_string or sub_string2 in lol_string or sub_string3 in lol_string:
        return json.dumps({"animation": "giggling", "msg": "It's funny 'cause it's true"})


def find_curse(sentence):
    string = sentence.lower()
    words = string.split()
    for word in words:
        if any(x == word for x in CURSES):
            bot_curse = random.choice(CURSES)
            curse_back = f"Yo momma, {bot_curse}."
            return json.dumps({"animation": "no", "msg": curse_back})

def identify_bye(sentence):
    bye_string = sentence.lower()
    sub_string = "bye"
    sub_string2 = "goodbye"
    sub_string3 = "see ya"
    if sub_string in bye_string or sub_string2 in bye_string or sub_string3 in bye_string:
        return json.dumps({"animation": "heartbroken", "msg": "See ya"})


