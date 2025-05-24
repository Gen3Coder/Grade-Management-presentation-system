#This will be the main code/ an initiator for the code we will write
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
    s= int(input("Enter a student's grade: ") )
    STG =  score_to_grade(s)
    Scores += STG
    choice = input('Would you like to sumbit another grade?(Y/N) ')
    if choice.lower() == 'y':
       break
    elif choice.lower() == 'n':
       pass
    else:
       break    
  
