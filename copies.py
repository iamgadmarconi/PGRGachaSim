from simulation import Simulation
from rates import priceperpull


class Copies:
    def __init__(self, copies):
        self.copies = int(copies)

    def averageprice(self, currency="CHF"):
        sim = Simulation(1000, self.copies*120)
        sim.run()
        ave_s, ave_ur = sim.calculate()
        ppp = priceperpull(currency)
        money_ur = ppp * ave_ur * self.copies
        money_s = ppp * ave_s * self.copies
        return round(money_ur, 2), round(money_s, 2)

    def __str__(self):
        money_ur, money_s = self.averageprice()
        return f"It costs approximately {money_s} Euros to get {self.copies} of a Rate Up S-Rank on a 100% banner.\n"\
               f"It costs approximately {money_ur} Euros to get {self.copies} of a Rate Up S-Rank on a 70% banner.\n"
