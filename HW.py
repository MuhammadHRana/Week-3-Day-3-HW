# # PROBLEM #1
# # Filter out all of the empty strings from the list below
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

full_places = list(filter(lambda x:len(x.replace(" ", "")) >1, places))
print(full_places)

# # PROBLEM #2
# # Write an anonymous function that sorts this list by the last name...
# # Hint: Use the ".sort()" method and access the key"

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

sorter = sorted(authors, key=lambda x: x.split()[-1].lower())
print(sorter)


# # PROBLEM #3
# # Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]


for k,v in enumerate(map(lambda x: x[-1]*(9/5) + 32, places)): places[k] = (places[k][0], v)
print(places)


# #PROBLEM #4
# # Write a recursive function that returns the fibonacci sequence up to the number passed in

# # 1, 1, 2, 3, 5, 8, 13, 21, 34


seq=[1,1]
def fib(num):
    # base case/a condition for your function to stop running
    if num <= 2:
        print(seq)
        return seq
    else:
        seq.append(seq[-1] + seq[-2])
        return fib(num-1)

fib(15)