__author__ = 'nrot'



class classCost(object):
    def __init__(self, string):
        import Source.Function.f_Cost_to_list as fctl
        c_cost = fctl.f_Cost_to_list(string)
        self.minCost = c_cost[0]
        self.maxCost = c_cost[1]

    def getRandomCost(self):
        import random
        return random.randint(self.minCost, self.maxCost)
