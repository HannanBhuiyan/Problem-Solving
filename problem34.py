# problem : Write a Python program to display your details like name, age, address in three different lines
# way one
name, age, address = "jhon", 20, "Dhaka"
print("Name {}\nAge {}\nAddress {}".format(name, age, address))

# way two
name, age, address = "jhon", 20, "Dhaka"
print(f"Name is {name}\nAge is {age}\nAddress is {address}")

# way three
name, age, address = "jhon", 20, "Dhaka"
print(f"Name is %s\nAge is %s\nAddress is %s" %(name, age, address))