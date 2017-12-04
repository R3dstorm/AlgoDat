#! /usr/bin/python3


import time
import math
import matplotlib.pyplot as plt

def read_info_from_file(file):
    """ Read the names of all localities in a GeoNames-File and return them in a list.
    Test the function checking the first 5 GeoNames of the file AT.txt.
    >>> read_info_from_file("../../AT.txt")[:5]
    ['Neu-Guntramsdorf', 'Zwieselstein', 'Zwettl Stift', 'Zistersdorf', 'Zeltweg']

    >>> read_info_from_file("../../AT.txt")[-5:]
    ['Sonnenalpe Nassfeld', 'Haus im Ennstal', 'Hall bei Admont', 'Vandans', 'Hittisau']

    :param file: file to read from, needs to comply with GeoNames.org Format.
    :return: returns a list of all localities contained in file.
    """

    # "Defines":
    localities_identifier_pos = 7 - 1
    localities_country_code_pos = 9-1
    localities_pos = 2 - 1
    inhabitants_pos = 15 - 1

    # TODO test if file is a string

    # Local variables:
    localLine = 0
    localities = []

    startTime = time.clock()

    inputFile = open(file, "r")
    for line in inputFile:
        localLine = inputFile.readline()
        lst = localLine.split("\t")
        if (lst[localities_identifier_pos] == 'P'\
            and int(lst[inhabitants_pos]) > 0)\
            and lst[localities_country_code_pos] == 'DE':
            localities.append(lst[localities_pos])

    stopTime = time.clock()
    print ("runtime of reading file: %f " % (stopTime-startTime))

    return localities


def compute_most_frequent_city_names_by_sorting(localities):
    ''' Sorts the list of localities and prints the most frequent ones with their number of occurrence
    Test the function checking the first 5 GeoNames of the file AT.txt.
    >>> compute_most_frequent_city_names_by_sorting(read_info_from_file("../../AT.txt"))[:5]
    [('Ansfelden', 2), ('Gmünd', 2), ('Absam', 1), ('Abtenau', 1), ('Aichau', 1)]

    :param localities:
    :return: sorted list containing tuplets with unique citynames and number of occurrence
    '''

    localityCounter = 1
    mostFrequentCities = []
    numberLocalities = len(localities)

    startTime = time.clock()
    #sort localities to form blocks
    localities.sort()

    # Count occurrence of cities (size of blocks)
    for i in range(0, numberLocalities - 1):
        currentLocalitiy = localities[i]
        if (localities[i + 1] == currentLocalitiy):
            localityCounter += 1
        else:
            mostFrequentCities.append((currentLocalitiy, localityCounter))
            localityCounter = 1
    # Save last element
    mostFrequentCities.append((localities[numberLocalities - 1], localityCounter))
    stopTime = time.clock()
    print ("runtime sort:%f" % (stopTime-startTime))
    # Sort for largest cities
    mostFrequentCities.sort(key=lambda localityOccurence: localityOccurence[1], reverse=True)

    return mostFrequentCities


def compute_most_frequent_city_names_by_map(localities):
    ''' Sorts the list of localities and prints the most frequent ones with their number of occurrence.
    Test the function checking the first 2 GeoNames of the file AT.txt. Arrangement of results by accident???
    >>> compute_most_frequent_city_names_by_map(read_info_from_file("../../AT.txt"))[:2]
    [('Ansfelden', 2), ('Gmünd', 2)]

    :param localities: list containing the names of localities.
    :return: sorted dictionary containing unique city names with number of occurrence.
    '''

    mostFrequentCities={}
    numberLocalities = len(localities)

    startTime = time.clock()

    for i in range(0, numberLocalities):
        if localities[i] in mostFrequentCities:
            mostFrequentCities[localities[i]] += 1
        else:
            mostFrequentCities[localities[i]] = 1

    stopTime = time.clock()
    print("runtime of map: %f" % (stopTime-startTime))
    mostFrequentCities = sorted(mostFrequentCities.items(), key=lambda pos: pos[1], reverse=True)

    #    if (localities[i] ==  )
    #if ()

    return mostFrequentCities


def compare_runtimes():

    output = ""
    PERF_OUT = open("performance_results.txt", "w")

    # Start time measurement
    start_time = time.clock()
    result = compute_most_frequent_city_names_by_sorting(read_info_from_file("../../allCountries.txt"))[:3]
    stop_time = time.clock()
    for i in range(0,3):
        temp = result[i]
        output += (temp[0] +":\t" + str(temp[1]) + "\n")
    print ("Top frequent cities wordlwide:\n%s \nruntime using sort: %f s \n" % (output, (stop_time-start_time)))
    PERF_OUT.write("""Performance ouptut using "compute_most_frequent_city_names_by_sorting":\n""")
    PERF_OUT.write("Top frequent cities wordlwide:\n%s \nruntime using sort: %f s \n\n" % (output, (stop_time-start_time)))

    start_time = time.clock()
    result = compute_most_frequent_city_names_by_map(read_info_from_file("../../allCountries.txt"))[:3]
    stop_time = time.clock()
    output = ""
    for i in range(0, 3):
        temp = result[i]
        output += (temp[0] + ":\t" + str(temp[1]) + "\n")
    print("Top frequent cities wordlwide:\n%s \nruntime using sort: %f s \n" % (output, (stop_time - start_time)))
    PERF_OUT.write("""Performance ouptut using "compute_most_frequent_city_names_by_sorting":\n""")
    PERF_OUT.write("Top frequent cities wordlwide:\n%s \nruntime using sort: %f s \n\n" % (output, (stop_time - start_time)))

    return 0




if __name__ == '__main__':
    # Call function read_info_from_file
    compare_runtimes()
    compute_most_frequent_city_names_by_sorting(read_info_from_file("../../AT.txt"))
    compute_most_frequent_city_names_by_map(read_info_from_file("../../AT.txt"))
