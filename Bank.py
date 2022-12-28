_CODE_DELIMITER = '-----'  # constant


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
        result = [self.bank*prosent for prosent in self.get_target_percents()]
        return(result)

    def __str__(self):
        # текстовое представление сделки
        pass

def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()



def parse_data():
    pass


def main():
    a = StrategyDeal(1000, 20.11483, (21.5432423, 22.864732843, 23.556789), 19.093022)
    print(a.get_target_percents())
    # content = read_data('deals.txt')
    # result = content
    # write_data('out.txt', result)


if __name__ == '__main__':
    main()
