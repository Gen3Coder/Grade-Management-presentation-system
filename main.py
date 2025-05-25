#This will be the main code/ an initiator for the code we will write
names = {}
name = {}
Section = {}
SAS  = {}
Scores = {}
count = -1
a = ''
b = ''
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

  
while True:
    count += 1
    n = str(input("Please enter a student's name: "))
    sec = str(input("Please the student's section: "))
    s= int(input("Enter a student's grade: ") )
    STG =  score_to_grade(s)
    names[count] = [n ,s, sec]
    if count not in name:
       name[count] = []
    name[count].append(names[count])
    choice = input('Would you like to sumbit the grade of another student?(Y/N) ')
    if choice.lower() == 'y':
       pass
    elif choice.lower() == 'n':
       break
    else:
       break    

print(name)
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
#Comparing two Sections
def compare_sections(students, section1, section2):
    scores1 = [s["Score"] for s in students.values() if s["Section"] == section1]
    scores2 = [s["Score"] for s in students.values() if s["Section"] == section2]

    if not scores1 or not scores2:
        print("One or both sections have no data.")
        return None, None

    avg1 = sum(scores1) / len(scores1)
    avg2 = sum(scores2) / len(scores2)
    print(f" Section {section1} - Average Score: {avg1:.2f}")
    print(f"Section {section2} - Average Score: {avg2:.2f}")

    if avg1 > avg2:
        print(f" Section {section1} performed better.")
    elif avg2 > avg1:
        print(f"Section {section2} performed better.")
    else:
        print("Both sections performed equally.")

    return avg1, avg2

   
