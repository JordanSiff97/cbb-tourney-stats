import csv

upsetCounts = {}
upsetSizes = {}

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


	def createExcelFile(upsetTups):
		with open('cbb_upsets.csv', "wb") as csvfile2:
			writer = csv.writer(csvfile2, delimiter=',')
			writer.writerow(["Year", "Upset Count", "Upset Size Sum"])
			for tup in upsetTups:
				writer.writerow(tup)



	ret = []
	totalSinceNewEra = 0
	total = 0
	upsetDict = {}
	for year in upsetCounts.keys():
		tup = (year, upsetCounts[year], upsetSizes[year])
		upsetDict[year] = (upsetCounts[year], upsetSizes[year])
		totalSinceNewEra += upsetCounts[year]
		total += upsetSizes[year]
		ret.append(tup)
	ret.sort()
	for tup in ret:
		print tup
	print "Upsets per year: " , totalSinceNewEra / (2016-1985.0)
	print "Upset sizes per year:", total / (2016-1985.0)
	createExcelFile(ret)

	print 81.2258/18.16129





