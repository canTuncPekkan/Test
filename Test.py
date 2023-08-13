from termcolor import colored
from time import time


def function(func, inList: list, expectedOutput, printResolt: bool = True) -> list:
    """Tests a function and tells where it failed

    Args:
        func (function): the name of the function to be tested
        input (list): the prameters you want to input to the function. every elament of the list is a separet pramiter
        output (any): the output you expect from your function with input as a pramiter
        printResolt (bool, optional): shuod the function print the resolt. Defaults to True.

    Returns:
        list[0] (bool): did the function work as intended
        list[1] (floot): the time it took to finish
        list[2] (str): color coded output of where the output was not intended.(green: as intended, red: not intended)
    """
    time0 = time()
    output = func(*inList)
    time1 = time()
    resultList = [True if output == expectedOutput else False, time1 - time0]
    output = str(output)
    expectedOutput = str(expectedOutput)
    coloredStr = ""
    for i in range(len(output) - 1):
        try:
            if output[i] == expectedOutput[i]:
                coloredStr += colored(output[i], "light_green")
            else:
                coloredStr += colored(output[i], "light_red")
        except:
            coloredStr += colored(output[i], "light_red")
    if printResolt:
        print(f"\nit took: {resultList[1]} seconds\nresolt is {resultList[0]}: {coloredStr}\n\n")
    return resultList.append(coloredStr)
