import random

# Paramètres du jeu
width = 20
bird_pos = random.randint(0, 4)  # Position verticale aléatoire
pipes = [6, 12, 18]

# Générer le "terrain"
lines = []
for i in range(5):
    line = [" "] * width
    if i == bird_pos:
        line[0] = "🐦"
    for pipe in pipes:
        line[pipe] = "|"
    lines.append("".join(line))

# Lire README existant
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Remplacer la section FLAPPY
start = "<!-- FLAPPY-BIRD-START -->"
end = "<!-- FLAPPY-BIRD-END -->"
new_section = start + "\n" + "\n".join(lines) + "\n" + end

before = content.split(start)[0]
after = content.split(end)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(before + new_section + after)
import random

# Paramètres du jeu
width = 20
bird_pos = random.randint(0, 4)  # Position verticale aléatoire
pipes = [6, 12, 18]

# Générer le "terrain"
lines = []
for i in range(5):
    line = [" "] * width
    if i == bird_pos:
        line[0] = "🐦"
    for pipe in pipes:
        line[pipe] = "|"
    lines.append("".join(line))

# Lire README existant
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Remplacer la section FLAPPY
start = "<!-- FLAPPY-BIRD-START -->"
end = "<!-- FLAPPY-BIRD-END -->"
new_section = start + "\n" + "\n".join(lines) + "\n" + end

before = content.split(start)[0]
after = content.split(end)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(before + new_section + after)
