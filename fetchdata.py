import requests
from collections import Counter


class BanksData:
    def __init__(self,url='https://opendata.socrata.com/resource/n2rk-fwkj.json'):
        self.url = url
        self.data = []
        self.banks = Counter()
        self.banks['__undefined__'] = []
        self.banks_total_CAD = dict()

        self.fetchdata()
        self.create_counter()
        self.compute_total_CAD()


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

    def compute_total_CAD(self):
        for bank_name in self.banks:
            if bank_name == '__undefined__':
                continue
            bank = self.banks[bank_name]
            total_balance = 0.
            for entry in bank:
                total_balance += entry['balance']
            self.banks_total_CAD[bank_name] = total_balance
        
    def highest_unclaimed_CAD(self):
        if not self.banks_total_CAD:
            self.compute_total_CAD()

        key_list = list(self.banks_total_CAD.keys())
        highest_key = key_list[0]
        highest_CAD = self.banks_total_CAD[highest_key]
        for key in key_list[1:]:
            if self.banks_total_CAD[key] > highest_CAD:
                highest_CAD = self.banks_total_CAD[key]
                highest_key = key
        return highest_key

    def highest_relative_unclaimed_CAD(self):
        if not self.banks_total_CAD:
            self.compute_total_CAD()

        key_list = list(self.banks_total_CAD.keys())
        highest_rel_key = key_list[0]
        highest_rel_CAD = self.banks_total_CAD[highest_rel_key] / \
                len(self.banks[highest_rel_key])

        for key in key_list[1:]:
            rel_CAD = self.banks_total_CAD[key] / \
                len(self.banks[key])

            if rel_CAD > highest_rel_CAD:
                highest_rel_CAD = self.banks_total_CAD[key]
                highest_rel_key = key

        return highest_rel_key


    def shuffle(self):
        pass

    def merge_sort(self):
        pass

    def binary_search(self, balance):
        pass

