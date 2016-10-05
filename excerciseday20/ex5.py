count = 0
sum = 0
numbers = []
highest = None
lowest = None
while True:
    try:
        line = input("enter a number or enter to finish: ")
        if line:
            number = int(line)
            # if highest == None and lowest == None:
            #     highest = number
            #     lowest = number
            if highest == None or number > highest:
                highest = number
            if lowest == None or number < lowest:
                lowest = number
            count += 1
            sum += number
            numbers.append(number)
        else:
            break
    except ValueError as err:
        print(err)
print(numbers)

def sort_list(the_list):
    n = len(the_list)
    for i in range(n):
        for j in range(1, n-i):
            if the_list[j-1] > the_list[j]:
                the_list[j-1], the_list[j] = the_list[j], the_list[j-1]
    return the_list

print(sort_list(numbers))
print('count: '+str(count)+'\tsum: '+str(sum)+'\tlowest: '+str(lowest)+'\thighest: '+
      str(highest)+'\tmean: '+str(sum/count))