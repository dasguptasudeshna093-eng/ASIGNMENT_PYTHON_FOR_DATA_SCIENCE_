students = [{"name": "Amina", "major": "AMDS"},
{"name": "Maya", "major": "Economics"},
{"name": "Disha", "major": "AMDS"},
{"name": "Nora", "major": "Public Health"},
{"name": "Lina", "major": "Economics"}]
x={}
y={}
for i in students:
  major=i["major"]
  name=i["name"]
  if major not in x:
    x[major]=[]
  x[major].append(name)
print("Groups: ",x)

for i in x:
  y[major]= len(x[major])
print(y)