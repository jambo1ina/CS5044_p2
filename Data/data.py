from generate_mapping import *
from extract_data import *
from process_data import *

VARIABLES_CSV = "variables.csv"
INPUT_XMLS = ["ess-documentation/round1.xml", "ess-documentation/round2.xml", "ess-documentation/round3.xml", "ess-documentation/round4.xml", "ess-documentation/round5.xml", "ess-documentation/round6.xml", "ess-documentation/round7.xml", "ess-documentation/round8.xml", "ess-documentation/round9.xml"]
INPUT_CSVS = ["ess-csv/round1.csv", "ess-csv/round2.csv", "ess-csv/round3.csv", "ess-csv/round4.csv", "ess-csv/round5.csv", "ess-csv/round6.csv", "ess-csv/round7.csv", "ess-csv/round8.csv", "ess-csv/round9.csv"]
MAPPING_DIR = "mappings/"
RAW_DATA = "raw.csv"
PROCESSED_DATA = "../data.csv"

print("\nRetreving variable names from:", VARIABLES_CSV)
variableNames = get_variables_names(VARIABLES_CSV)
print("Variables Retreived:", variableNames)

print("\nReading from files:", INPUT_CSVS)

print("Expanding variable names...")
expandedVariablesNames = expand_variable_names(INPUT_CSVS, variableNames)
print("Expanded variable names:", expandedVariablesNames)

print("\nExtracting data....")
extract_data(INPUT_CSVS, RAW_DATA, expandedVariablesNames)
print("written to file: ", RAW_DATA)

print("\nReading file:", INPUT_XMLS)
print("Generating mappings...")
generate_mappings(INPUT_XMLS, MAPPING_DIR, expandedVariablesNames)
print("Writing mappings to:", MAPPING_DIR)

print("\nLoading mappings from:", MAPPING_DIR)
mappings = load_mappings(MAPPING_DIR)

print("\nReading File:", RAW_DATA)
print("Processing data...")
processData(RAW_DATA, PROCESSED_DATA, variableNames, mappings)
print("Writting processed data to:", PROCESSED_DATA)