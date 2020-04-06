"""
 The logic of this function is:
 - Given the amount of money, add the coin from the smallest value to the largest
 until the total amount surpasses the required amount.
 - Compute the extra amount of coins given.
 - Take out the number of coins from largest value until it is equal to the extra
 amount given.
"""


def getridcoin(amount, coin_list):
    money = int(amount * 100)

    class Coin:
        def __init__(self, value):
            self.value = value
            self.amount = 0
            self.given = 0

        def total(self):
            """

            :rtype: int
            """
            return self.value * self.amount

    # Check if there are more than 5 types of coins
    if len(coin_list) > 5:
        print("WARNING: More coin types than expected!")

    else:

        # Create coin objects so that data can be manipulated more easily
        onedollar = Coin(100)
        fiftycent = Coin(50)
        twentycent = Coin(20)
        tencent = Coin(10)
        fivecent = Coin(5)

        collection = [onedollar, fiftycent, twentycent, tencent, fivecent]
        total_stash = 0

        # Input amount of each coin type from the coin list
        for n in range(0, 5):
            collection[n].amount = int(coin_list[n])

        # Check if there are enough coin for exchange
        for m in range(0, 5):
            total_stash += collection[m].total()

        if total_stash < money:
            print("WARNING: Insufficient coin purse!")

        else:
            # Step 1: Add coins from small value up, until the amount added is larger
            # than the required amount.
            prov_sum = 0
            n = 4

            while n >= 0:
                while collection[n].amount > 0:
                    if prov_sum < money:
                        prov_sum += collection[n].value
                        collection[n].amount -= 1
                        collection[n].given += 1
                    else:
                        break

                n -= 1

            extra = prov_sum - money

            # Step 2: Remove the extra amount of coin, starting from the highest value
            # coin type.
            n = 0
            while n <= 4:

                if extra < collection[n].value:
                    n += 1

                else:

                    while extra > 0:

                        extra -= collection[n].value
                        collection[n].given -= 1

                        if extra - collection[n].value < 0:
                            break

            given_out = []
            for i in range(0, 5):
                given_out.append(collection[i].given)

            print(given_out)

            return given_out


# Test cases:
# input set 1: [3,5,16,2,9] and $4.65
# input set 2: [3,4,6,7,9] and $5.20
# input set 3: [0,2,5,7,8] and $5.50
# input set 4: [1,2,3,4,5,6] and $1.00

list_1 = [4.65, 5.20, 5.20, 1.00]
list_2 = [[3, 5, 16, 2, 9], [3, 4, 6, 7, 9], [0, 2, 5, 7, 8], [1, 2, 3, 4, 5, 6]]

for j in range(0, 4):
    getridcoin(list_1[j], list_2[j])
