import csv

def get_variables_names(variables_csv, delimiter=",", name_index=0):
    variableNames = []
    with open(variables_csv, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)
        for i, line in enumerate(reader):
            if i == 0:
                continue
            else:
                variableNames.append(line[name_index])
    return variableNames

#expand all wildcard variable names
def expand_variable_names(input_csvs, variableNames, delimiter=","):
    expandedVariablesNames = []
    for variable in variableNames:
        if "*" in variable:
            prefix = variable[:variable.find("*")]
            
            for input in input_csvs:
                with open(input, "r") as f:
                    reader = csv.reader(f, delimiter=delimiter)
                    for i, line in enumerate(reader):
                            if i != 0:
                                break
                            else:
                                for heading in line:
                                    if heading.startswith(prefix) and heading not in expandedVariablesNames:
                                        expandedVariablesNames.append(heading)

        else:
            expandedVariablesNames.append(variable)
    return expandedVariablesNames

#genereate output CSV
def extract_data(input_csvs, output_csv, expandedVariablesNames, delimiter=",", missing_data="-"):
    with open(output_csv, 'w') as out:
        for heading in expandedVariablesNames:
            out.write(heading)
            out.write(",")

        out.write("\n")

        for file in input_csvs:
            with open(file, "r") as f:
                reader = csv.reader(f, delimiter=delimiter)
                indexes = dict()

                for i, line in enumerate(reader):
                    if i == 0:
                        for var in expandedVariablesNames:
                            for j,heading in enumerate(line):
                                if heading in expandedVariablesNames:
                                    indexes[heading] = j

                            for heading in expandedVariablesNames:
                                if heading not in indexes.keys():
                                    indexes[heading] = -1
                    else:
                        values = dict()
                        for heading in indexes.keys():
                            index = indexes[heading]
                            if index == -1:
                                values[heading] = missing_data
                            else:
                                values[heading] = line[index]
                        
                        for heading in expandedVariablesNames:
                            out.write(values[heading])
                            out.write(",")

                        out.write("\n")
