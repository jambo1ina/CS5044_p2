import csv

INPUT_CSV = ["ess/round1.csv", "ess/round2.csv", "ess/round3.csv", "ess/round4.csv", "ess/round5.csv", "ess/round6.csv", "ess/round7.csv", "ess/round8.csv", "ess/round9.csv"]
OUTPUT_CSV = "data.csv"
DELIMITER = ","
VARIABLES_CSV = "variables.csv"
VARIABLE_NAME_INDEX = 0
MISSING_DATA = "-"

variableNames = []
with open(VARIABLES_CSV, "r") as f:
    reader = csv.reader(f, delimiter=DELIMITER)
    for i, line in enumerate(reader):
        if i == 0:
            continue
        else:
            variableNames.append(line[VARIABLE_NAME_INDEX])

print("extracting: ", variableNames)
print("to file: ", OUTPUT_CSV)

with open(OUTPUT_CSV, 'w') as out:
    for heading in variableNames:
        out.write(heading)
        out.write(",")

    out.write("\n")

    for file in INPUT_CSV:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=DELIMITER)
            indexes = dict()
            for i, line in enumerate(reader):
                if i == 0:
                    for j,heading in enumerate(line):
                        if heading in variableNames:
                            indexes[heading] = j

                    for heading in variableNames:
                        if heading not in indexes.keys():
                            indexes[heading] = -1
                else:
                    values = dict()
                    for heading in indexes.keys():
                        index = indexes[heading]
                        if index == -1:
                            values[heading] = MISSING_DATA
                        else:
                            values[heading] = line[index]
                    
                    for heading in variableNames:
                        out.write(values[heading])
                        out.write(",")

                    out.write("\n")
