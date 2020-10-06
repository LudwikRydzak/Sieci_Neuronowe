from perceptron import *
from generator import *
perceptron = Perceptron(2, 0.0001)
learning_set = [[1,1,1],[-1,0,1],[-1,1,0],[-1,0,0]]
learning_set = generate(5)
perceptron.learn(learning_set)
print(perceptron.prediction([1,1]))