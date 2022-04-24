import random


class BotFunctions():
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



