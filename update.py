import csv

count = 1

#seperator = ' '

with open('ip.txt', 'r+') as f:

	read = csv.reader(f, delimiter = ' ', quotechar='|') 

	with open('mdl.list', 'w+') as mdl:
		write = csv.writer(mdl)
		for id in read:
			count = count+1
			score = count

			if count > 100:
				score = 1
			elif count < 10:
				score = 127

			write.writerow((id[0], 1, score)) 
