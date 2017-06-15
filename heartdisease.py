import csv
from BeautifulSoup import BeautifulSoup
mortality = {}
min_value = 0; max_value = 2000
reader = csv.reader(open('heartdisease.csv'), delimiter=",")
for row in reader:
	try:
		fips = row[17]
		rate = float(row[7])
		mortality[fips] = rate
	except:
		pass

svg = open('counties.svg' , 'r').read()

soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])

paths = soup.findAll('path')

colors = ["#fee5d9" , "#fcbba1" , "#fc9272" , "#fb6a4a" , "#ef3b2c" , "#cb181d" , "#99000d"]

path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt; marker-start:none;stroke-linejoin:bevel;fill:'

for p in paths:
	if p['id'] not in ["State_Lines" , "separator"]:
		try:
			rate = mortality[p['id']]
		except:
			continue

		if rate > 1500:
			color_class = 6
		elif rate > 1000:
			color_class = 5
		elif rate > 600:
			color_class = 4
		elif rate > 300:
			color_class = 3
		elif rate > 100:
			color_class = 2
		elif rate > 50:
			color_class = 1
		else:
			color_class = 0

		color = colors[color_class]
		p['style'] = path_style + color

print soup.prettify()
