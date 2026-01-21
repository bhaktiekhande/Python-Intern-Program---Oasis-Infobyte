# BMI -Body Mass Index

height = float(input("Enter your height in Centemeters :"))
weight = float(input("Enter your weight in Kg : "))

height = height/100
BMI = weight/(height*height)

print("Your Body Mass Index is :", BMI)

if(BMI>0):
    if(BMI<=16):
        print("You are severely underweight")
    elif(BMI<=18.5):
        print("you are underweight") 
    elif(BMI<=25):
        print("You are Healthy")  
    elif(BMI<=30):
        print("you are overweight") 
    else:
        print("You are severely overweight")
else:
    print("Enter valid details....")
       