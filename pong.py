import random

height = 5
width = 11

# Position du ballon (x = horizontal, y = vertical)
ball_x = random.randint(1, width-2)
ball_y = random.randint(0, height-1)

# Générer le terrain Pong
lines = []
for y in range(height):
    line = [" "] * width
    if y == ball_y:
        line[ball_x] = "🏓"
    line[0] = "|"  # raquette gauche
    line[-1] = "|"  # raquette droite
    lines.append("".join(line))

# Lire README existant
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Remplacer la section PONG
start = "<!-- PONG-START -->"
end = "<!-- PONG-END -->"
new_section = start + "\n" + "\n".join(lines) + "\n" + end

before = content.split(start)[0]
after = content.split(end)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(before + new_section + after)
