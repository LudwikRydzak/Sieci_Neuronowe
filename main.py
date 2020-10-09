from perceptron import *
from generator import *

uni0_bi1 = int(input("Unipolarne wejscia - 0, Bipolarne wejścia - 1 \n"))
perceptron = Perceptron(2, 0.0001)
learning_set = [[1,1,1],[-1,0,1],[-1,1,0],[-1,0,0]]
#learning_set = generate(10, uni0_bi1)
perceptron.learn(learning_set, uni0_bi1)
print(perceptron.prediction([0,0], uni0_bi1))
print(perceptron.prediction([0,1], uni0_bi1))
print(perceptron.prediction([1,0], uni0_bi1))
print(perceptron.prediction([1,1], uni0_bi1))