import yaml

def read_file():

     with open('./file/file.yaml', 'r', encoding='utf_8') as f:
        data = yaml.load(f)
        data1 = data['test']

        list = []
        for i in data1:
            list.append(data1[i])

        return list

if __name__ == '__main__':
    read_file()
