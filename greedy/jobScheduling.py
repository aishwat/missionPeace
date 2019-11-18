class Job:
    def __init__(self, id, d, profit):
        self.id = id
        self.d = d
        self.profit = profit

    def __lt__(self, other):
        return self.profit > other.profit

    def __repr__(self):
        return "(" + str(self.id) + " " + str(self.d) + " " + str(self.profit) + ")"


class Scheduling:
    def __init__(self, jobIds, deadlines, profits):
        self.jobs = []
        for i in range(len(profits)):
            self.jobs.append(Job(jobIds[i], deadlines[i], profits[i]))

    def getMaxProfitSchedule(self, deadline):
        jobs = sorted(self.jobs)
        print(jobs)

        result = [-1] * deadline

        # each job takes 1 unit time
        for i in range(len(jobs)):
            # try and fit at last available slot
            for j in range(min(jobs[i].d - 1, deadline - 1), -1, -1):
                if result[j] == -1:
                    result[j] = jobs[i].id
                    break;
        print(result)


ids = ['a', 'b', 'c', 'd', 'e']
d = [2, 1, 2, 1, 3]
profits = [100, 19, 27, 25, 15]
s = Scheduling(ids, d, profits)
s.getMaxProfitSchedule(3)
