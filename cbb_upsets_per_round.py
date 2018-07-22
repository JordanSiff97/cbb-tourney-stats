import csv
import copy

upsetCounts = {}
upsetSizes = {}
upsetArrays = {}
games = {}
gameIdx = {}
gameIdxRev = {}

games["Round of 64"] = 64
games["Round of 32"] = 32
games["Sweet Sixteen"] = 16
games["Elite Eight"] = 8
games["National Semifinals"] = 4
games["National Championship"] = 2
games["Opening Round"] = 68

gameIdx[64] = 0
gameIdx[32] = 1
gameIdx[16] = 2
gameIdx[8] = 3
gameIdx[4] = 4
gameIdx[2] = 5

gameIdxRev[0] = 64
gameIdxRev[1] = 32
gameIdxRev[2] = 16
gameIdxRev[3] = 8
gameIdxRev[4] = 4
gameIdxRev[5] = 2




with open('NCAA_MM_Results.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)

	header = reader.next()

	for row in reader:
		year = row[0][-2:]
		if int(year) < 85:
			year = "20" + year
		else:
			year = "19" + year
		game = games[row[1]]
		winner = int(row[3])
		loser = int(row[6])
		if winner > loser:
			print year, game, winner, loser
			yearIdx = gameIdx[game]
			try:
				upsetCounts[year] += 1
				upsetSizes[year] += winner - loser
				upsetArrays[year][yearIdx] += 1
			except:
				upsetCounts[year] = 1
				upsetSizes[year] = winner - loser
				upsetArrays[year] = [0,0,0,0,0,0]
				upsetArrays[year][yearIdx] += 1
	ret = []
	totalSinceNewEra = 0
	total = 0
	for year in upsetCounts.keys():
		tup = (year, upsetCounts[year], upsetSizes[year])
		totalSinceNewEra += upsetCounts[year]
		total += upsetSizes[year]
		ret.append(tup)
	ret.sort()
	for tup in ret:
		print tup
	print "Upsets per year: " , totalSinceNewEra / (2016-1985.0)
	print "Upset sizes per year:", total / (2016-1985.0)
	#print upsetArrays

	upsetsPerGame = copy.deepcopy(upsetArrays)

	#make upset arrays per game instead of raw counts
	for yearKey in upsetsPerGame:
		for idx in range(len(upsetsPerGame[yearKey])):
			#print "1" , upsetsPerGame[yearKey][idx]
			upsetsPerGame[yearKey][idx] = upsetsPerGame[yearKey][idx] / (gameIdxRev[idx] / 2.0)
			#print "2" , upsetsPerGame[yearKey][idx]
	#print upsetsPerGame
	#print upsetArrays


#make tuples for upsets in first first round vs last 5 rounds
#write last created tuples to excel file
with open("cbb_upsets_per_round.csv", 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Year", "First Round Upsets", "Rest of Tourney Upsets", "Second Round Upsets"])
	for seasonNum in range(32):
		year = str(1985 + seasonNum)
		upsetArray = upsetArrays[year]
		#upsets in first round
		firstRoundUpsets = upsetArray[0]
		#upsets in rest of tournament
		restUpsets = 0
		#upsets in first two rounds
		secondRoundUpsets = upsetArray[1]
		for round in range(6):
			if round == 0:
				restUpsets += 0
			else:
				restUpsets += upsetArray[round]
		tup = (year,firstRoundUpsets,restUpsets,secondRoundUpsets)
		print tup
		writer.writerow(tup)
















