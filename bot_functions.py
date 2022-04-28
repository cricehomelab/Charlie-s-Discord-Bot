import random
from blacklisted_words import WordScan

class BotFunctions:
    def __init__(self):
        self.scan = WordScan()

    def get_quote(self, message_to_trim):
        command_length = len("!addquote ")
        quote_to_add = message_to_trim[command_length:]
        first_quote = 0
        second_quote = None
        found_quote = 0
        # runs through looking for potential data we won't want a discord bot to say.
        slur_used = self.scan.check_string(message_to_trim)
        print(f"after checking for language {slur_used}")
        if not slur_used[0]:
            for num, character in enumerate(quote_to_add):
                if character == '"' or character == "“" or character == "”":
                    if found_quote == 1:
                        second_quote = num + 1
                    found_quote += 1
            quote = quote_to_add[first_quote:second_quote]
            attribution = quote_to_add[second_quote:]
            if len(attribution) < 1:
                attribution = "-Unknown"
            print(f"get_quote return content True, {quote}, {attribution}")
            return True, quote, attribution
        else:
            return False, "Not adding"

    def inspire_me(self, quotes):
        quote = random.choice(quotes)
        return quote

    def roll(self, dice_string):
        print(f"original dice_string {dice_string}")
        char_list = []
        for char in dice_string:
            char_list.append(char)
        numbers = []
        place_holder = []
        modifier = []
        modifier_symbol = ""
        for num, char in enumerate(char_list):
            if char == "+":
                for character in char_list[num:]:
                    if character.isdigit():
                        modifier.append(character)
                modifier = "".join(modifier)
                modifier = int(modifier)
                modifier_symbol = "+"
            elif char == "-":
                for character in char_list[num:]:
                    if character.isdigit():
                        modifier.append(character)
                modifier = "".join(modifier)
                modifier = -abs(int(modifier))
                modifier_symbol = "-"
            elif char.isdigit():
                place_holder.append(char)
            else:
                place_holder = "".join(place_holder)
                place_holder = int(place_holder)
                numbers.append(place_holder)
                place_holder = []
        place_holder = "".join(place_holder)
        place_holder = int(place_holder)
        numbers.append(place_holder)
        print(f"modifier = {modifier}")
        print(f"modifier symbol = {modifier_symbol}")
        # score calculation.
        score = 0
        x = 0
        rolls = []
        while x < numbers[0]:
            roll = random.randint(1, numbers[1])
            rolls.append(roll)
            score += roll
            x += 1
        if modifier:
            score += modifier
        else:
            modifier = 0
            modifier_symbol = "+"
        numbers.append(score)
        numbers.append(rolls)
        print(f"modifier = {modifier}")
        print(f"modifier symbol = {modifier_symbol}")
        numbers.append(modifier_symbol)
        numbers.insert(2, modifier)
        print(numbers)
        #  [    0         1            2        3           4           5   ]
        #  [# of dice, # of sides,  modifier, score, [list of rolls], + or -]
        return numbers




