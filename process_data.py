import csv
import os

from numpy import var

INPUT_CSV = "ess.csv"
INPUT_DIR = "mappings/"
OUTPUT_CSV = "processed_data.csv"
DELIMITER = ","
MISSING_DATA = "-"

VARIABLE_NAMES = ['essround', 'inwyys', 'inwyr', 'cntry', 'polintr', 'trstprl', 'vote', 'prtv*', 'lrscale', 'imwbcnt', 'edulvlb', 'emplrel', 'gndr', 'pdjobyr', 'hincfel', 'uemp12m', 'chldhhe']

#get mappings
mappings = dict()

for dirName, subdirList, fileList in os.walk(INPUT_DIR):
    round = dirName[dirName.rfind("/") + 1:]
    if len(round) == 0:
        continue
    
    mappings[round] = dict()

    for file in fileList:
        variableName = file[:file.rfind(".csv")]
        mappings[round][variableName] = dict()

        with open(dirName + "/" + file, "r") as f:
            reader = csv.reader(f, delimiter=DELIMITER)
            for i, line in enumerate(reader):
                if i == 0:
                    mappings[round][variableName]["description"] = line[0]
                else:
                    mappings[round][variableName][line[0]] = line[1]

#process data
expandedVariableNames = []
expansionMap = dict()

with open(OUTPUT_CSV, "w") as out:
    with open(INPUT_CSV, "r") as f:
        reader = csv.reader(f, delimiter=DELIMITER)
        for i, line in enumerate(reader):
            if i == 0:
                expandedVariableNames = line

                #generate expansion map
                for expanded in expandedVariableNames:
                    if expanded in VARIABLE_NAMES:
                        continue
                    else:
                        for var in VARIABLE_NAMES:
                            if "*" in var:
                                prefix = var[:var.find("*")]
                                if expanded.startswith(prefix):
                                    expansionMap[expanded] = var

                out.write(str(VARIABLE_NAMES).replace("[" , "").replace("]", "") + "\n")
            else:
                round = str(line[0])
                for j,item in enumerate(line):
                    if expandedVariableNames[j] in expansionMap:
                        if item == "-" or item == "0":
                            continue
                        else:
                            if expandedVariableNames[j] in mappings[round] and item in mappings[round][expandedVariableNames[j]]:
                                out.write(mappings[round][expandedVariableNames[j]][item] + ",")
                            else:
                                out.write(item + ",") 
                    else:
                        if expandedVariableNames[j] in mappings[round] and item in mappings[round][expandedVariableNames[j]]:
                            out.write(mappings[round][expandedVariableNames[j]][item] + ",")
                        else:
                            out.write(item + ",")

                out.write("\n")