INPUT_CODE_DELIMITER = '# ---end----'  # constant


def read_data(file_name):
    file = open(file_name, encoding='utf-8')
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w', encoding='utf-8')
    file.write(data)
    file.close()


def prepare_old_data(data):
    old_links, old_code = data.split('##', 1)
    old_code = '##' + old_code
    return old_links, old_code


def prepare_md_titles(data): # Отделяет название от описания.
    title, description = None, None

    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description'):
            description = line.replace('# description ', '')

    return title, description


def prepare_md_format(title, description, source_code, old_links, old_code): # Оборачиваем в систаксис разметки
    link = '-'.join(title.lower().split()) # название записываем маленькими буквами через -.
    template = "+ [{}](#{})"
    md_link = template.format(title, link)


    template = """
{}
{}

{}

## {}

{}

```python
{}
```"""

    return template.format(old_links.rstrip('\n'), md_link, old_code, title, description, source_code.lstrip())


def convert_data(data, old_data):
    titles, source_code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(titles)
    old_links, old_code = prepare_old_data(old_data)
    result_md = prepare_md_format(title, description, source_code, old_links, old_code)

    return result_md


def main():
    content = read_data('seminar_1.py')
    old = read_data('answer.md')
    result = convert_data(content, old)
    write_data('answer.md', result)


if __name__ == "__main__":
    main()
