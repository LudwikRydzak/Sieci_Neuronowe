from perceptron import *
from generator import *
from Testowanie import *

test()


# uni0_bi1 = int(input("Unipolarne wejscia - 0, Bipolarne wejścia - 1 \n"))
# perceptron = Perceptron(2, 0.0001, 2000, -1,1)
# #learning_set = [[1,1,1],[-1,0,1],[-1,1,0],[-1,0,0]]
# learning_set = generate(20, uni0_bi1)
# test_set = generate(20, uni0_bi1)
# perceptron.learn(learning_set, uni0_bi1)
# print(perceptron.test_perceptron(test_set, uni0_bi1))