from random import choice
import getopt, sys

class Dice(object):
	die = {	"b": ["blank", "blank", "success", "advantage", "two advantage", "advantage + success"],
		"a": ["blank", "two advantage", "success", "advantage", "two success", "advantage + success", "advantage", "success"],
		"p": ["blank", "success", "success", "two success", "two success", "advantage", "success + advantage", "success + advantage", "success + advantage", "two advantage", "two advantage", "triumph"],
		"s": ["blank", "blank", "failure", "failure", "threat", "threat"],
		"d": ["blank", "threat", "two threat", "threat", "threat", "threat", "two threat", "failure + threat"],
		"c": ["blank", "failure", "failure", "two failure", "two failure", "threat", "threat", "failure + threat", "failure + threat", "two threat", "two threat", "despair"],
		"f": ["dark", "dark", "dark", "dark", "dark", "dark", "two dark", "light", "light", "two light", "two light", "two light"],
		"1": ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"],
		"0": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
			}
	def __init__(self, type):
		self.type = type

	def roll(self):
		print choice(self.die[self.type])

def run(pool):
	for c in pool:
		Dice(c.lower()).roll()

if __name__ == '__main__':	#command line interface
	pool = None
	try:
		myopts, args = getopt.getopt(sys.argv[1:],"p:")
	except getopt.GetoptError as e:
		print (str(e))
		print("Usage: %s -p pool" % sys.argv[0])
		sys.exit(2)

	for o, a in myopts:
		if o == '-p':
			pool = a
	run(pool)
