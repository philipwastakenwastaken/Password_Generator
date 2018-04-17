import random


class PasswordGen:

    def __init__(self, len, dist):
        self.len = len
        self.dist = dist

    # generates password from ASCII codes [33;126]
    def gen_pass_simp(self):
        pass_string = ''
        for i in range(self.len):
            pass_string += chr(random.randint(33, 126))
        return pass_string

    def int_to_ascii(self, pass_list):
        for index, val in enumerate(pass_list):
            pass_list[index] = chr(val)

    def gen_pass(self, symbol_range_list, word_range_list):
        pass_list = self.create_pass_list(symbol_range_list, word_range_list)
        self.int_to_ascii(pass_list)
        random.shuffle(pass_list)
        return ''.join(str(x) for x in pass_list)

    def gen_pass_symbols(self):
        symbol_range_list = list(range(33, 65)) + list(range(91, 97)) + list(range(123, 127))
        word_range_list = list(range(65, 81)) + list(range(97, 123))
        return self.gen_pass(symbol_range_list, word_range_list)

    def gen_pass_no_symbols(self):
        word_range_list = list(range(65, 81)) + list(range(97, 123))
        symbol_range_list = list(range(48, 58))
        return self.gen_pass(symbol_range_list, word_range_list)

    def pick_numbers(self, length, range_list):
        num_list = []
        for x in range(length):
            num_list.append(random.choice(range_list))
        return num_list

    def create_pass_list(self, symbol_range_list, word_range_list):
        return self.pick_numbers(self.len // self.dist, symbol_range_list) + self.pick_numbers(self.len - self.len // self.dist, word_range_list)
