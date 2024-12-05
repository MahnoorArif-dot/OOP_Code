file1 = open("grades.txt", "r")
file2 = open("errors.txt", "w")

file1.readline()
file1.readline()
x = file1.readlines()
i = 3
count = 0
error_list = []

for line in x:
    a = line[0:4]
    b = line[43:49].strip()
    c = line[49:52].strip()
    d = line[52:55].strip()
    e = line[55:58].strip()

    if a != "BSEF" and a != "BITF":
        if i not in error_list:
            file2.write(str(i) + "\n")
            file2.write(line + "\n")
            error_list.append(i)
            count += 1
    elif b == "" or c == "" or c == "AB" or d == "" or d == "AB" or e == "" or e == "AB":
        if i not in error_list:
            file2.write(str(i) + "\n")
            file2.write(line + "\n")
            error_list.append(i)
            count += 1

    i += 1

file1.close()
file2.close()
print(f'Count of errors is {count}')

