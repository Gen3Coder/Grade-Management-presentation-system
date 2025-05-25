
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
