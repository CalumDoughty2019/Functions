#legacy method
print("legacy method")
print("================")
print("Name is Jimmy", "Jimmy")
print("Name: " '%s %s' % ('Peter', 'Capaldi'))
print("Age: " '%d' " yrs " '%d' " mths " % (56, 9))
print("Cost: " '%f' % 56.99)
print("Cost: " '%10.2f' % 56.99)
print("Quantity " '%5d' " Unit Price " '%8.2f' " Total Cost " '%10.2f' % (15, 3.895, 15*3.895))

#.format method (current method)
print()
print(".format method")
print("================")
print("Name: {0} {1}".format("Peter", "Capaldi"))
print("Age: {0}yrs {1}mths".format(56, 9))
print("Quantity {0:5d} Unit price {1:8.2f} Total Cost {2:10.2f}".format(15, 3.895, 15*3.895))