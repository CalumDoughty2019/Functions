import math

def jinkeesVelma(labour, oil):
    oilFilter = 9.99
    labourCost = labour * 45.5
    oilCost = oil * 5.85
    return oilFilter+labourCost+oilCost


print("CUSTOMER")
customer_firstName = input("Enter your first name ")
customer_secondName = input("Enter your surname ")
address = input("What is your street address? ")
postcode = input("What is your postcode? ")
print("CAR")
make = input("What is the make of car? ")
model = input("What is the model of car? ")
reg = input("What is the registration of the car? ")
print("SERVICING")
labour = float(input("How long was spent on the job (hrs)? "))
oil = float(input("How much oil was used (ltrs)? "))

print()
print("======================================================")
print("======================RECIEPT=========================")
print("======================================================")
print("Customer Name: " + customer_firstName + " " + customer_secondName)
print("First line of Address: " + address)
print("Postcode: " + postcode)
print("Car: " + make + " " + model)
print()
print("---Servicing---")
oilFilter = 9.99
labourCost = labour * 45.5
oilCost = oil * 5.85
totalCost = oilFilter + labourCost + oilCost
print("Oil Filter replacement: £" + str(oilFilter))
print("Labour: " + str(labour) + "hours x £45.50 hourly rate")
print("Cost of labour: £" + str(labourCost))
print("Engine oil: " + str(oil) + "litres x £5.85 per litre")
print("Cost of engine oil: £" + str(oilCost))
print()
print("TOTAL: £{0:.2f}".format(totalCost))
print()
print("======================================================")
