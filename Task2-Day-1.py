print("*****************WELCOME TO MARANGI PAINTING COMPANY******************")

constant_wallsize = 115

# getting the wall size from the user
wall_size = int(
    input("Enter the The Square Size of the wall in metres squared"))
# Getting the paint price rate of a gallon from the user
paint_price = int(input("Enter price of paint per Gallon"))


# Calculating the number of paint gallons required
number_of_paint_gallons = wall_size/constant_wallsize

# Calculating the number of labour hours required
labour_hours = number_of_paint_gallons*8

# Calalculating number of labour charges required
labour_charges = labour_hours*20

# Calculating the total cost of paint
cost_of_paint = number_of_paint_gallons * paint_price

# Calclating the total cost of the Painting Job
total_cost = cost_of_paint+labour_charges

print("The Number of Gallons required are\t",
      number_of_paint_gallons, "Gallons")

print("The number of labour Hours\t\t", labour_hours, " hrs")

print("The labour charges are\t\t \t$", labour_charges)

print("The cost of paint is\t\t \t$", cost_of_paint)

print("The Total Cost of the Painting Job is\t$", total_cost)
