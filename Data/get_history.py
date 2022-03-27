import wikipediaapi

TITLE = "Timeline of the 21st century"
START_YEAR = 2003
END_YEAR = 2019
OUTPUT_CSV = "../history.csv"

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

page = wiki.page(TITLE)
lines = page.text.splitlines()

newYear = True
year = "2001"

with open(OUTPUT_CSV, "w") as out:
    out.write("year, date, event\n")

    for line in lines[3:]:
        
        if line == "":
            newYear = True
            continue 
        elif line.startswith("2010s"):
            continue
        elif line.startswith("2020s"):
            break
        elif newYear and line.startswith("20"):
            year = line
            newYear = False
            continue
        
        if int(year) < START_YEAR:
            continue
        elif int(year) > END_YEAR:
            break

        date = ""
        event = ""

        if line.startswith(MONTHS):
            elements = line.split(":", 1)
            date = elements[0]
            event = elements[1]
        else:
            event = line

        out.write(year + "," + date + "," + event + "\n")

