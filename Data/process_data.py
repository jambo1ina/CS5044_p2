import csv
import os

#get mappings
def load_mappings(input_dir, delimiter=","):
    if input_dir[-1] != "/":
        input_dir += "/"

    mappings = dict()

    for dirName, _, fileList in os.walk(input_dir):
        round = dirName[dirName.rfind("/") + 1:]
        if len(round) == 0:
            continue
        
        mappings[round] = dict()

        for file in fileList:
            variableName = file[:file.rfind(".csv")]
            mappings[round][variableName] = dict()

            with open(dirName + "/" + file, "r") as f:
                reader = csv.reader(f, delimiter=delimiter)
                for i, line in enumerate(reader):
                    if i == 0:
                        mappings[round][variableName]["description"] = line[0]
                    else:
                        mappings[round][variableName][line[0]] = line[1]
    return mappings

#process data
def processData(input_csv, output_csv, variablesNames, mappings, delimiter=","):
    expandedVariableNames = []
    expansionMap = dict()

    with open(output_csv, "w") as out:
        with open(input_csv, "r") as f:
            reader = csv.reader(f, delimiter=delimiter)
            for i, line in enumerate(reader):
                if i == 0:
                    expandedVariableNames = line

                    #generate expansion map
                    for expanded in expandedVariableNames:
                        if expanded in variablesNames:
                            continue
                        else:
                            for var in variablesNames:
                                if "*" in var:
                                    prefix = var[:var.find("*")]
                                    if expanded.startswith(prefix):
                                        expansionMap[expanded] = var

                    for heading in variablesNames:
                        if heading == "":
                            continue

                        description = heading

                        if "*" in heading:
                            for expanded in expansionMap.keys():
                                original = expansionMap[expanded]
                                if original == heading:
                                    heading = expanded
                                    break

                        for round in mappings.keys():
                            if heading in mappings[round]:
                                description = mappings[round][heading]["description"].replace(" ", "_").replace("'", "")
                                break

                        out.write(description + ",")
                    out.write("\n")
                else:
                    round = str(line[0])
                    expanded = []

                    for j,item in enumerate(line):
                        if item == "":
                            continue

                        if expandedVariableNames[j] in expansionMap:
                            expanding = expansionMap[expandedVariableNames[j]]

                            if expanding in expanded:
                                continue
                            
                            elif item == "-" or item == "0":
                                if (expandedVariableNames[j+1] in expansionMap and expansionMap[expandedVariableNames[j+1]] == expanding):
                                    continue
                                else:
                                    out.write(item + ",")
                                    
                            else:
                                if expandedVariableNames[j] in mappings[round] and item in mappings[round][expandedVariableNames[j]]:
                                    out.write(mappings[round][expandedVariableNames[j]][item] + ",")
                                else:
                                    out.write(item + ",") 

                                expanded.append(expanding)
                        else:
                            if expandedVariableNames[j] in mappings[round] and item in mappings[round][expandedVariableNames[j]]:
                                out.write(mappings[round][expandedVariableNames[j]][item] + ",")
                            else:
                                out.write(item + ",")

                    out.write("\n")