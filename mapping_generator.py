import xml.etree.ElementTree as ET

INPUT_XMLS = ["ess-documentation/round1.xml", "ess-documentation/round2.xml", "ess-documentation/round3.xml", "ess-documentation/round4.xml", "ess-documentation/round5.xml", "ess-documentation/round6.xml", "ess-documentation/round7.xml", "ess-documentation/round8.xml", "ess-documentation/round9.xml"]
OUT_DIR = "mappings/"

VARIABLES =  ['essround', 'inwyys', 'inwyr', 'cntry', 'polintr', 'trstprl', 'vote', 'prtvtat', 'prtvtbe', 'prtvtch', 'prtvtcz', 'prtvde1', 'prtvde2', 'prtvtdk', 'prtvtes', 'prtvtfi', 'prtvtfr', 'prtvtgb', 'prtvtgr', 'prtvthu', 'prtvtie', 'prtvtil', 'prtvtit', 'prtvtlu', 'prtvtnl', 'prtvtno', 'prtvtpl', 'prtvtpt', 'prtvtse', 'prtvtsi', 'prtvtat', 'prtvtabe', 'prtvtch', 'prtvtcz', 'prtvade1', 'prtvade2', 'prtvtdk', 'prtvtee', 'prtvtaes', 'prtvtfi', 'prtvtfr', 'prtvtgb', 'prtvtagr', 'prtvthu', 'prtvtie', 'prtvtis', 'prtvtait', 'prtvtlu', 'prtvtanl', 'prtvtno', 'prtvtpl', 'prtvtpt', 'prtvtse', 'prtvtasi', 'prtvtsk', 'prtvttr', 'prtvtua', 'prtvtaat', 'prtvtabe', 'prtvtbg', 'prtvtach', 'prtvtcy', 'prtvbde1', 'prtvbde2', 'prtvtadk', 'prtvtaee', 'prtvtaes', 'prtvtfi', 'prtvtafr', 'prtvtagb', 'prtvtahu', 'prtvtie', 'prtvtlv', 'prtvtbnl', 'prtvtno', 'prtvtapl', 'prtvtapt', 'prtvtro', 'prtvtru', 'prtvtse', 'prtvtbsi', 'prtvtask', 'prtvtaua', 'prtvtaat', 'prtvtbbe', 'prtvtabg', 'prtvtbch', 'prtvtcy', 'prtvtacz', 'prtvbde1', 'prtvbde2', 'prtvtbdk', 'prtvtbee', 'prtvtbes', 'prtvtafi', 'prtvtbfr', 'prtvtgb', 'prtvtbgr', 'prtvthr', 'prtvtbhu', 'prtvtie', 'prtvtail', 'prtvlt1', 'prtvlt2', 'prtvlt3', 'prtvtlv', 'prtvtcnl', 'prtvtno', 'prtvtbpl', 'prtvtapt', 'prtvtaro', 'prtvtaru', 'prtvtse', 'prtvtcsi', 'prtvtask', 'prtvtatr', 'prtvtbua', 'prtvtcbe', 'prtvtbbg', 'prtvtcch', 'prtvthr', 'prtvtcy', 'prtvtbcz', 'prtvcde1', 'prtvcde2', 'prtvtbdk', 'prtvtcee', 'prtvtbes', 'prtvtbfi', 'prtvtbfr', 'prtvtgb', 'prtvtcgr', 'prtvtchu', 'prtvtaie', 'prtvtbil', 'prtvlt1', 'prtvlt2', 'prtvlt3', 'prtvtdnl', 'prtvtano', 'prtvtbpl', 'prtvtbpt', 'prtvtbru', 'prtvtase', 'prtvtcsi', 'prtvtbsk', 'prtvtbua', 'prtvtal', 'prtvtcbe', 'prtvtcbg', 'prtvtdch', 'prtvtacy', 'prtvtccz', 'prtvdde1', 'prtvdde2', 'prtvtcdk', 'prtvtdee', 'prtvtces', 'prtvtcfi', 'prtvtcfr', 'prtvtgb', 'prtvtdhu', 'prtvtaie', 'prtvtbil', 'prtvtais', 'prtvtbit', 'prtvalt1', 'prtvalt2', 'prtvalt3', 'prtvtenl', 'prtvtano', 'prtvtcpl', 'prtvtbpt', 'prtvtcru', 'prtvtbse', 'prtvtdsi', 'prtvtcsk', 'prtvtcua', 'prtvtxk', 'prtvtbat', 'prtvtcbe', 'prtvtech', 'prtvtdcz', 'prtvede1', 'prtvede2', 'prtvtcdk', 'prtvteee', 'prtvtces', 'prtvtcfi', 'prtvtcfr', 'prtvtbgb', 'prtvtehu', 'prtvtaie', 'prtvtcil', 'prtvalt1', 'prtvalt2', 'prtvalt3', 'prtvtfnl', 'prtvtbno', 'prtvtcpl', 'prtvtbpt', 'prtvtbse', 'prtvtesi', 'prtvtbat', 'prtvtcbe', 'prtvtfch', 'prtvtdcz', 'prtvede1', 'prtvede2', 'prtvtfee', 'prtvtdes', 'prtvtdfi', 'prtvtcfr', 'prtvtbgb', 'prtvtehu', 'prtvtbie', 'prtvtcil', 'prtvtbis', 'prtvtbit', 'prtvblt1', 'prtvblt2', 'prtvblt3', 'prtvtfnl', 'prtvtbno', 'prtvtdpl', 'prtvtcpt', 'prtvtdru', 'prtvtbse', 'prtvtesi', 'prtvtcat', 'prtvtdbe', 'prtvtdbg', 'prtvtgch', 'prtvtbcy', 'prtvtecz', 'prtvede1', 'prtvede2', 'prtvtddk', 'prtvtgee', 'prtvtees', 'prtvtdfi', 'prtvtdfr', 'prtvtcgb', 'prtvtahr', 'prtvtfhu', 'prtvtcie', 'prtvtcis', 'prtvtcit', 'prtvblt1', 'prtvblt2', 'prtvblt3', 'prtvtalv', 'prtvtme', 'prtvtgnl', 'prtvtbno', 'prtvtdpl', 'prtvtcpt', 'prtvtrs', 'prtvtcse', 'prtvtfsi', 'prtvtdsk', 'lrscale', 'imwbcnt', 'edulvlb', 'emplrel', 'gndr', 'pdjobyr', 'hincfel', 'uemp12m', 'chldhhe']

for input in INPUT_XMLS:
    round = input[input.rfind("/round") + 6:input.rfind(".xml")]

    tree = ET.parse(input)
    root = tree.getroot()

    for var in root[3]:
        try:
            name = var.attrib["name"]
            if name in VARIABLES:

                description = ""
                mapping = dict()

                for item in var:
                    if item.tag == "{http://www.icpsr.umich.edu/DDI}labl":
                        description = item.text.replace("\n", "")

                    if item.tag == "{http://www.icpsr.umich.edu/DDI}catgry":
                        for child in item:
                            mapping[item[0].text.replace("\n", "")] = item[1].text.replace("\n", "")

                with open(OUT_DIR + round + "/" + name + ".csv", 'w') as out:
                    out.write(description + "\n")

                    for key in mapping.keys():
                        out.write(key + "," + mapping[key] + "\n")
        except:
            continue