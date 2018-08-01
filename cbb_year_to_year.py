import csv

#weight of a win in specific round
pointsPerRound = {}
pointsPerRound["Opening Round"] = 0
pointsPerRound["Round of 64"] = 2
pointsPerRound["Round of 32"] = 4
pointsPerRound["Sweet Sixteen"] = 8
pointsPerRound["Elite Eight"] = 16
pointsPerRound["National Semifinals"] = 32
pointsPerRound["National Championship"] = 65

teamWinScores = {}

teamScoreDiff = {}


with open('NCAA_MM_Results.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	header = reader.next()

	for line in reader:
		date = line[0]
		year = date[-2:]
		if int(year) >= 85:
			year = int("19" + year)
		else:
			year = int("20" + year)
		rd = line[1]
		winner = line[4]
		loser = line[7]
		scoreDiff = int(line[5]) - int(line[8])
		#update team scores and differentials
		if (winner,year) in teamWinScores.keys():
			teamWinScores[(winner,year)] += pointsPerRound[rd]
			teamScoreDiff[(winner,year)] += scoreDiff
		else:
			teamWinScores[(winner,year)] = pointsPerRound[rd]
			teamScoreDiff[(winner,year)] = scoreDiff
		if (loser,year) in teamWinScores.keys():
			teamWinScores[(loser,year)] += 1
			teamScoreDiff[(loser,year)] -= scoreDiff
		else:
			teamWinScores[(loser,year)] = 1
			teamScoreDiff[(loser,year)] = scoreDiff * -1

yearToYear = {}
yearToYearDiff = {}

for team in teamWinScores.keys():
	school = team[0]
	year = team[1]
	prevYear = year-1
	try:
		yearToYear[team] = (teamWinScores[(school,prevYear)],teamWinScores[team])
		yearToYearDiff[team] = (teamScoreDiff[(school,prevYear)],teamScoreDiff[team])
	except:
		pass



with open('cbb_year_to_year.csv', 'wb') as csvwrite:
	writer = csv.writer(csvwrite)
	writer.writerow(["school", "season", "prev winScore", "winScore", "prev scoreDiff", "scoreDiff"])
	for team in yearToYear.keys():
		school = team[0]
		year = team[1]
		prevWinScore = yearToYear[team][0]
		winScore = yearToYear[team][1]
		prevScoreDiff = yearToYearDiff[team][0]
		scoreDiff = yearToYearDiff[team][1]
		writer.writerow([school, year, prevWinScore, winScore, prevScoreDiff, scoreDiff])

