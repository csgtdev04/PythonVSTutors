userGrade = int(input("What did you get on your test: "))

if userGrade >= 95:
    print("You are very smart")
elif userGrade > 90 and userGrade < 95:
    print("You are smart")
elif userGrade >= 80 and userGrade < 90:
    print("You are decent")
elif userGrade < 80 and userGrade >= 70:
    print("Almost failing")
else:
    print("You have to study a LOT! FAILED!!!")

