# check the age for voting

age = int(input("Enter your age:"))

# positive conditioning
if (age >= 18):
    print("You are elegible to vote")
else:
    print("You are not elegible to vote")


# negative conditioning
if (age < 18):
    print("You are not elegible to vote")
else:
    print("You are elegible to vote")


# short hand for if else

print("You are elegible to vote") if age>=18 else print("You are not elegible to vote")

vote = True if age>=18 else False

if vote:
    print("vote")
else: 
    print("no vote")

# logical operator
con = age>=18 and "vote" or "no vote"

print(con)