import Spammer

list = Spammer.parse_message("/media/tonyvo/VO/Programming/git-repos/Voma_Notifications/Messages/2DayWarning.mv")
dictionary = {"[NAME]" : "Tuan","[PRICE]" : "600"}

print list
print(Spammer.construct_token_string(list, dictionary))