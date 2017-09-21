from variables import *
from pylab import *
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt, mpld3

colours = ['#F0D41F','r','g']
medias = ['#1F80F0','#1FBEF0','#DD1132','#0EEC91']
fracs_bpce = [12,13,12]
fracs_ce = [10,7,19]
fracs_bp = [16,12,3]
fracs_natixis = [19,11,5]
fracs_sources = [10,10,10,10]
labels_avis = 'Neu.', 'Neg.', 'Pos.'
labels_sources = 'Fac.', 'Twi.','Goo','Web'

explode=(0, 0, 0, 0)

# Make square figures and axes

the_grid = GridSpec(4, 4)

figure(1, figsize=(9,9))

subplot(the_grid[0,0])

title('BPCE')
pie(fracs_bpce, labels=labels_avis, autopct='%0.1f%%',radius=2.25, shadow=False,colors=colours, startangle=90)

subplot(the_grid[0,3])

title('SOURCES')
pie(fracs_sources, labels=labels_sources, autopct='%0.1f%%',radius=2.25, shadow=False,colors=medias, startangle=90)

subplot(the_grid[2,0])

title('BPCE')
pie(fracs_bpce,radius=0.9, labels=labels_avis, autopct='%0.1f%%', shadow=False,colors=colours, startangle=90)

subplot(the_grid[2, 1])

title("Caisse d'Eparge")
pie(fracs_ce,radius=0.9, labels=labels_avis, autopct='%0.1f%%', shadow=False,colors=colours, startangle=90)

subplot(the_grid[2, 2])

title("Banque Populaire")
pie(fracs_bp, radius=0.9, labels=labels_avis, autopct='%0.1f%%', shadow=False,colors=colours, startangle=90)

subplot(the_grid[2, 3])

title("Natixis")
pie(fracs_natixis,radius=0.9, labels=labels_avis, autopct='%0.1f%%', shadow=False,colors=colours, startangle=90)

subplot (the_grid[3,0])

y = [pop_prod, pop_com, pop_gouv, pop_perf, pop_concur, pop_digital, 10, 8.1]
N = len(y)
x = range(N)
width = 0.25/0.5
bar(x, y, width, color="blue")

subplot (the_grid[3,1])

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 0.25/0.5
bar(x, y, width, color="blue")

subplot (the_grid[3,2])

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 0.25/0.5
bar(x, y, width, color="blue")

subplot (the_grid[3,3])

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 0.25/0.5
bar(x, y, width, color="blue")

figure(2, figsize = (9,9))

show()
