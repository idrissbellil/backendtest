import requests
from collections import Counter


class BanksData:
    def __init__(self,url='https://opendata.socrata.com/resource/n2rk-fwkj.json'):
        self.url = url
        self.data = []
        self.banks = Counter()
        self.banks['__undefined__'] = []

    def fetchdata(self):
        try :
            response = requests.get(self.url)
            data = response.json()
            self.data = data

        except Exception as e:
            print(e)

    def create_counter(self):
        for entry in self.data :
            try :
                if entry['bank_name'].upper() not in self.banks.keys():
                    self.banks[entry['bank_name'].upper()] = []
                if('balance' in entry.keys()):
                    entry['balance'] = float(entry['balance'])
                else :
                    entry['balance'] = 0.
                self.banks[entry['bank_name'].upper()].append(entry)

            except KeyError:
                print('No bank name found, adding to "__undefined__"')
                self.banks['__undefined__'].append(entry)

            except ValueError:
                print('ignoring entry...')
                continue

    def highest_unclaimed_CAD(self):
        pass

    def highest_relative_unclaimed_CAD(self):
        pass

    def shuffle(self):
        pass

    def merge_sort(self):
        pass

    def binary_search(self, balance):
        pass

