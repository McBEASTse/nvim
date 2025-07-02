import random

# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0

# Sätt antal linjer varje tuple som dice_art består av.
# I detta fall kontrolleras antal element (inom varje "") av första dice art.
num_lines_per_die = len(dice_art[1])
num_of_dice = int(input("Hur många tärningar vill du kasta?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Varje tuple består av fem element (rader).
# Varje rad av varje tuple behöver skrivas ut i följd i en linje.
# Därför behövs en for loop som kör fem gånger i följd där den skriver ut varje rad för varje tuple (från dice_art).

for line in range(num_lines_per_die):
    # Loopen nedan kollar "Hur många tärningar har vi i vår dice lista?"
    for die in dice:
        # Nedan tittar först vilken typ av tärning som blev resultatet.
        # dice_art.get(die) kollar listan dice_art och sedan vilken av
        # tärningarna (die) som ska visas.
        # [line] är en index operator som skriver ut en
        # rad (element, mellan "" och innan varje ,) av
        # vilken die inom dice_art som ska visas.
        # Värdet på [line] ökar för varje loop och tar sedan
        # nästa index (plats inom tuplen, i detta fall är index radnummer).
        # Första for loopen säger att detta ska köras fem gånger.
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die

print(f"Totala summan av {num_of_dice} tärningar är: {total}")
