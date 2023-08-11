from pathlib import Path

# universal path
ROOT_DIR = Path(__file__).absolute().parent.parent

# variables
result = []
count_users = 0
count_result = 0

# open file and check
try:
    file = open(ROOT_DIR / "rockyou.txt")
except Exception:
    exit("File not open")

# if check == 'yes' append data from sile in result
check = input(str("Do u want to add data from file in result list(yes, not)?\n"))


# moving through the file 'rockyou.txt'
while True:
    try:
        word = file.readline()

        if check == "yes":
            result.append(word)
            count_result += 1

        # check 'user' word in lines
        if word == "user\n":
            count_users += 1

    except Exception:
        break


# output answers
print("Count lines in result[] = " + str(count_result))
print("Count user = " + str(count_users))

# close file
file.close()
