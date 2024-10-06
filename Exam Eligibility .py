medical_cause=input("did you have a medicals cause Y or N: ")
atten = int(input("enter the attendence of your student: "))

if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten>=75:
        print ("you are allowed")
    else:
        print("Not allowed")