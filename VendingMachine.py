POUND_VALUES = [[1, 10],
                [2, 12],
                [5, 6],
                [10, 1],
                [20, 1],
                [50, 1]]
DOLLAR_VALUES = [[1, 12],
                [5, 11],
                [10, 6],
                [25, 5]]
KRONE_VALUES = [[1, 16],
                [5, 9],
                [10, 6],
                [20, 5]]


class VendingMachine:
    def __init__(self, change):
        self.change = change

    def calculate_change(self, tender, purchase):
        # move 100 into calculation because python is stupid
        change = int((tender*100 - purchase*100))
        ans = []

        n = len(self.change)
        # range from 1 less than length to >-1 in decrements of 1
        for i in range(n - 1, -1, -1):
            while change >= self.change[i][0] and self.change[i][1] > 0:
                change -= self.change[i][0]
                self.change[i][1] -= 1
                ans.append(self.change[i][0])

        return ans


if __name__ == '__main__':
    tender_amount = 2
    purchase_amount = 1.25

    vm = VendingMachine(POUND_VALUES)
    print(vm.calculate_change(tender_amount, purchase_amount))

    vm_dollar = VendingMachine(DOLLAR_VALUES)
    print(vm_dollar.calculate_change(tender_amount, purchase_amount))

    vm_krone = VendingMachine(KRONE_VALUES)
    print(vm_krone.calculate_change(tender_amount, purchase_amount))

