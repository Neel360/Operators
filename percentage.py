english = int(input("Enter your marks for English: "))
science = int(input("Enter your marks for science: "))
maths = int(input("Enter your marks for maths: "))
geography = int(input("Enter your marks for geography: "))

sum = english + science + maths + geography

perc = (sum/400) * 100

print(perc,'%', sep="")