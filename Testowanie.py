import matplotlib.pyplot as plt
import numpy as np
from perceptron import *
from generator import *


def test():
    ranges = [[-1, 1], [-0.9, 0.9], [-0.8, 0.8], [-0.7, 0.7], [-0.6, 0.6], [-0.5, 0.5], [-0.4, 0.4], [-0.3, 0.3],
              [-0.2, 0.2], [-0.15, 0.15], [-0.1, 0.1], [-0.05, 0.05], [-0.01, 0.01]]
    learning_rate = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005,
                     0.002, 0.001, 0.0005, 0.0002, 0.0001, 0.00005, 0.00002, 0.00001]
    learning_count = 100
    max_epochs = 500
    uni0_bi1 = [0, 1]
    testing_count = 25

    with open('badaniaV2learningRate2.txt', 'w') as file:
        file.writelines(
            'learning count; testing count; learning rate; max_epochs; uni/bi; range;max epochs of learning; mean epochs of learning; min epochs of learning; max percentage of good answers; mean percentage of good answers; min percentage of good answers\n')
        for unibi in uni0_bi1:
            testing_set = generate(testing_count, unibi)
            learning_set = generate(learning_count, unibi)
            epochs_min_set = []
            percentage_min_set = []
            epochs_mean_set = []
            percentage_mean_set = []
            epochs_max_set = []
            percentage_max_set = []
            for rate in learning_rate:
                epochs_mean = 0
                percentage_mean = 0
                epochs_max = 0
                epochs_min = 501
                percentage_max = 0
                percentage_min = 101

                for i in range(10):
                    perceptron = Perceptron(2, rate, max_epochs, -1, 1)
                    epochs_of_learning = perceptron.learn(learning_set, unibi)
                    percentage = perceptron.test_perceptron(testing_set, unibi)
                    epochs_mean += epochs_of_learning
                    percentage_mean += percentage
                    if epochs_of_learning>epochs_max:
                        epochs_max = epochs_of_learning
                    if epochs_of_learning<epochs_min:
                        epochs_min = epochs_of_learning
                    if percentage > percentage_max:
                        percentage_max = percentage
                    if percentage < percentage_min:
                        percentage_min = percentage
                epochs_mean /= 10
                percentage_mean /= 10
                epochs_min_set.append(epochs_min)
                percentage_min_set.append(percentage_min)
                epochs_mean_set.append(epochs_mean)
                percentage_mean_set.append(percentage_mean)
                epochs_max_set.append(epochs_max)
                percentage_max_set.append(percentage_max)
                file.writelines(
                        f'{learning_count};{testing_count};{rate};{max_epochs};{unibi};[-1, 1];{epochs_max};{epochs_mean};{epochs_min};{percentage_max};{percentage_mean};{percentage_min}\n')
            show_learning_epochs(learning_rate, epochs_min_set, epochs_mean_set, epochs_max_set)
            show_learning_percentages(learning_rate, percentage_min_set, percentage_mean_set, percentage_max_set)

    with open('badaniaV2weightRanges2.txt', 'w') as file:
        file.writelines(
            'learning count; testing count; learning rate; max_epochs; uni/bi; range; epochs of learning; percentage of good answers\n')
        for unibi in uni0_bi1:
            testing_set = generate(testing_count, unibi)
            learning_set = generate(learning_count, unibi)
            epochs_min_set = []
            percentage_min_set = []
            epochs_mean_set = []
            percentage_mean_set = []
            epochs_max_set = []
            percentage_max_set = []
            for wrange in ranges:
                epochs_mean = 0
                percentage_mean = 0
                epochs_max = 0
                epochs_min = 501
                percentage_max = 0
                percentage_min = 101

                for i in range(10):
                    perceptron = Perceptron(2, 0.0001, max_epochs, wrange[0], wrange[1])
                    epochs_of_learning = perceptron.learn(learning_set, unibi)
                    percentage = perceptron.test_perceptron(testing_set, unibi)
                    epochs_mean += epochs_of_learning
                    percentage_mean += percentage
                    if epochs_of_learning>epochs_max:
                        epochs_max = epochs_of_learning
                    if epochs_of_learning<epochs_min:
                        epochs_min = epochs_of_learning
                    if percentage > percentage_max:
                        percentage_max = percentage
                    if percentage < percentage_min:
                        percentage_min = percentage
                epochs_mean /= 10
                percentage_mean /= 10
                epochs_min_set.append(epochs_min)
                percentage_min_set.append(percentage_min)
                epochs_mean_set.append(epochs_mean)
                percentage_mean_set.append(percentage_mean)
                epochs_max_set.append(epochs_max)
                percentage_max_set.append(percentage_max)
                file.writelines(
                        f'{learning_count};{testing_count};0.0001;{max_epochs};{unibi};{wrange};{epochs_max};{epochs_mean};{epochs_min};{percentage_max};{percentage_mean};{percentage_min}\n')
            show_range_epochs(ranges, epochs_min_set, epochs_mean_set, epochs_max_set)
            show_range_percentages(ranges, percentage_min_set, percentage_mean_set, percentage_max_set)

def show_learning_epochs(x, ymin, ymean, ymax):
    plt.title('Badanie wpływu współczynnika uczenia na szybkość uczenia w epokach')
    plt.xlabel('współczynnik uczenia')
    plt.ylabel('epoki')
    plt.plot(x, ymin, 'r+', label='minimalna liczba epok')
    plt.plot(x, ymean, 'bo', label='średnia liczba epok')
    plt.plot(x, ymax, 'g+', label='maksymalna liczba epok')
    plt.show()
def show_learning_percentages(x, ymin, ymean, ymax):
    plt.title('Badanie wpływu współczynnika uczenia na jakość uczenia w procentach')
    plt.xlabel('współczynnik uczenia')
    plt.ylabel('% poprawnych odpowiedzi')
    plt.plot(x, ymin, 'r+', label='minimalny uzyskany procent')
    plt.plot(x, ymean, 'bo', label='średni uzyskany procent')
    plt.plot(x, ymax, 'g+', label='maksymalny uzyskany procent')
    plt.show()
def show_range_epochs(x, ymin, ymean ,ymax):
    plt.title('Badanie wpływu zakresu inicjowania wag na szybkość uczenia w epokach')
    plt.xlabel('zakres wag')
    plt.ylabel('epoki')
    plt.plot(x, ymin, 'r+', label='minimalna liczba epok')
    plt.plot(x, ymean, 'bo', label='średnia liczba epok')
    plt.plot(x, ymax, 'g+', label='maksymalna liczba epok')
    plt.show()
def show_range_percentages(x, ymin, ymean, ymax):
    plt.title('Badanie wpływu zakresu inicjowania wag na jakość uczenia w procentach')
    plt.xlabel('zakres wag')
    plt.ylabel('% poprawnych odpowiedzi')
    plt.plot(x, ymin, 'r+', label = 'minimalny uzyskany procent')
    plt.plot(x, ymean, 'bo', label = 'średni uzyskany procent')
    plt.plot(x, ymax, 'g+', label = 'maksymalny uzyskany procent')
    plt.legend
    plt.show()