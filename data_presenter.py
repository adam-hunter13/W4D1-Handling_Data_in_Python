# Question 2-3

open_file = open('Cupcakeinvoices.csv')
for line in open_file:
    print(line)
open_file.close()

# Question 4


cupcakes = open('Cupcakeinvoices.csv')
total_chocolate = 0
total_vanilla = 0
total_strawberry = 0

for line in cupcakes:
  line = line.rstrip('\n').split(',')
  for value in line:
    if value == 'Chocolate':
      total_chocolate += 1
    elif value == 'Vanilla':
      total_vanilla += 1
    elif value == 'Strawberry':
      total_strawberry += 1

print(total_chocolate,total_vanilla,total_strawberry)

# Question 5
# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

cupcakes = open('Cupcakeinvoices.csv')


for line in cupcakes:
    line = line.rstrip('\n').split(',')
    totalPrice = int(line [3]) * float(line[4])

    print(totalPrice)


# Question 6
# Loop through all the data, and print out the total for all invoices combined.
cupcakes = open('Cupcakeinvoices.csv')
datTotal = []

for line in cupcakes:
    line = line.rstrip('\n').split(',')
    totalPrice = int(line [3]) * float(line[4])
    datTotal.append(totalPrice)

    print(datTotal)

total = sum(datTotal)
print('Sum of list elements is', total)

# Question 7
# Close your open file.

open_file.close()