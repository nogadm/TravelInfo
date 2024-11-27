import json
from datetime import datetime, timedelta, timezone
from api.currency import CurrencyApi

class Travel:
    
    src_city = None
    dest_city = None
    data = None

    def __init__(self, src_city, dest_city):
        self.src_city = src_city
        self.dest_city = dest_city
        self.data = self.load_database()

    def load_database(self):
        # load database json file
        f = open('database.json')
        data = json.load(f)
        f.close()
        return data

    def time_difference(self):
        # get time zones and country names
        src_time_zone = self.data[self.src_city]["time_zone"]
        dest_time_zone = self.data[self.dest_city]["time_zone"]

        src_country = self.data[self.src_city]["country"]
        dest_country = self.data[self.dest_city]["country"]

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
        message = f"{self.src_city} is {abs(time_diff)} hours {relative} of {self.dest_city}\\n\\n" \
                f"Current Time:\\n{self.src_city}, {src_country}: {current_time_in_src}\\n{self.dest_city}, {dest_country}: " \
                f"{current_time_in_dest}"
        return message

    def which_plug(self):
        # get a list of plugs
        dest_city_plugs = self.data[self.dest_city]["adapter"]

        # message to be displayed to user
        message = ("The plugs that are used in " + self.dest_city + " are:\\n" +
                "\\n".join(dest_city_plugs))

        return message

    def emergency_numbers(self):
        # get a list of the emergency numbers
        emergency_nums = self.data[self.dest_city]["emergency_numbers"]
        emergency_nums_str = '\\n'.join(f'{key} - {value}' for key, value in emergency_nums.items())

        # message to be displayed to user
        message = f"The emergency numbers in {self.dest_city} are:\\n{emergency_nums_str}"
        return message

    def learn_the_language(self):
        # get the language of the destination city and a list of phrases
        lang = self.data[self.dest_city]["language"]
        phrases = self.data[self.dest_city]["phrases"]
        phrases_str = '\\n'.join(f'{key}: {value}' for key, value in phrases.items())

        # message to be displayed to user
        message = f"The main language in {self.dest_city} is {lang}.\\n\\n" \
                f"Here are some helpful phrases you should probably know:\\n" \
                f"{phrases_str}"
        return message

    def full_city_details(self):
        # find conversion rate
        src_currency = self.data[self.src_city]["currency"]
        dest_currency = self.data[self.dest_city]["currency"]
        conversion_rate = "\\n" + CurrencyApi().get_conversion_rate(src_currency, dest_currency).return_value

        # find the rest of the city details
        time_diff = "\\n" + self.time_difference()
        plug = "\\n" + self.which_plug()
        emergency_nums = "\\n" + self.emergency_numbers()
        phrases = "\\n" + self.learn_the_language()

        info = [conversion_rate, time_diff, plug, emergency_nums, phrases]
        return info

    def get_full_destination_name(self):
        country = self.data[self.dest_city]["country"]
        full_name = f"{self.dest_city}, {country}"
        return full_name



