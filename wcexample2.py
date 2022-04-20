import wizcoin

change = wizcoin.WizCoin(9, 7, 20)
print(change.sickles)  # prints 7
change.sickles += 10
print(change.sickles)  # prints 17

pile = wizcoin.WizCoin(2, 3, 31)
print(pile.sickles)  # prints 3
pile.someNewAttribute = 'A new attr'  # A new attribute is created.
print(pile.someNewAttribute)