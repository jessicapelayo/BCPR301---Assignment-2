"""
    >>> myModel = Model()
    >>> myModel.read_in_csv("TestData.csv")
    loading file...
    File Loaded!

    >>> integer = myModel.wash_data().__len__()
    >>> integer
    7


"""
import re
import pickle


class Model:
    def __init__(self):
        self.data_set = list()
        self.display_data = list()
        self.wrong_data = list()
        self.file_there = ""

    def add_new_data(self, new_array):
        # try catch if its a list
        self.data_set += new_array

    def del_data(self):
        self.data_set = list()

    def get_data_set(self):
        return self.data_set

    def get_data(self):
        return self.display_data

    def get_data_set_length(self):
        return self.data_set.__len__()

    def read_in_csv(self, path):
        print("loading file...")
        file = open(path)
        txt = file.read()
        li = txt.split('\n')
        if li[-1].strip() == '':
            del li[-1]
        self.add_new_data(li)
        if self.data_set is not []:
            print("File Loaded!")
        #self.wash_data()

    def delete_bad(self):
        for item in self.wrong_data:
            self.data_set.remove(item)

    def wash_data(self):
        RULES = ['^[A-Z][0-9]{3}$', '(M|F)', '[0-9]{2}$', '[0-9]{3}$', '(Normal|Overweight|Obesity|Underweight)', '[0-9]{2,3}$']
        for line in self.data_set:
            tmp = line.split(',')
            i = 0
            for item in tmp:
                result = re.match(RULES[i], item)
                i += 1
                if result == None:
                    self.wrong_data.append(line)
        self.delete_bad()
        return self.data_set

    def save_data(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.display_data, f)

    def pickle_data(self):
        try:
            with open('data.pickle', 'rb') as f:
                self.display_data = pickle.load(f)
        except FileNotFoundError:
            print("Existing data not found.")
            return

    def get_sales(self):
        result = []
        for i in self.display_data:
            result.append(int(i[3]))
        return result

    def get_weight(self):
        normal = 0
        over = 0
        obese = 0
        under = 0
        for i in self.display_data:
            if i[4] == 'Normal':
                normal += 1
            elif i[4] == 'Overweight':
                over += 1
            elif i[4] == 'Obesity':
                obese += 1
            elif i[4] == 'Underweight':
                under += 1
        return [normal, over, obese, under]

    def get_gender(self):
        m = 0
        f = 0
        for i in self.display_data:
            if i[1] == 'M':
                m += 1
            elif i[1] == 'F':
                f += 1
        return [m, f]

