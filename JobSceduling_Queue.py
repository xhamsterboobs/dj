from collections import deque
class JobSceduling_Queue:

    def __init__(self):
        self.job_Queue=deque()
    
    def addJob(self,jobName):
        self.job_Queue.append(jobName)
        print(f"Job {jobName} is Added ...")

    def DeleteJob(self):
        if not self.job_Queue:
            print("No Job's Are Availabele In  Job Queue... ")
        else:
            job=self.job_Queue.popleft()
            print(f"Job {job} is Deleted / Proced...")
    
    def viewJob(self):
        if not self.job_Queue:
            print("No Job's Are available...")

        else:
            print("All Jobs In The Job Queue")
            for i in range(len(self.job_Queue)):
                print(f"Job {i+1} :{self.job_Queue[i]}")

j=JobSceduling_Queue()
flg=True
while flg:
    print("\t\tWelcome")
   
    print("1--> Add Job")
    print("2--> Delete/Process Job")
    print("3--> View Jobs")
    print("4--> Exit")

    ch=input("Enter The Choice :")
    if ch=='1':
        name=input("Enter Job :")
        j.addJob(name)
    elif ch== '2':
        j.DeleteJob()
    elif ch=='3':
        j.viewJob()
    elif ch=='4':
        flg=False
        print("Exit...")
    else:
        print("Invalid Input...")