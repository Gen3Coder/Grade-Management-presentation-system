#This will be the main code/ an initiator for the code we will write
Names = []
Section = []
SAS  = []
Scores = []
a = ''
b = ''
 n = str(input("Please enter a student's name: "))
    sec = str(input("Please the student's section: "))
    grd= int(input("Enter a student's grade: ") )
    STG =  score_to_grade(s)
    Names.append(n)
    Section.append(sec)
def score_to_grade(grd):
  if 85<grd:
     return("A")
  elif 85>grd>=80:
     return("A-")
  elif 80>grd>=75 :
     return("B+")
  elif 75>grd>=68 :
     return("B")
  elif 68>grd>=65 :
     return("B-")
  elif 65>grd>=60:
     return("C+")
  elif 60>grd>=50:
     return("C")
  elif 50>grd>=45:
     return("C-")
  elif 45>grd>=40:
      return("D")
  elif grd<40:
     return("F")

STG=score_to_grade(grd)
  Scores.append(STG)
while True:
   
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
   
