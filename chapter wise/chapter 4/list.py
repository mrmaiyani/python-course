data = ["Apple", "Orange", 10, 345.06, "Meet", "Suhali"]
# imp note : list can change value on list 

print("All Data:")
print(data)
print("\nPrint Index Of Data:")
print(data[1])

data[0] = "Pineapple" #index 0 is change
print("\nAll Data:")
print(data)
print("\nPrint Index Of Data:")
print(data[0])

print("\nPrint Data of Index Range:")
print(data[1:4]) # Print Range Index

data.append("Radhe") #Add Data
print("\nAll Data:")
print(data)