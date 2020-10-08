'''
socratica: https://www.youtube.com/watch?v=hUes6y2b--0
tutorials point: https://www.tutorialspoint.com/hadoop/hadoop_mapreduce.htm
computerphile: https://www.youtube.com/watch?v=cvhKoniK5Uo

map-reduce is a menthod of distributing large workloads (terabytes) amongest many nodes
then combining the output after computuation.
'''

# using map reduce to calc areas of circles given their radii
from math import pi as PI
radii = [1, 2, 3, 4, 5]
area = lambda radius: 2*PI*radius
print(list(map(area, radii)))

# in one line
print(list(map(lambda r: 2*PI*r, [1, 2, 3, 4, 5])))
