class Pool:
    @staticmethod
    def banner():
        pool = [False] * 199
        pool.append(True)
        return pool

    @staticmethod
    def rateup():
        pool = [True] * 7
        foo = [False] * 3
        pool.extend(foo)
        return pool


def priceperpull(currency):
    currencies = {"EUR": 100, "CHF": 85}
    return currencies[currency] / (7300 / 250)


def rank(rank: str):
    ranks = {"S": 1, "SS": 3, "SSS": 5, "SSS+": 11}
    return ranks[rank]
