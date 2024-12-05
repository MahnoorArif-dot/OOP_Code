try:
    with open("errors.txt", "r") as e:
        e.readline()
        e.readline()
        with open("grades.txt", "r+") as g:
            s = e.readline()

            while s != "":
                try:
                    lineno = int(s)
                    s = e.readline()
                    g.seek((lineno - 1) * 59)
                    g.writelines(s)
                    s = e.readline()
                except ValueError:
                    print("Error: Failed to convert line number to an integer.")
                    break

    print("Update done")
except FileNotFoundError:
    print("Error: One or both files not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
