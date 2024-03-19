# clean_config.py
with open('config.py', 'r') as file:
    lines = file.readlines()

with open('config.py', 'w') as file:
    for line in lines:
        if 'TOKEN' not in line and 'SECRET' not in line:
            file.write(line)