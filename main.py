#This will be the main code/ an initiator for the code we will write

names = {} #this is the list all the data gets stored in
name = {} 
Section = {}
SAS  = {}
Scores = {}
count = 0
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
 # Calcutation
    avg1 = sum(scores1) / len(scores1) # Calculates average for A SECTION
    avg2 = sum(scores2) / len(scores2)
    print(f" Section {section1} - Average Score: {avg1:.2f}")
    print(f"Section {section2} - Average Score: {avg2:.2f}")
#comparision
    if avg1 > avg2:
        print(f" Section {section1} performed better.")
    elif avg2 > avg1:
        print(f"Section {section2} performed better.")
    else:
        print("Both sections performed equally.")

    return avg1, avg2
cs = input("Please input the section's you want to compare.(Eg:- 2,3): ")
sec1, sec2 = [s.strip() for s in cs.split(',')]
avg1, avg2 = compare_sections(names, sec1, sec2)
#Data retriving for graphs 2,3 and 4
def get_roll_grade_score(section):
    rolls = []
    grades = []
    scores = []
    for roll, val in names.items():
        if val["Section"] == section:
            rolls.append(roll)
            grades.append(val["Grade"])
            scores.append(val["Score"])

def grade_frequency():
    freq = {"A": 0, "A-": 0, "B+": 0, "B": 0, "B-": 0, "C+": 0, "C": 0, "C-": 0, "D": 0, "F": 0}
    for student in names.values():
        grade = student["Grade"]
        if grade in freq:
            freq[grade] += 1
    return freq

freqdictionary = grade_frequency()
print("\nGrade Frequency:")
for a, b in freqdictionary.items():
    print(f"{a}: {b}")
#Now WE DRAWW!!
import turtle 
graphie=turtle.Turtle() 
turtle.bgcolor("black")
graphie=turtle.Turtle()
graphie.hideturtle()
graphie.speed(0)
graphie.color("green")


def draw_comparison_graph(avg1, avg2, sec1, sec2):
 

 x = -310
 y = 70
 bar_width = 40
 gap2 = 60
 scale = 2

    # Title
 graphie.penup()
 graphie.goto(-300, 300)
 graphie.pendown()
 graphie.write("Section Comparison Graph", font=("Verdana", 16, "bold"))

    # axis
 graphie.penup()
 graphie.goto(-310,270)
 graphie.pendown()
 graphie.right(90)
 graphie.forward(200)
 graphie.left(90)
 graphie.forward(200)
  
  #Score Grid
 for i in range(0, 201, 20):  
        graphie.penup()
        graphie.goto(-340, 70 + i)
        graphie.pendown()
        graphie.write(f"{i/2}", font=("Verdana", 9, "normal"))
        graphie.penup()
 # Graph 1 BAR A
 graphie.penup()
 graphie.goto(x + 50, 70)
 graphie.pendown()
 graphie.fillcolor("green")
 graphie.begin_fill()
 graphie.setheading(90)
 graphie.forward(avg1 * scale)
 graphie.right(90)
 graphie.forward(bar_width)
 graphie.right(90)
 graphie.forward(avg1 * scale)
 graphie.end_fill()
 graphie.penup()
 graphie.goto(x + 50 + bar_width / 2, y - 20)
 graphie.write(f"Sec {sec1}", align="center", font=("Verdana", 12))

#Graph 1 BAR B
 graphie.penup()
 graphie.goto(x + 40 + bar_width + gap2, 70)
 graphie.pendown()
 graphie.fillcolor("green")
 graphie.begin_fill()
 graphie.setheading(90)
 graphie.forward(avg2 * scale)
 graphie.right(90)
 graphie.forward(bar_width)
 graphie.right(90)
 graphie.forward(avg2 * scale)
 graphie.end_fill()
 graphie.penup()
 graphie.goto(x + 50 + bar_width + gap2 + bar_width / 2, y - 20)
 graphie.write(f"Sec {sec2}", align="center", font=("Verdana", 12))


# Graph Drawing Condition :)
if avg1 and avg2:
    draw_comparison_graph(avg1, avg2, sec1, sec2)
#Graph2
def Classscore1(names, section=None):
    width = 15
    spacing = 20
    scale = 2
    x2 = 200
    y2 = 300
  #Score Grid
    for i in range(0,201,20):
        graphie.penup()
        graphie.goto(165,(90+i))
        graphie.pendown()
        graphie.write(f"{i/2}",font=("Verdana",9,"normal"))
        graphie.penup()

    graphie.penup()
    graphie.goto(x2, y2+20 )
    graphie.write(f"Scores of Section {section}", font=("Verdana", 16, "bold"))
    graphie.goto(x2, y2)
    graphie.pendown()
    graphie.forward(200)
    graphie.left(90)
    graphie.forward(200)
    graphie.penup()
    graphie.right(90)

    
    if section:
        students = [(roll, val["Score"]) for roll, val in names.items() if val["Section"] == section]
    else:
        students = [(roll, val["Score"]) for roll, val in names.items()]

    # Draw bars
    for i, (roll, score) in enumerate(students):
        height = score * scale
        x = x2 + i * (width + spacing)
        graphie.penup()
        graphie.goto(x+spacing, y2-200)
        graphie.setheading(90)
        graphie.pendown()
        graphie.begin_fill()
        graphie.forward(height)
        graphie.right(90)
        graphie.forward(width)
        graphie.right(90)
        graphie.forward(height)
        graphie.end_fill()

        graphie.penup()
        graphie.goto(x + width / 2, y2-200 - 20)
        graphie.write(f"R{str(roll)}", align="center", font=("Verdana", 8))

        graphie.goto(x + width, y2-200 + height + 5)
        graphie.write(str(score),align="center",font=("Verdana", 8))
Classscore1(names, section=sec1)


# GRAPH 3
def Classscore2(names, section=None):
    width = 15
    spacing = 10
    scale = 2
    x2 = -300
    y2 = -100
  
  #Score Grid
    for i in range(0,201,20):
        graphie.penup()
        graphie.goto(-335,(-310+i))
        graphie.pendown()
        graphie.write(f"{i/2}",font=("Verdana",9,"normal"))
        graphie.penup()
    
    graphie.penup()
    graphie.goto(x2, y2+20)
    graphie.write(f"Scores of Section {section}", font=("Verdana", 16, "bold"))
    graphie.goto(x2, y2)
    graphie.pendown()
    graphie.forward(200)
    graphie.left(90)
    graphie.forward(200)
    graphie.penup()
    graphie.right(90)

    
    if section:
        students = [(roll, val["Score"]) for roll, val in names.items() if val["Section"] == section]
    else:
        students = [(roll, val["Score"]) for roll, val in names.items()]

    # Draw bars
    for i, (roll, score) in enumerate(students):
        height = score * scale
        x = x2 + i * (width + spacing)
        graphie.penup()
        graphie.goto(x+spacing, y2-200)
        graphie.setheading(90)
        graphie.pendown()
        graphie.begin_fill()
        graphie.forward(height)
        graphie.right(90)
        graphie.forward(width)
        graphie.right(90)
        graphie.forward(height)
        graphie.end_fill()

        graphie.penup()
        graphie.goto(x + width / 2, y2-200 - 20)
        graphie.write(f"R{str(roll)}", align="center", font=("Verdana", 8))

        graphie.goto(x + width , y2-200 + height + 5)
        graphie.write(str(score), align="center", font=("Verdana", 8))
Classscore2(names, section=sec2)
#Graph 4
def draw_grade_frequency(freqdictionary):
    width4 = 20
    spacing = 15
    scale = 10
    x4 = 240
    y4 = -100

    graphie.penup()
    graphie.goto(200, -100)
    graphie.write("General Grade Frequency", font=("Verdana", 16, "bold"))

    graphie.goto(x4, y4)
    graphie.pendown()
    graphie.forward(250)
    graphie.left(90)
    graphie.forward(300)
    graphie.penup()

    for i,(Grade, count) in enumerate(sorted(freqdictionary.items(), reverse=True)):
        height4 = count * scale
        x = x4 + i * (width4 + spacing)
        graphie.penup()
        graphie.goto(x, y4-250)
        graphie.setheading(90)
        graphie.pendown()
        graphie.begin_fill()
        graphie.forward(height4)
        graphie.right(90)
        graphie.forward(width4)
        graphie.right(90)
        graphie.forward(height4)
        graphie.end_fill()

        graphie.penup()
        graphie.goto(x + width4 / 2, y4-250 - 20)
        graphie.write(Grade, align="center", font=("Verdana", 10))
        graphie.goto(x + width4 / 2, y4-250 + height4 + 5)
        graphie.write(str(count), align="center", font=("Verdana", 8))
draw_grade_frequency(freqdictionary)
turtle.done()
