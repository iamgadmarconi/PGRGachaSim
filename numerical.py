from rates import Pool
from random import choice


class Won:
    def __init__(self, total_pulls, pulls_since_s, character, pulls_since_ur):
        self.total_pulls = total_pulls
        self.pulls_since_s = pulls_since_s
        self.pulls_since_ur = pulls_since_ur
        self.character = character

    def __str__(self):
        return f"You got an S rank on pull {self.total_pulls}, {self.pulls_since_s} pulls since your last S rank. The" \
               f" S rank was {self.character.__str__()}, this is pull {self.pulls_since_ur} since the last Rate Up."


class Construct:
    def __init__(self):
        self.type = choice(Pool.rateup())
        if self.type is True:
            self.character = "Rate Up"
        elif self.type is False:
            self.character = "Off Banner"

    def __str__(self):
        return f"{self.character}"


class Numerical:
    def __init__(self, pulls, pulls_since_s=0):
        self.pulls = pulls
        self.pulls_since_s = pulls_since_s
        self.pulls_since_ur = 0
        self.num_ur = 0
        self.total_pulls = 0
        self.record = []

    def __repr__(self):
        string = ""
        for record in self.record:
            string += f"{record.__str__()}\n"
        return string.strip()

    def rolls(self):
        for self.total_pulls in range(self.pulls):
            self.total_pulls += 1
            won = choice(Pool.banner())
            if won is False:
                self.pulls_since_s += 1
                self.pulls_since_ur += 1
                if self.pulls_since_s == 60:
                    construct = Construct()
                    if construct.type is True:
                        sto = self.pulls_since_ur
                        self.pulls_since_ur = 0
                        self.num_ur += 1
                    elif construct.type is False:
                        sto = self.pulls_since_ur
                        pass
                    self.record.append(Won(self.total_pulls, self.pulls_since_s, construct, sto))
                    self.pulls_since_s = 0
            elif won is True:
                construct = Construct()
                if construct.type is True:
                    sto = self.pulls_since_ur
                    self.pulls_since_ur = 0
                    self.num_ur += 1
                elif construct.type is False:
                    sto = self.pulls_since_ur
                    pass
                self.record.append(Won(self.total_pulls, self.pulls_since_s, construct, sto))
                self.pulls_since_s = 0
