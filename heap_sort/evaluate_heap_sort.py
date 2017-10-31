#! /usr/bin/python3


import random
import time
import math
from heapSort import heap_sort

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
#
# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C, S = np.cos(X), np.sin(X)
#
# plt.plot(X, C)
# plt.plot(X, S)
#
# plt.show()


def plot_runtime ():
    """

    :return:
    """

# Generate Heapsort runtime plot T(n) with different input sizes n as shown in lecture "minsort".
# Choose appropriate sizes to get a meaningful plot with enough data points and reasonable runtime (1 minute).


    X = [0]
    run_time = [0]
    PERF_OUT = open ("performance_results.txt", "w")

    # Generate arrays with big data sizes...
    for i in range(8):
        n = int(math.pow(10,i))
        data = generate_Data(n)

        # Start time measurement
        start_time = time.clock()

        # Start sorting
        data = heap_sort(data)

        # Stop time measurement
        stop_time = time.clock()

        # Plot running time
        X.append(n)
        runtime_in_seconds = stop_time - start_time
        run_time.append(runtime_in_seconds)
        PERF_OUT.write("%d\t%.1f\n" % (n, runtime_in_seconds))

    PERF_OUT.close()
    plt.plot(X, run_time)
    plt.show()
    return 0


def generate_Data (number_data):

    array = [1]
    for i in range (number_data):
        array.append(int(random.random()*10000))

    return array


if __name__ == "__main__":
    # Create an unsorted list of integers.
    # numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9, 12 ,15 ,17, 11, 166, 16, 2]
    # Sort the list.
    plot_runtime()
    #print(generate_Data(10))