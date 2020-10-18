import math
# Pi = math.pi

# -----------------------
# This section gets everything ready for the next section.

# Get input from user.
print("Enter radius: ")
radius = input()
print("Enter arc angle: ")
arc_angle = input()

# Cast to floats
r = float(radius)
a = float(arc_angle)

#-----------------------
# This section does the maths bit.

# Finds proportion
proportion = a / 360

# Finds area
area = math.pi * (r*r)
rounded_area = round(area, 3)

# Finds circumference
circumference = (2 * math.pi) * r
rounded_circumference = round(circumference, 3)

# Finds sector area
sector_area = area * proportion
rounded_sector_area = round(sector_area, 3)

# Finds arc length
arc_length = circumference * proportion
rounded_arc_length = round(arc_length, 3)

#-----------------------
# This section prints the answers.

# Print answer
print("Answers")
print("Area = ", area)
print("Circumference = ", circumference)
print("Sector area = ", sector_area)
print("Arc Length = ", arc_length)

# Print rounded answers
print ("Rounded values:")
print("Area = ", rounded_area)
print("Circumference = ", rounded_circumference)
print("Sector area = ", rounded_sector_area)
print("Arc Length = ", rounded_arc_length)