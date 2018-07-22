import csv

'''
Calculates the number of upsets and the total size of upsets 
in each season's tourney since 1985
'''


#dictionaries to store number of upsets and size of upsets
upsetCounts = {}
upsetSizes = {}

#parses csv of tourney results and updates dictionaries when an upset is detected
with open('NCAA_MM_Results.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)

	header = reader.next()

	for row in reader:
		year = row[0][-2:]
		if int(year) < 85:
			year = "20" + year
		else:
			year = "19" + year
		game = row[1]
		winner = int(row[3])
		loser = int(row[6])
		if winner > loser:
			#print year, game, winner, loser
			try:
				upsetCounts[year] += 1
				upsetSizes[year] += winner - loser
			except:
				upsetCounts[year] = 1
				upsetSizes[year] = winner - loser

	#writes a csv with upset counts/size for each season
	def createExcelFile(upsetTups):
		with open('cbb_upsets.csv', "wb") as csvfile2:
			writer = csv.writer(csvfile2, delimiter=',')
			writer.writerow(["Year", "Upset Count", "Upset Size Sum"])
			for tup in upsetTups:
				writer.writerow(tup)



	ret = []
	totalCountSinceNewEra = 0
	totalSizeSinceNewEra = 0
	upsetDict = {}

	#calculates average number of upsets per year and average total size of upsets per year
	for year in upsetCounts.keys():
		tup = (year, upsetCounts[year], upsetSizes[year])
		upsetDict[year] = (upsetCounts[year], upsetSizes[year])
		totalCountSinceNewEra += upsetCounts[year]
		totalSizeSinceNewEra += upsetSizes[year]
		ret.append(tup)
	ret.sort()

	#initiates create csv and prints averages to cli
	for tup in ret:
		print tup
	print "Upsets per year: " , totalCountSinceNewEra / (2016-1985.0)
	print "Upset sizes per year:", totalSizeSinceNewEra / (2016-1985.0)
	createExcelFile(ret)

	#print 81.2258/18.16129





