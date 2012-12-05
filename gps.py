# Joshua M Reynolds
# Date: October 15, 2012
# GPS Assignment
#
# Create a gps that saves the waypoints of the user. Have
# the program get input from the user. GPS to be able
# to find the length of a given path and should be able
# to calculate the distance.

import random
import math

def gpsGetLongLat():
	latitude = (random.random()*360) - 180
	longitude = 0.0
	return latitude, longitude

class Waypoint(object):
	def __init__(self, latitude, longitude, name=''):
		self.latitude = latitude
		self.longitude = longitude
		self.name = name
	
class Path(object):
	def __init__(self, name=''):
		# set empty waypoint list 
		self.waypoints = []
		self.name = name
		
	def add_waypoint(self, waypoint):
		self.waypoints.append(waypoint)

	def distance(self):

		"""calculates distances between two points"""

		radius = 6371
		if len(self.waypoints) < 2:
			return 0
		d1 = 0

		for index in range(1, len(self.waypoints)):
			w1 = self.waypoints[index - 1]
			w2 = self.waypoints[index]

			dlat = math.radians(w2.latitude-w1.latitude)
			dlong = math.radians(w2.longitude - w1.longitude)

			a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(w1.latitude)) \
			* math.cos(math.radians(w2.latitude)) * math.sin(dlong/2) * math.sin(dlong/2)
			c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
			d1 += radius * c
		return d1

		

w2 = Waypoint(39.83333, -98.5833,'Middle of USA')
w3 = Waypoint(40.0755, -76.3299,'Olivet, MI')
w4 = Waypoint(24.00, -10, 'I have no Idea')


p1 = Path('Here to Lebanon, KS')
p1.add_waypoint(w3)
p1.add_waypoint(w2)

p2 = Path('Here and Back Again')
p2.add_waypoint(w3)
p2.add_waypoint(w2)
p2.add_waypoint(w4)
p2.add_waypoint(w3)

p3 = Path('No idea where I\'m at')
p3.add_waypoint(w2)
p3.add_waypoint(w4)

print p1.distance()
print p2.distance()
print p3.distance()
