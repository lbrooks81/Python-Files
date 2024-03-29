from pathlib import Path

path = Path('guest.txt')
names : list = path.read_text().splitlines()

for name in names:
    print(f"Welcome, {name.title()}")