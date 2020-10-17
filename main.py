#get input for number of people on trip, make sure its less than 1000
#run a loop to get amount spent for each student make sure it 0 < x <= 10000
#get a sum for the for array
#get average using sum and list
#do the math

tripAttendees = int(input("Enter number of trip attendees: "))
spendingAmount = [float(input(f"Enter amount spent by student {i}: ")) for i in range(1, tripAttendees+1)]

averageSpent = sum(spendingAmount) / len(spendingAmount)
total = 0
for i in spendingAmount:
    total += abs(i-averageSpent)

print(total/2)
