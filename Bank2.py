import string

INPUT_CODE_DELIMITER = '-----'  # constant


class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.target1, self.target2, self.target3 = targets
        self.close = close

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return([self.target1, self.target2, self.target3])


    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        result = [round((target - self.entry)*100/self.entry, 3) for target in self.get_targets()]
        return result

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        result = [round(self.bank*(percent/100+1), 3) for percent in self.get_target_percents()]
        return result

    def __str__(self):
        # текстовое представление сделки
        i = 1
        str_target = ''
        for target in self.get_targets():
            str_target = str_target + str(i) + ' target: ' + str(target) + '\n' + 'Percent: ' +str(
                self.get_target_percents()[i-1]) + '\n' + "Bank: " + str(self.get_target_banks()[i-1]) + '\n\n'
            i+=1
        string = ('BANK: '+ str(self.bank) +'\n'+ 'START_PRISE: '+ str(self.entry) +'\n'+ 'STOP_PRISE: '+ str(
            self.close) + '\n' + 'STOP_PERCENT: '+ str(round((self.close-self.entry)*100/self.entry,
                 3)) + '\n' +'STOP_BANK: ' + str(round(((self.close-self.entry)/self.entry +1)*self.bank, 3))+ '\n\n' +
                  str_target)
        return string


def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()



def parse_data(data):
    list_of_deals = data.split(INPUT_CODE_DELIMITER)
    list_of_banks = []
    for bank in list_of_deals:
        bank = bank.strip()
        bank = bank.split('\n')
        bank_data = {}
        for line in bank:
            if line[:4] =='Bank':
                line = line.strip(' \n:'+string.ascii_letters)
                bank_data['Bank'] = float(line)
            if line[:5] == 'Entry':
                line = line.strip(' \n:' + string.ascii_letters)
                bank_data['Entry'] = float(line)
            if line[:5] == 'Close':
                line = line.strip(' \n:' + string.ascii_letters)
                bank_data['Close'] = float(line)
            if line[:6] == 'Target':
                targets = line.split(';')
                Targets_list = []
                for target in targets:
                    target = float(target.strip(' \n:' + string.ascii_letters))
                    Targets_list.append(target)
                bank_data['Targets'] = tuple(Targets_list)
        list_of_banks.append(bank_data)
    return list_of_banks


def list_class_object(data):
    list_of_banks = parse_data(data)
    list_strategyDeal = []
    for banks in list_of_banks:
        if banks:
            list_strategyDeal.append(StrategyDeal(banks['Bank'], banks['Entry'], banks['Targets'], banks['Close']))
    return list_strategyDeal

def str_for_out(data):
    list_strategyDeal = list_class_object(data)
    string = ''
    for bank in list_strategyDeal:
        string = string+str(bank)
    return string



def main():
    a = StrategyDeal(1000, 20.11483, (21.5432423, 22.864732843, 23.556789), 19.093022)
    #print(a)
    content = read_data('deal.txt')
    out = str_for_out(content)
    write_data('out.txt', out)


if __name__ == '__main__':
    main()
