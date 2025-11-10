import array
def selection_sort(students):
    for i in range(len(students)):
        small=i
        for j in range(i+1,len(students)):
            if students[j]<students[small]:
                small=j
        students[i],students[small]=students[small],students[i]

print("\t\t----Welcome----")
total_student=int(input("Enter the total Number of student :"))

students=array.array('i',[])
print("Enter the percent of student's :")
for i in range(total_student):
    roll=int(input(f"Student {i+1} :"))
    students.append(roll)
print(f"Persent list before sorting :{students}")
selection_sort(students)
print(f"Persent list after sorting :{students}")