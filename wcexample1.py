import wizcoin

purse = wizcoin.WizCoin(2, 5, 99)  # The ints are passed to __init__().
print(purse)
print('G:', purse.galleons, 'S:', purse.sickles, 'K:', purse.knuts)
print('Total value:', purse.value())
print('Weight:', purse.weightInGrams(), 'grams')

print()

coinJar = wizcoin.WizCoin(13, 0, 0)
print(coinJar)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print('Total Value:', coinJar.value())
print('Weight:', coinJar.weightInGrams())

# Attributes

