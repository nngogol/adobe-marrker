import csv
import codecs

# your file in .csv
ya_awesome_file = 'adobe_markers.csv'

# language
lang = 'rU'

data = csv.reader(codecs.open(ya_awesome_file, lang, 'utf-16'), delimiter='\t')

print("\t\tIn - Out === Name", len(str(list(data)[1][2])))

# it is a stupid hack.
# i need to know "is '00:00:00:00' have len = 10+1?"
# ttti stores given value and if it's == 11, then there will be result
ttti = -1
for i in data:
	if i[0] == 'Marker Name':
		continue
	else:
       ttti = len(i[3])
	   break

if ttti == 11:

    for i in data:
        name, time_in, time_out = i[0], i[2], i[3]

        time_in = str(time_in)[:-3]
        time_out = str(time_out)[:-3]

        if time_in[:2] == '00':
            time_in = time_in[3:]

        if time_out[:2] == '00':
            time_out = time_out[3:]

        print("{0} - {1} === {2}".format(time_in, time_out, name))
