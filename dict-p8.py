scores = {"Amina": {"python": 82, "statistics": 76, "calculus": 88},
"Maya": {"python": 58, "statistics": 64, "calculus": 61}, "Disha":{"python": 91, "statistics": 89, "calculus": 94}, "Nora":{"python": 45, "statistics": 52, "calculus": 56}}
d={ }

for i,j in scores.items():
      total=sum(j.values())
      x=total/3
      if x>60:
        status = "pass"
      else:
        status ="fail"

      d[i]={"average":x,"status":status}

print(d)