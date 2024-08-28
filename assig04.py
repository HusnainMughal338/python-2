#calculate age by using the current age value in the database .
def age_calculation(currentyear,birthyear):
    age = currentyear - birthyear
    return age 
result =  age_calculation(2024,2005)
print("The age of Husnain Mughal is", result)

#print(Find the area of Triangle)
def area_of_triangle(length:int,width:int):
    area = length*width
    return area
result = area_of_triangle(12,10)
print("The area of triangle",result)


#(Find the area of a circle)
def area_of_circle(radius:int):
    area = 3.14*(radius**2)
    return area
result = area_of_circle(3)
print("The total area of cube is",result)

#print(Find the area of a cube)
def area_of_cube(surface_area:int):
    area = 6*(surface_area**2)
    return area
result = area_of_cube(6)
print("The total area of a cube is",result)

#print(creat a program to convert tempratre to fahrenheit)
def convert_to_fahrenheit(temprature:int):
    fahrenheit = (1.8*temprature)+32
    return fahrenheit
result = convert_to_fahrenheit(22)
print("To convert temprature into fahrenhiet is",result)

#print(Find the percentage of husnain matric result)
def percentage_of_marks(obtain_marks:int,total_marks:int):
    percentage = (obtain_marks/total_marks)*100
    return percentage
result = percentage_of_marks(966,1100)
print("The percentage of Husnain marks is",result)


#print(Find the volume of a cylinder)
def volume_of_cylinder(radius:int,hight:int):
    volume = 3.14*(radius**2)*hight
    return volume
result = volume_of_cylinder(10,12)
print("The volume of a cylinder is",result)

#print(Calculate the BMI by using height meters and weight in kilograms) 
def BMI_calculate(height:int, weight:int):
    BMI = weight/height**2
    return BMI
result = BMI_calculate(10,12)
print("Body mass index is",result)