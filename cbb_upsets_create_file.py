import cbb_mm_parse_upsets
import cbb_srs_std_dev
import csv

'''
Creates csv with multiple stats
'''

parity_scores = cbb_srs_std_dev.parity_scores
upsetDict = cbb_mm_parse_upsets.upsetDict


with open("cbb_upsets.csv", 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Year", "Upset Count", "Upset Size Sum", "Parity Score"])
	for year in range(32):
		season = 1985 + year
		writer.writerow([season, upsetDict[str(season)][0], upsetDict[str(season)][1], parity_scores[int(season)]])

print "DONE"






















