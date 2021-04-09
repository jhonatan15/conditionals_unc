condition_1 = 10
condition_2 = 20

if(condition_1 > condition_2):
    print(condition_1, " es mayor que ", condition_2)
else:
    print(condition_1, " no es mayor que ", condition_2)



rain = input("It is raining? Yes/No ")
print(rain)
if (rain == "Yes" or rain == "yes" or rain == "YES"):
    print("You must bring an umbrella")
elif (rain == "No" or rain == "NO" or rain == "no"):
    print("You don't need an umbrella")
else:
    print("You must enter yes or no")
