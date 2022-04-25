import random


class BotFunctions:
    def __init__(self):
        pass

    def get_quote(self, message_to_trim):
        command_length = len("!addquote ")
        quote_to_add = message_to_trim[command_length:]
        first_quote = 0
        second_quote = None
        found_quote = 0
        for num, character in enumerate(quote_to_add):
            if character == '"' or character == "“" or character == "”":
                if found_quote == 1:
                    second_quote = num + 1
                found_quote += 1
        quote = quote_to_add[first_quote:second_quote]
        attribution = quote_to_add[second_quote:]
        if len(attribution) < 1:
            attribution = "-Unknown"
        return quote, attribution

    def inspire_me(self, quotes):
        quote = random.choice(quotes)
        return quote

    def roll(self, dice_string):
        char_list = []
        for char in dice_string:
            char_list.append(char)
        numbers = []
        place_holder = []
        for char in char_list:
            if char.isdigit():
                place_holder.append(char)
            else:
                place_holder = "".join(place_holder)
                place_holder = int(place_holder)
                numbers.append(place_holder)
                place_holder = []
        place_holder = "".join(place_holder)
        place_holder = int(place_holder)
        numbers.append(place_holder)
        # score calculation.
        score = 0
        x = 0
        rolls = []
        while x < numbers[0]:
            roll = random.randint(1, numbers[1])
            rolls.append(roll)
            score += roll
            x += 1
        numbers.append(score)
        numbers.append(rolls)
        return numbers




