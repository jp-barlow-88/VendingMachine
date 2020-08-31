import VendingMachine as vm
import unittest


class Test(unittest.TestCase):

    def test_pound(self):
        vending_machine = vm.VendingMachine(vm.POUND_VALUES)
        self.assertEqual(vending_machine.calculate_change(2, 1.25), [50, 20, 5])

    def test_dollar(self):
        vending_machine = vm.VendingMachine(vm.DOLLAR_VALUES)
        self.assertEqual(vending_machine.calculate_change(2, 1.25), [25, 25, 25])

    def test_krone(self):
        vending_machine = vm.VendingMachine(vm.KRONE_VALUES)
        self.assertEqual(vending_machine.calculate_change(2, 1.25), [20, 20, 20, 10, 5])


if __name__ == '__main__':
    unittest.main()
