#This will be the main code/ an initiator for the code we will write
import turtle # Importing a Library
graphie=turtle.Turtle() #Naming our Turtle
names = {} #this is the list all the data gets stored in
name = {} 
Section = {}
SAS  = {}
Scores = {}
count = -1
a = ''
b = ''
#THIS IS THE GRADE LOGIC
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

  
while True: #THis is the While loop for the inputs
    count += 1
    n = str(input("Please enter a student's name: ")) #Input code for name
    sec = str(input("Please the student's section: ")) #Input code for section
    s= int(input("Enter student's score: ") )#Input code For score
    STG =  score_to_grade(s)#Calling and storing the score to grade converting function from above
    names[count] = {
      "Name":n,
      "Score":s,
      "Section":sec,
      "Grade":STG
    }
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


#Comparing two Sections
def compare_sections(names, section1, section2):
    scores1 = [s["Score"] for s in names.values() if s["Section"] == section1]#Fetches the Score Data From The List for one section
    scores2 = [s["Score"] for s in names.values() if s["Section"] == section2]#Fetches the Score Data From The List for the other

    if not scores1 or not scores2:  #Error handling 
        print("One or both sections have no data.")
        return None, None
 # Calculates average for A SECTION
    avg1 = sum(scores1) / len(scores1) # Calculates average for A SECTION
    avg2 = sum(scores2) / len(scores2)
    print(f" Section {section1} - Average Score: {avg1:.2f}")
    print(f"Section {section2} - Average Score: {avg2:.2f}")
#Compares the Averages for the sections,Basic Arithmetic Logic new
    if avg1 > avg2:
        print(f" Section {section1} performed better.")
    elif avg2 > avg1:
        print(f"Section {section2} performed better.")
    else:
        print("Both sections performed equally.")

    return avg1, avg2
cs = input("Please input the section's you want to compare.(Eg:- 2,3): ")
a, b = cs.split(',')
compare_sections(names,a.strip(),b.strip())
#NOW ONTO PRESENTATIONNNN
#draft
turtle.bgcolor("black")
graphie=turtle.Turtle()
#The basis of the graph
graphie.hideturtle()
graphie.speed(0)
graphie.color("green")
#Graph dimensions
x=-300
y=100
barwidth=80
gap=100
scale=100
#Title 
graphie.penup()
graphie.goto(x+barwidth/2,y+200)
graphie.write("Section Comparision Graph",align="center",font=("Verdana",14,"bold"))
#grade Gridlines(yaxis)
graphie.penup()
graphie.goto(-250,80)
graphie.pendown()
graphie.right(90)
graphie.forward(300)
graphie.left(90)
graphie.forward(300)
graphie.penup()
graphie.goto((-250+100),(80-300))
graphie.pendown()
graphie.fillcolor("green")
graphie.begin_fill()
graphie.left(90)
graphie.forward(250)
graphie.right(90)
graphie.forward(45)
graphie.right(90)
graphie.forward(250)
graphie.end_fill()
turtle.done()

