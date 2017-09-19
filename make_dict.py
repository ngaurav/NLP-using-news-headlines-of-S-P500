import csv
file = open('dict.csv','w')
f1 = open('snp500_formatted.txt','r')
f2 = open('../nlp/snp500_formatted.txt','r')
c = csv.writer(file)
c1 = csv.reader(f1)
c2 = csv.reader(f2)
c1 = list(c1)
c2 = list(c2)

for i in range(len(c1)):
	data = []
	data.extend((c1[i][0],c2[i][0]))
	c.writerow(data)

