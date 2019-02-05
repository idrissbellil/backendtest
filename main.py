from fetchdata import BanksData, merge_sort
import random
import matplotlib.pyplot as plt
import numpy as np

def main():
    banks = BanksData()
    
    # answering the first question
    print('Highest unclaimed CADs : {}'.format(
        banks.highest_unclaimed_CAD()
        ))

    # answering the second question,
    # assuming the the relative highest CAD means
    # the average CADs per bank account
    print('Highest average unclaimed CADs : {}'.format(
        banks.highest_relative_unclaimed_CAD()
        ))

    # Not required but it might help to have an idea
    labels, values = zip(*banks.banks_total_CAD.items())
    indexes = np.arange(len(labels))

    plt.bar(indexes, values, 1)
    plt.xticks(indexes, labels, rotation=90 )
    plt.savefig('banks_CADs.png')

    #
    # Going the extra mile
    #
    # 1- creating the tuple
    banks.create_extra_mile()
    
    # 2- Shuffling
    random.shuffle(banks.extra_mile)

    # 3- merge sorting
    merge_sort(banks.extra_mile)

    # 4- Attempting to find the value "9862.07"
    index = banks.binary_search(9862.07)
    if(banks.extra_mile[index][1]==9862.07):
        print('Value found \n\t{}'.format(banks.extra_mile[index][0]))
    
if __name__ == '__main__':
    main()

