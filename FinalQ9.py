import pandas as pd
data = {"Name": ["Amina", "Maya", "Lina", "Nora", "Sara"], "Quiz": [18, 12, 16, 9, 15], "Midterm": [25, 19, 28, 15, 22],
    "Final": [45, 31, 40, 25, 38]}

df = pd.DataFrame(data)
print(df)
df["Total"] = df["Quiz"] + df["Midterm"] + df["Final"]

df["Average"] = df["Total"] / 3

df["Status"] = df["Total"].apply(
    lambda x: "Pass" if x >= 50 else "Fail")

print("\nPassed Students:")
print(df[df["Status"] == "Pass"])

df = df.sort_values(by="Total", ascending=False)

print("\nSorted DataFrame:")
print(df)
df.to_excel("student_results.xlsx", index=False)

