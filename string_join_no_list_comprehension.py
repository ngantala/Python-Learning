record = "x.example.com"

spliting = record.split(".")
print(spliting)

new_list = []

for i in range(len(spliting)-1):
    new_list.append(".".join(spliting[i:]))
    print(new_list)
