import array
def bubble_sort(students):
    for i in range(len(students)):
        for j in range(len(students)-1):
            if students[j]>students[j+1]:
                students[j],students[j+1]=students[j+1],students[j]

print("\t\t----Welcome----")
total_student=int(input("Enter the total Number of student :"))

students=array.array('i',[])
print("Enter the Percents of student :")
for i in range(total_student):
    roll=int(input(f"Student {i+1} :"))
    students.append(roll)
print(f"persent list before sorting :{students}")
bubble_sort(students)
print(f"Persent list after sorting :{students}")