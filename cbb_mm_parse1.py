import csv

'''
Calculates the average total points scored in a tourney game
for each season since 1985, then puts the values into a csv
'''

#dictionary to store total points scored in each years tourney
years = {}

#opens csv with all tourney game results
with open('NCAA_MM_Results.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)

	header = reader.next()

	#parses each row in the csv and adds total points scored to respective year's total
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

#list to store average total points per tourney game in a given season
avgs = []

#calculates average total points scored, creates tuple with value
for year in years.keys():
	totalYearScore = years[year]
	avgYearScore = totalYearScore / 63.0
	yearTup = (year, avgYearScore)
	avgs.append(yearTup)

avgs.sort()

#writes values to csv
with open('ncaa_tourney_avgs.csv', 'wb') as csvwrite:
	writer = csv.writer(csvwrite)
	header = ["Year", "Average Total Score"]
	writer.writerow(header)
	for year in avgs:
		writer.writerow(year)

#prints values to cli
print avgs
