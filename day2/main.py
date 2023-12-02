def process_game(game):
        red, green, blue = 12, 13, 14
        max_red, max_green, max_blue = 0, 0, 0
        possible = True
        for round in game:
            scores = round.split(", ")
            for score in scores:
                val, color = int(score.split(" ")[0]), score.split(" ")[1]
                if color == "red":
                    max_red = max(max_red, val)
                    if red < val:
                        possible = False
                elif color == "green":
                    max_green = max(max_green, val)
                    if green < val:
                        possible = False
                elif color == "blue":
                    max_blue = max(max_blue, val)
                    if blue < val:
                        possible = False
        power = max_red * max_green * max_blue
        return possible, power                

def main(input):
    with open(input, "r") as f:
        games = f.read().splitlines()
        total_ids, total_power = 0, 0
        for game_id in range(len(games)):
            game = games[game_id].split(": ")[1].split("; ")
            result = process_game(game)
            if result[0]:
                total_ids += game_id + 1
            total_power += result[1]
        print(f"Total IDs: {total_ids}, Total Power: {total_power}")

# main("./example_p1")
main("./input")
