import csv
import math

def stdDev(nrtg_list):
	sum = 0
	team_num = 0
	for nrtg in nrtg_list:
		sum += nrtg
		team_num += 1
	avg = sum / float(team_num)
	for idx in range(len(nrtg_list)):
		nrtg_list[idx] = (nrtg_list[idx] - avg) ** 2
	new_sum = 0
	for adj_nrtg in nrtg_list:
		new_sum += adj_nrtg
	new_avg = new_sum / float(team_num)
	std_dev = math.sqrt(new_avg)
	return std_dev

for year in range(8):
	season = 2011 + year
	filename = 'cbb' + str(season) + '.csv'
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		blank = reader.next()
		header = reader.next()

		all_nrtg = []
		for num in range(68):
			team = reader.next()
			nrtg = float(team[17])
			all_nrtg.append(nrtg)
		parity_rtg = stdDev(all_nrtg)
		print season, parity_rtg













