legal_commands = {"paid", "annouce", "emailon", "emailoff", "phoneon", "phoneoff", "utility","history"}
legal_admin_commands = {"nuke","report","setutility"}
all_commands = legal_admin_commands | legal_commands

def legal_command(reply):
    return reply.split(" ")[0] in all_commands

