# Prototyping Coin object


class Coin:
    def __init__(self, value):
        self.value = value
        self.amount = 0
        self.given = 0

    def total(self):
        return self.value * self.amount


#         MAIN PROGRAMME
""" 
 The logic of this programme is:
 - Given the amount of money, add the coin from the smallest value to the largest
 until the total amount surpasses the required amount.
 - Compute the extra amount of coins given.
 - Take out the number of coins from largest value until it is equal to the extra
 amount given.
"""

money = int(round(100 * float(input("Amount to be exchanged is:"))))

print("\n")

#           Create coin objects with values in term of cents
oneD = Coin(100)
fiftyC = Coin(50)
twentyC = Coin(20)
tenC = Coin(10)
fiveC = Coin(5)

# Ask user to input number of coins in the form of a list

print("***Enter the amount for each type of coin in the following order")
print("from 1 dollar, 50 cents, 20 cents, 10 cents and 5 cents. ")
print("Use comma to separate the inputs.***")

amount_string = input("Please enter the amount for each type of coins:")
amount_list = amount_string.split(",")

if len(amount_list) > 5:  # Check if there are more than five types of coin
    print("\n***ERROR: THERE ARE ONLY FIVE TYPES OF COINS IN SINGAPORE!!!***")

else:
    print("\n This is your current coin stash in decreasing order \n from one dollars to five cents")
    print(amount_list)

    collection = [oneD, fiftyC, twentyC, tenC, fiveC]
    for n in range(0, 5):
        collection[n].amount = int(amount_list[n])

    total_stash = 0
    for i in range(0, 5):
        total_stash += collection[i].total()

    if total_stash < money:  # Check if there are enough coins
        print("*** ERROR:  THE AMOUNT OF COINS IS INSUFFICIENT!  ***")

    else:
        #       Gradually add coins to the returning stash
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

        # take out the extra coins in order of decreasing values
        extra = prov_sum - money

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

        #  Printing the output

        """This could be a nicer way to show the combination"""
        # print("The combination of coins would be: \n")
        # print("\tThe number of $1 coins given = " + str(oneD.given))
        # print("\tThe number of 50 cent coins given = " + str(fiftyC.given))
        # print("\tThe number of 20 cent coins given = " + str(twentyC.given))
        # print("\tThe number of 10 cent coins given = " + str(tenC.given))
        # print("\tThe number of 5 cent coins given = " + str(fiveC.given))

        given_out = []
        for a in range(0, 5):
            given_out.append(collection[a].given)
        print("The combination of coins given out, starting from 1 dollar, is:")
        print(given_out)

# END OF PROGRAMME

#Test cases:
# input set 1: [3,5,16,2,9] and $4.65
# input set 2: [3,4,6,7,9] and $5.20
# input set 3: [0,2,5,7,8] and $5.50
# input set 4: [1,2,3,4,5,6] and $1.00