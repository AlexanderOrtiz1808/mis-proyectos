fuel = 100
space_jumps = 5

while space_jumps > 0:
    expense = int(input("How much fuel was spent on the journey? "))
    space_jumps -= 1
    fuel -= expense
    
    if fuel <= 0:
        print("You have run out of fuel, ship stranded.")
        break

if space_jumps == 0:
    print("Today's space journeys are over.")
    if fuel > 0:
        print(f"✅ Mission successful. You arrived at the destination with {fuel} fuel to spare.")