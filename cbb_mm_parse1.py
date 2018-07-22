import csv

years = {}

with open('NCAA_MM_Results.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)

	header = reader.next()

	for row in reader:
		year = row[0][-2:]
		if int(year) < 85:
			year = "20" + year
		else:
			year = "19" + year
		winScore = int(row[5])
		loseScore = int(row[8])
		if year in years.keys():
			years[year] += winScore + loseScore
		else:
			years[year] = winScore + loseScore

avgs = []

for year in years.keys():
	totalYearScore = years[year]
	avgYearScore = totalYearScore / 63.0
	yearTup = (year, avgYearScore)
	avgs.append(yearTup)

avgs.sort()

with open('ncaa_tourney_avgs.csv', 'wb') as csvwrite:
	writer = csv.writer(csvwrite)
	header = ["Year", "Average Total Score"]
	writer.writerow(header)
	for year in avgs:
		writer.writerow(year)

print avgs
