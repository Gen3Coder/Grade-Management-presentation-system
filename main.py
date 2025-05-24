#This will be the main code/ an initiator for the code we will write
Names = []
Section = []
SAS  = []
Scores = []
a = ''
b = ''
def score_to_grade(grd):
  if grd>=85:
     return("Grade: A")
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
    Names.append(n)
    Section.append(sec)
    Scores.append(STG)
    for score, sect in zip(Scores, Section):
       pair = f"{score}:{sect}"
       if pair not in SAS:
        SAS.append(pair)
    choice = input('Would you like to sumbit the grade of another student?(Y/N) ')
    if choice.lower() == 'y':
       pass
    elif choice.lower() == 'n':
       break
    else:
       break    

print(SAS)
#Here we will have the code to compare the grades of sections
cs = input("Please input the section's you want to compare.(Eg:- 2,3): ")
a, b = cs.split(',')
def compare_section(sec1, sec2):
   if sec1 == sec2:
      return('{}')
   elif sec1 >= sec2:
      #another thing also happens here
      pass
   elif sec1 <= sec2:
      #You would never guess
      #Something else would also happen
      pass
   
