# NTI - Yousef Gomaa

# Task 1
# num = [10,20,30,40]

# avg = 0

# for i in num:
#     avg += i

# avg = avg/len(num)

# print("Average of List \"num\":",str(avg))

# Task 2
n = input("Kindly enter the number of subjects: ")
total = 0

for i in range(int(n)):
    m = input("Kindly put grade for subject"+str(i)+": ")
    if float(m) > 100:
        print("Error")
        continue
    else:
        total += float(m)

if (int(n)>0):
    print("Percentage:",str(total/(int(n))),"%")