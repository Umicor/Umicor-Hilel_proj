team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players(players: list[dict]) -> None:
    """This function should print all players to the client"""
    for dictionary in players:
        dict_items = [f"{key}: {value}" for key, value in dictionary.items()]
        print(", ".join(dict_items))


def add_player(num: int, name: str, age: int) -> None:
    """This function adds the new player."""
    my_dict = {"name": name, "age": age, "number": num}
    team.append(my_dict)


def remove_player(players: list[dict], num: int) -> None:
    """This function removes the player by his/her number."""
    players_to_keep = []
    for dictionary in players:
        if num != dictionary.get("number"):
            players_to_keep.append(dictionary)
    players[:] = players_to_keep


def main():
    show_players(team)

    print("________")

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    show_players(team)
    print("________")

    remove_player(players=team, num=17)

    show_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
