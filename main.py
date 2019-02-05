from fetchdata import BanksData
import matplotlib.pyplot as plt
import numpy as np

def main():
    banks = BanksData()
    
    print('Highest unclaimed CADs : {}'.format(
        banks.highest_unclaimed_CAD()
        ))

    print('Highest average unclaimed CADs : {}'.format(
        banks.highest_relative_unclaimed_CAD()
        ))

    labels, values = zip(*banks.banks_total_CAD.items())
    indexes = np.arange(len(labels))

    plt.bar(indexes, values, 1)
    plt.xticks(indexes, labels, rotation=90 )
    plt.savefig('banks_CADs.png')
    
if __name__ == '__main__':
    main()

