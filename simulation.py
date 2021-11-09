from numerical import Numerical


class Simulation:
    def __init__(self, trials, pullspertrial=10000):
        self.trials = trials
        self.pullspertrial = pullspertrial
        self.record = []

    def __str__(self):
        ave_s, ave_ur = self.calculate()
        return f"For {self.trials} trials with {self.pullspertrial} pulls per trial, it takes an average of {ave_s}"\
               f" pulls to get an S-Rank.\nIf the banner is rotational, it takes an average of {ave_s} pulls to get an "\
               f"S-Rank, and an average of {ave_ur} pulls to get the Rate Up S-Rank."

    def run(self):
        for trial in range(self.trials):
            obj = Numerical(self.pullspertrial)
            obj.rolls()
            self.record.append(obj)

    def calculations(self, obj: Numerical):
        try:
            average_s = obj.total_pulls / len(obj.record)
            average_ur = obj.total_pulls / obj.num_ur
        except ZeroDivisionError:
            average_s = obj.total_pulls / len(obj.record)
            average_ur = self.pullspertrial
        return average_s, average_ur

    def calculate(self):
        average_rateup = 0
        average_srank = 0
        total = 0
        for trial in self.record:
            total += 1
            average_s, average_ur = self.calculations(trial)
            average_rateup += average_ur
            average_srank += average_s

        return average_srank // total, average_rateup // total


# s = Simulation(100, 1200)
# s.run()
# s.calculate()
# print(s.__str__())