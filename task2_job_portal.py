# task 2 job eligibility
print("Welcome to the job eligibility")
python = input("Do you know python? (yes / no) :").strip().lower()
experience = int(input("enter your years of experience or number of projects"))
certificate = input("do u have a computer science degree or bootcamp certificate? (yes /no) :").strip().lower()
if python == "yes" and (experience >= 2 or certificate == "yes") :
   print("congratulation! u have been accepted")
else :
 print ("U not qualified")
 print("#" * 30)   