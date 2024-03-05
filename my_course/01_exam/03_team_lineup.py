def team_lineup(*args):
    players_dict = {}
    for player_name, country_name in args:
        if country_name not in players_dict:
            players_dict[country_name] = []
        players_dict[country_name].append(player_name)

    sorted_players_dict = dict(sorted(players_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    result = ''
    for country, players in sorted_players_dict.items():
        result += f'{country}:\n'
        for player in players:
            result += f'  -{player}\n'

    return result


# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))
