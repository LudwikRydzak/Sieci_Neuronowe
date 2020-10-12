import matplotlib as mtl
import numpy as np
from perceptron import *
from generator import *


def test():
    ranges = [[-1, 1], [-0.9, 0.9], [-0.8, 0.8], [-0.7, 0.7], [-0.6, 0.6], [-0.5, 0.5], [-0.4, 0.4], [-0.3, 0.3],
              [-0.2, 0.2], [-0.15, 0.15], [-0.1, 0.1], [-0.05, 0.05], [-0.01, 0.01]]
    learning_rate = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8,
                           7, 6, 5, 4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.3, 0.1, 0.05, 0.02, 0.01, 0.005,
                           0.002, 0.001, 0.0005, 0.0002, 0.0001, 0.00005, 0.00002, 0.00001]
    learning_count = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000]
    max_epochs = [50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 15000, 20000, 30000]
    uni0_bi1 = [0, 1]
    testing_count = 1000

    with open('wynikiBadania.txt', 'w') as file:
        file.writelines(
            'learning count; testing count; learning rate; max_epochs, uni/bi; range; epochs of learning; percentage of good answers\n')
        for unibi in uni0_bi1:
            testing_set = generate(testing_count, unibi)
            for count in learning_count:
                print('.')
                learning_set = generate(count, unibi)
                for range in ranges:
                    for epochs in max_epochs:
                        for rate in learning_rate:
                            perceptron = Perceptron(2, rate, epochs, range[0], range[1])
                            epochs_of_learning = perceptron.learn(learning_set, unibi)
                            percentage = perceptron.test_perceptron(testing_set, unibi)
                            file.writelines(f'{count};{testing_count};{rate};{epochs};{unibi};{range};{epochs_of_learning};{percentage}\n')
