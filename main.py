#This will be the main code/ an initiator for the code we will write
Names = []
Section = []
Scores = []
def score_to_grade(grd):
  if grd>=85:
     print("Grade: A")
  elif 85>grd>=70 :
     return("Grade: B")
  elif 70>grd>=50:
     return("Grade: C")
  elif 50>grd>=40:
      return("Grade: D")
  elif grd<40:
     return("Grade: F")

  
while True:
    n = str(input("Please enter a student's name: "))
    sec = str(input("Please the student's section: "))
    s= int(input("Enter a student's grade: ") )
    STG =  score_to_grade(s)
    Names += n
    Section += sec
    Scores += STG
    choice = input('Would you like to sumbit the grade of another student?(Y/N) ')
    if choice.lower() == 'y':
       break
    elif choice.lower() == 'n':
       pass
    else:
       break    
  
#Here we will have the code to compare the grades of sections
cs = input("Please input the section's you want to compare.(Eg:- 2,3): ")
def compare_section(sec1, sec2):
   if sec1 == sec2:
      #something happens here
      pass
   elif sec1 >= sec2:
      #another thing also happens here
      pass
   elif sec1 <= sec2:
      #You would never guess
      #Something else would also happen
      pass
   
