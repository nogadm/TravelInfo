import base64
import json
from datetime import datetime, timedelta, timezone
import currency_api_request as ca


def load_database():
    # load database json file
    f = open('database.json')
    data = json.load(f)
    f.close()
    return data


def time_difference(src_city, dest_city):
    # load database file
    data = load_database()

    # get time zones and country names
    src_time_zone = data[src_city]["time_zone"]
    dest_time_zone = data[dest_city]["time_zone"]

    src_country = data[src_city]["country"]
    dest_country = data[dest_city]["country"]

    # calculate time difference
    time_diff = src_time_zone - dest_time_zone

    # check if the source city is ahead/behind the destination city
    if time_diff < 0:
        relative = "behind"
    elif time_diff > 0:
        relative = "ahead"
    else:
        relative = ""

    # calculate local times
    current_time_in_src = datetime.now(tz=timezone(timedelta(hours=src_time_zone))).strftime('%H:%M')
    current_time_in_dest = datetime.now(tz=timezone(timedelta(hours=dest_time_zone))).strftime('%H:%M')

    # message to be displayed to user
    message = f"{src_city} is {abs(time_diff)} hours {relative} of {dest_city}\n\n" \
              f"Current Time:\n{src_city}, {src_country}: {current_time_in_src}\n{dest_city}, {dest_country}: " \
               f"{current_time_in_dest}"
    return message


def which_plug(dest_city):
    # load database json file
    data = load_database()

    # get a list of plugs
    dest_city_plugs = data[dest_city]["adapter"]

    # message to be displayed to user
    message = ("The plugs that are used in " + dest_city + " are:\n" +
               "\n".join(dest_city_plugs))

    return message


def emergency_numbers(dest_city):
    # load database json file
    data = load_database()

    # get a list of the emergency numbers
    emergency_nums = data[dest_city]["emergency_numbers"]
    emergency_nums_str = '\n'.join(f'{key} - {value}' for key, value in emergency_nums.items())

    # message to be displayed to user
    message = f"The emergency numbers in {dest_city} are:\n{emergency_nums_str}"
    return message


def learn_the_language(dest_city):
    # load database json file
    data = load_database()

    # get the language of the destination city and a list of phrases
    lang = data[dest_city]["language"]
    phrases = data[dest_city]["phrases"]
    phrases_str = '\n'.join(f'{key}: {value}' for key, value in phrases.items())

    # message to be displayed to user
    message = f"The main language in {dest_city} is {lang}.\n\n" \
              f"Here are some helpful phrases you should probably know:\n" \
              f"{phrases_str}"
    return message


def encode_image(image):
    encoded_image = base64.b64encode(image).decode('utf-8')
    return encoded_image


def full_city_details(src_city, dest_city):
    # load database json file
    data = load_database()

    # find conversion rate
    src_currency = data[src_city]["currency"]
    dest_currency = data[dest_city]["currency"]
    conversion_rate = "\n" + ca.convert_amount(src_currency, dest_currency, 1)

    # find the rest of the city details
    time_diff = "\n" + time_difference(src_city, dest_city)
    plug = "\n" + which_plug(dest_city)
    emergency_nums = "\n" + emergency_numbers(dest_city)
    phrases = "\n" + learn_the_language(dest_city)

    # create a dictionary with icons and city details
    info = dict()

    with open('icons/currency.png', 'rb') as f:
        image = f.read()
        encoded_image = encode_image(image)
        info['conversion_rate'] = [encoded_image, conversion_rate]

    with open('icons/time.png', 'rb') as f:
        image = f.read()
        encoded_image = encode_image(image)
        info['time_diff'] = [encoded_image, time_diff]

    with open('icons/plug.png', 'rb') as f:
        image = f.read()
        encoded_image = encode_image(image)
        info['plug'] = [encoded_image, plug]

    with open('icons/emergency.png', 'rb') as f:
        image = f.read()
        encoded_image = encode_image(image)
        info['emergency_nums'] = [encoded_image, emergency_nums]

    with open('icons/language.png', 'rb') as f:
        image = f.read()
        encoded_image = encode_image(image)
        info['phrases'] = [encoded_image, phrases]

    return info


def find_country(dest_city):
    data = load_database()
    return data[dest_city]["country"]



