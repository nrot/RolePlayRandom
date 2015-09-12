__author__ = 'nrot'

class classTree(object):
    def __init__(self, name, parentLink):
        self.name = name
        self.Pareny = parentLink
        self.branchs = [[],[]]
        self.info = []
    def addBranch(self, branch, chance="one"):
        self.branchs[0].append(branch)
        self.branchs[1].append(chance)

    def addInfo(self, info):
        self.info.append(info)

    def parser(self, table):
        0