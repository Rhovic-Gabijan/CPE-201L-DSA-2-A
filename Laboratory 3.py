x = int(input("Enter No. of Test: "))
scores = []
even = 0
p = 0
for a in range(x):
    p +=1
    test = int(input(f"{p}. Enter Test Scores: "))
    scores.append(test)
    
    
for i in scores:
    if i % 2 == 0:
        even += i

print("\nSum of Even test score:", even)
print("-"*20)