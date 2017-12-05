#testing my own kol2

import unittest
from kol2 import Client
from kol2 import Bank
from kol2 import Transaction




class BankTest(unittest.TestCase):


    def setUp(self):
        self.name = "Jan"
        self.surname = "Kowalski"
        self.cash = 100
        self.test_client = Client(self.name,self.surname, self.cash,)
        self.test_client_2 = Client("Anna", "Kowalska", 100)
        self.test_bank = Bank()
        self.test_transaction = Transaction()


    def test_init_Client(self):
        self.assertEqual(self.test_client.name, self.name)
        self.assertEqual(self.test_client.surname, self.surname)
        self.assertEqual(self.test_client.cash, self.cash)

    def test_add_client(self):
        self.test_bank.add_client(self.test_client)
        self.test_bank.add_client(self.test_client_2)
        self.test_bank.data[0].print_client()
        self.test_bank.data[1].print_client()
        self.assertEqual(self.test_bank.data[0].name, self.name)
        self.assertEqual(self.test_bank.data[0].surname, self.surname)
        self.assertEqual(self.test_bank.data[0].cash, self.cash)

    def test_add_bank(self):
        self.test_transaction.add_bank(self.test_bank)
        self.assertEqual(self.test_transaction.banks[0], self.test_bank)

    def test_input(self):
        self.test_bank.input(self.test_bank.data[0],300)
        self.assertEqual(self.test_bank.data[0].cash, 400)

    def test_withdrawal(self):
        self.test_bank.withdrawal(self.test_bank.data[0],100)
        self.assertEqual(self.test_bank.data[0].cash, 300)

    def test_transfer(self):
        self.test_bank.add_client(self.test_client_2)
        self.test_bank.transfer(self.test_bank.data[0], self.test_bank.data[1], 50)
        self.assertEqual(self.test_bank.data[0].cash, 250)
        self.assertEqual(self.test_bank.data[1].cash, 150)

