print("\t\t ...Wellcomt to my company...")

def selectionSort(salaries):
    for i in range(len(salaries)):
        small=i
        for j in range(i+1,len(salaries)):
            if salaries[j]<salaries[small]:
               small=j
        salaries[i],salaries[small]=salaries[small],salaries[i]

total_employee=int(input("Enter the total number of employee :"))
print("Enter the salaries of the Employee :")
salaries=[]
for i in range(total_employee):
    sl=float(input(f"Enter salary of Employee {i+1} : "))
    salaries.append(sl)

print(f"Salaries of the Employee before Sorting :{salaries}")
selectionSort(salaries)
print(f"Salaries after the selection Sort (Acssending) :{salaries}")
print("\n\t-----Thank you ------")