import sys
import numpy as np

with open('old_commands.txt', 'r') as file1:
    with open('new_commands.txt', 'r') as file2:
        old_commands = np.array([old_command.strip().lower() for old_command in file1.readlines()])
        new_commands = np.array([new_command.strip().lower() for new_command in file2.readlines()])
        commands = list(set(new_commands) - set(old_commands))
        print_out = sorted(commands)
        print("\n".join(print_out))
        print("===================")
        print(f"New commands count: {len(print_out)}")
