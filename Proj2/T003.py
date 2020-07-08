#  Alexandre Lança - 90701
#  Bruno Codinha   - 90707
#
#  Grupo 3

import random

class LearningAgent:

        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):
            self.nS = nS
            self.nA = nA
            self.q_table = [[None for i in range(self.nA)] for j in range(self.nS)]
            self.alpha = 0.2
            self.gamma = 0.9
            self.epsilon = 1
            self.visited = [[0 for i in range(self.nA)] for j in range(self.nS)]


        def getMax_index(self, st, aa):
            max = self.q_table[st][0]
            index = 0
            for k in range(len(aa)):

                if self.q_table[st][k] == None and k == 0:
                    max = 0

                if self.q_table[st][k] == None:
                    self.q_table[st][k] = 0

                if self.q_table[st][k] > max:
                    max = self.q_table[st][k]
                    index = k

            return index

        def get_least_visited(self, st, aa):
            min = 9999999999
            index = 0

            for i in range(len(aa)):
                if self.visited[st][i] < min:
                    min = self.visited[st][i]
                    index = i

            return index


        # Select one action, used when learning
        # st - is the current state
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                random_number = random.random()

                if random_number > self.epsilon:
                    # Vai escolher o max
                    a = self.getMax_index(st, aa)
                    self.visited[st][a] += 1
                else:
                    # Vou escolher uma ação random
                    if random.random() > 0.8:
                        a = random.randrange(len(aa))
                        self.visited[st][a] += 1
                    else:
                        a = self.get_least_visited(st, aa)
                        self.visited[st][a] += 1
                        

                if ( (self.epsilon * 0.993) >= 0.2):
                    self.epsilon *= 0.993

                return a

        # Select one action, used when evaluating
        # st - is the current state
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                # define this function
                a = self.getMax_index(st, aa)
                # print("select one action to see if I learned")
                return a


        # this function is called after every action
        # st - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,st,nst,a,r):

            index = 0
            max = self.q_table[nst][0]

            for rw in range(len(self.q_table[nst])):
                if self.q_table[nst][rw] == None:
                    break
                if self.q_table[nst][rw] > max:
                    max = self.q_table[nst][rw]
                    index = rw

            if self.q_table[nst][index] == None:
                self.q_table[nst][index] = 0

            if self.q_table[st][a] == None:
                self.q_table[st][a] = 0

            self.q_table[st][a] = self.q_table[st][a] + self.alpha * (r + self.gamma * self.q_table[nst][index] - self.q_table[st][a])
