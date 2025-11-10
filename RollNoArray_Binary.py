import array
found=False
def binary_search(students,target_roll):
    low=0
    high=len(students)-1
    while low<=high:
        mid=(low+high)//2
        if students[mid]==target_roll:
            found=True
            return mid
        if students[mid]<target_roll:
            low=mid+1
        else:
            high=mid-1

students=array.array('i',[])
total=int(input("Enter the total no. of students :"))
print("Enter their roll numbers :")
for i in range(total):
    ch=int(input(f"Student {i+1}:"))
    students.append(ch)
target_roll=int(input("Enter the roll number to search :"))
if not found:
    print(f"Student present at position :{binary_search(students,target_roll)+1}")
else:
    print(f"Student not Present : NOT FOUND")