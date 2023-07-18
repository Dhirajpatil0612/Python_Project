import random
num=random.randint(0,100)
attempt=1
check=0
for i in range(0,5):
    guess=int(input("Guess the number between 1 to 100: "))
    if guess>num:
        print("Lower number please!")
        check=1
    elif guess<num:
        print("Higher number please!")
        check=1
    else:
        print(f"Congratulation!You have Guess The Number in {attempt} attempt")
        check=0
        break
    attempt+=1
print()
print()
print()
if check==1:
    print("You failed in Guessing The Number!")
