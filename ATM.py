class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdraws_list = []

    def give(self, request):
        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.withdraws_list.append(request)
            self.balance -= request

            notes = [100, 50, 10, 5]
            for note in notes:
                while request >= note:
                    request -= note
                    print("give ", str(note))

                if request < 5 and request > 0:
                  print("give " + str(request))
                  request = 0

    def withdraw(self, request):

        print(f"your bank is {self.bank_name}")

        print("Current balance = ", self.balance)

        self.give(request)

    def show_withdraw_list(self):
        print("The withdrawals list is: ")
        for i in self.withdraws_list:
            print(i, end=", ")


atm1 = ATM(700, "baraka bank")

atm1.withdraw(185)
atm1.withdraw(200)
atm1.withdraw(65)
atm1.withdraw(93)

atm1.show_withdraw_list()
