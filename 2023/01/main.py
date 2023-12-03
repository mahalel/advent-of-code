import re

def word_to_digit(word):
    word_to_digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    return word_to_digit_mapping.get(word, word)

def get_calibration_value(x):
    regex_digits = re.findall(r"\d", x)
    return int(regex_digits[0] + regex_digits[-1])

def get_calibration_value_p2(x):
    regex_words = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
    matches = regex_words.findall(x)
    matches = [word_to_digit(match) for match in matches]
    return int(matches[0] + matches[-1])

def part_one(input):
    with open(input, "r") as f:
        total = 0
        for line in f.readlines():
            total += get_calibration_value(line)
        print(total)

def part_two(input):
    with open(input, "r") as f:
        total = 0
        for line in f.readlines():
           total += get_calibration_value_p2(line)
        print(total)

part_one("./input")
part_two("./input")
