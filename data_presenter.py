data = open("Cupcakeinvoices.csv")


for line in data:
    print(line)
data.seek(0,0)

# data.close()
# data =open('Cupcakeinvoices.csv')
for i in data:
    n = i.split(',')
    print(n[2])

# data.seek(0,0)
# for i in data:
#     n = i.split(',')
#     print(n[3])

data.seek(0,0)
for i in data:
    n = i.split(',')
    invoice = (float(n[3]) * float(n[4]))
    print(invoice)

data.seek(0,0)
total = 0
for i in data:
    n = i.split(',')
    total = total+(float(n[3]) * float(n[4]))

print("this is the total invoice of all items ordered =", total)

data.close()
