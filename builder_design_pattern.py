class FifaOnlinePlayer:
    def __init__(self, builder):
        self.name = builder.name
        self.age = builder.age
        self.nationality = builder.nationality
        self.position = builder.position
        self.team = builder.team
        self.stats = builder.stats

    def __repr__(self):
        return f'Name: {self.name} - Age: {self.age} - Nationality: {self.nationality} - Position: {self.position} - Team: {self.team} - Stats: {self. stats}'


class FifaOnlinePlayerBuilder:
    def __init__(self):
        self.name = None
        self.age = None
        self.nationality = None
        self.position = None
        self.team = None
        self.stats = None

    def with_name(self, name):
        self.name = name
        return self

    def with_age(self, age):
        self.age = age
        return self

    def with_nationality(self, nationality):
        self.nationality = nationality
        return self

    def with_position(self, position):
        self.position = position
        return self

    def with_team(self, team):
        self.team = team
        return self

    def with_stats(self, stats):
        self.stats = stats
        return self

    def build(self):
        return FifaOnlinePlayer(self)


def main():
    player_builder = FifaOnlinePlayerBuilder()
    cr7 = (
        player_builder
        .with_name('CR7')
        .with_age(39)
        .with_nationality('Portugal')
        .with_position('Striker')
        .with_team('Al Nassr')
        .with_stats({'goal': 50, 'assist': 10})
        .build()
    )
    print(cr7)

    m10 = (
        player_builder
        .with_name('M10')
        .with_age(37)
        .with_nationality('Argentina')
        .with_position('Forward')
        .with_team('Inter Miami')
        .with_stats(None)
        .build()
    )
    print(m10)


if __name__ == '__main__':
    main()
