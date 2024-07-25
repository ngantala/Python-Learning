record = "x.example.com"
splitting = record.split(".")
print(splitting)

rejoin = [".".join(splitting)]
print(rejoin)

print([".".join(splitting[i:]) for i in range(len(splitting))])

print([".".join(splitting[i:]) for i in range(len(splitting)-1)])


print([i for i in range(5)])
