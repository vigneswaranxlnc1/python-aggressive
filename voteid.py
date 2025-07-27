collage_from = str(input("Enter the collage from: "))
print("Welcome to the Student Vote ID Collector!")
student_name = str(input("Enter your full name: "))
student_age = int(input("Enter your age: "))



print("-----Student Vote ID-----")
if student_age >= 18:
    print("Hey !", student_name ,"welcome to college election Hope you are back for the election ")
    print("You are eligible to vote.")
    print("Collage From:", collage_from)
else:
    print("Sorry guys, you are not eligible to vote right now once you become eligible you can vote.")
    print("You are not eligible to vote.")
    print("Collage From:", collage_from)
