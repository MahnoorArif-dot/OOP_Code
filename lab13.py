class NUMBERS:
    def __init__(self):
        self.odd_numbers = []
        self.even_numbers = []

    def add(self, num):
        if num % 2 == 0:
            self.even_numbers.append(num)
        else:
            self.odd_numbers.append(num)

    def delete(self, num):
        if num % 2 == 0:
            self.even_numbers.remove(num)
        else:
            self.odd_numbers.remove(num)

    def alter(self, old_num, new_num):
        if old_num % 2 == 0:
            self.even_numbers[self.even_numbers.index(old_num)] = new_num
        else:
            self.odd_numbers[self.odd_numbers.index(old_num)] = new_num

    def search(self, num):
        if num % 2 == 0:
            return self.even_numbers.index(num)
        else:
            return self.odd_numbers.index(num)

    def print_all_numbers(self):
        print(self.odd_numbers + self.even_numbers)

    def __getitem__(self, index):
        all_numbers = self.odd_numbers + self.even_numbers
        return all_numbers[index]

    def __setitem__(self, index, value):
        all_numbers = self.odd_numbers + self.even_numbers
        all_numbers[index] = value
        self.odd_numbers, self.even_numbers = [], []
        for num in all_numbers:
            self.add(num)

    def __iter__(self):
        self.index = -1
        self.all_numbers = self.odd_numbers + self.even_numbers
        return self

    def __next__(self):
        if self.index + 1 >= len(self.all_numbers):
            raise StopIteration
        self.index += 1
        return self.all_numbers[self.index]
def main():
    numbers_list = NUMBERS()
    numbers_list.add(3)
    numbers_list.add(6)
    numbers_list.add(1)
    numbers_list.add(8)
    print("All Numbers:")
    numbers_list.print_all_numbers()
    print("\nIterating through numbers using iterator:")
    for num in numbers_list:
        print(num)
    print("\nNumber at index 2:", numbers_list[2])
    search_result = numbers_list.search(6)
    if search_result != -1:
        print("\nNumber 6 found at index:", search_result)
    else:
        print("\nNumber 6 not found.")
    numbers_list.delete(6)
    print("\nAll Numbers after deleting 6:")
    numbers_list.print_all_numbers()
    numbers_list.alter(1, 7)
    print("\nAll Numbers after altering 1 to 7:")
    numbers_list.print_all_numbers()
    numbers_list[1] = 5
    print("\nAll Numbers after setting index 1 to 5:")
    numbers_list.print_all_numbers()

if __name__ == "__main__":
    main()


