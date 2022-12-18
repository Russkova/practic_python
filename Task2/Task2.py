
def read_data(file_name):
    file = open(file_name)
    data = file.readlines()
    file.close()
    return data


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


class CsvToJsonConverter:

    def __init__(self, csv_data):
        self.title = csv_data[0]
        self.values = csv_data[1:]

    def prepare_title(self):
        title = self.title.strip().split(',')
        return title

    def prepare_row_values(self):
        values = [row.strip().split(',') for row in self.values]
        return values


    def convert_row_to_json(self, data):
        formatted_values = ",".join([""""{}": {}""".format(key, value) for key, value in data.items()])
        new_line = """{{ {} }}""".format(formatted_values)
        return new_line

    def to_json(self):
        title = self.prepare_title()
        row_values = self.prepare_row_values()

        self.check_data(title, row_values)

        result = [self.convert_row_to_json(dict(zip(title, row))) for row in row_values]
        return "[{}]".format(",".join(result))

    def check_data(self, title, row_values):
        for row in row_values:
            assert len(title) == len(row), "Column count is not equals value count"


def main():
    data = read_data('input.csv')
    if not data:
        print('File is empty.')
        return
    converter = CsvToJsonConverter(data)
    result = CsvToJsonConverter.to_json(converter)
    write_data('output.json', result)



if __name__ == "__main__":
    main()