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

    def pick_numbers(self, length, range_list):
        num_list = []
        for i in range(length):
            x = random.randint(0, len(range_list) - 1)
            num_list.append(random.randint(range_list[x][0], range_list[x][1]))
        return num_list

    def gen_pass(self):
        symbol_range = [[33, 64], [91, 96], [123, 126]]
        word_range = [[65, 80], [97, 122]]
        symbol_list = self.pick_numbers(self.len // self.dist, symbol_range)
        word_list = self.pick_numbers(self.len - self.len // self.dist, word_range)
        pass_list = symbol_list + word_list

        self.int_to_ascii(pass_list)
        random.shuffle(pass_list)
        return ''.join(str(x) for x in pass_list)


password = PasswordGen(100, 4)
print(password.gen_pass())
