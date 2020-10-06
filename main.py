from perceptron import *

perceptron = Perceptron(2, 0.002)
learning_set = [[1,1,1],[0,0,1],[0,1,0],[0,0,0]]
perceptron.learn(learning_set)