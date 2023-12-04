from collections import defaultdict

def get_matches(card):
    winning_numbers, numbers_we_have = card.split(": ")[1].split(" | ")
    winning_numbers = set([int(i) for i in winning_numbers.split()])
    numbers_we_have = set([int(i) for i in numbers_we_have.split()])
    matches = len(winning_numbers.intersection(numbers_we_have))
    return matches

def main(input):
    with open(input, "r") as f:
        content = f.readlines()
    cards_total = 0
    cards = defaultdict(lambda: 1)
    for idx, card in enumerate(content):
        c = cards[idx]
        matches = get_matches(card)
        for i in range(1, matches + 1):
            cards[idx + i] += 1 * c
        if matches > 0:
            cards_total += 2 ** (matches - 1)
    return cards_total, sum(cards.values())

# input = "./example"
input = "./input"

print(main(input))
