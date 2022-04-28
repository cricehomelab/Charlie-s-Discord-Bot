"""
Trigger Warning: The following list are offensive rude words that have no place being stored/used in my discord bot.
The intention creating this blacklist is to prevent these words from being used in my discord server. These words have
a context for demeaning and marginalizing people. I don't want them used in my discord server this is meant as a way to
help prevent them from being used or stored in any context from my discord bot. If you are reading this list please be
warned these words might be found offensive but are being stored here for the greater good of preventing use of racial
slurs, homophobic slurs, and sexist slurs from being used on my discord server.

If you are offended by these being stored in this way I sincerely apologize, and am open to suggestions about how to
better store this information while still working to ensure that my bots don't cause harm to the people I love
and care about.

I realize the list is very small now this module is in early stages of development, and can be edited if for some reason
you want to use my code in your own implementation of a way to keep people safe online. Have a nice day.


"""

class WordScan:
    def __init__(self):
        # This is a list of slurs I intend to prevent from being mentioned by my bot.
        # TRIGGER WARNING the following list of words should not be used anywhere, and are without a doubt words that
        # that can violate the TOS of Discord. This list is used to prevent the words from being used in my software
        # or from being stored in my databases. As I do not want a part in spreading racism, hatred, or bullying of
        # people who, like everyone, are trying to live their lives, and are marginalized for their perceived
        # "differences".
        # put banned words here.
        self.list_of_slurs = ["chink", "faggot", "nigger", "wop", "tranny", "cunt", "bitch"]

    def check_string(self, string_to_check):
        """
        This will check through a string for innapropriate language and filter it.
        :param string_to_check: this is the string being passed.
        :return: True/False - True means that the phrase is censored and should not be repeated, saved, or added by the
        bot
        False means there is nothing in the censor list that should be prevented from uploading.
        Will also return a string, if the string is censored it will return "Innapropriate quote" otherwise it will
        return the string that was submitted.
        """
        prevent_upload = False
        string_to_check = string_to_check.split()
        print(f"checking for bad words in {string_to_check}")
        for word in string_to_check:
            word = ''.join(filter(str.isalnum, word))
            if word.lower() in self.list_of_slurs:
                print(f"word {word} is banned.")
                prevent_upload = True
                string_to_check = "Innapropriate quote"
                break
        if prevent_upload:
            return True, string_to_check
        else:
            string_to_check = ' '.join(string_to_check)
            return False, string_to_check


def main():
    scan = WordScan()
    string_to_check = "!addquote “You are a bad person.” - someone"
    print(f"return input {scan.check_string(string_to_check)}")

# main()