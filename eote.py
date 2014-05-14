from random import randint
import getopt, sys

class Boost(object):
	die = {1: "blank", 2:"blank", 3: "success", 4: "advantage", 5: "two advantage", 6: "advantage + success"}

	@classmethod
	def roll(self):
		print self.die[randint(1, 6)]

class Ability(object):
	die = {1: "blank", 2:"two advantage", 3: "success", 4: "advantage", 5: "two success", 6: "advantage + success", 7: "advantage", 8: "success"}

	@classmethod
	def roll(self):
		print self.die[randint(1, 8)]

class Proficiency(object):
	die = {1: "blank", 2:"success", 3: "success", 4: "two success", 5: "two success", 6: "advantage", 7: "success + advantage", 8: "success + advantage", 9: "success + advantage", 10: "two advantage", 11: "two advantage", 12: "triumph"}

	@classmethod
	def roll(self):
		print self.die[randint(1, 12)]

class Setback(object):
	die = {1: "blank", 2:"blank", 3: "failure", 4: "failure", 5: "threat", 6: "threat"}

	@classmethod
	def roll(self):
		print self.die[randint(1, 6)]

class Difficulty(object):
	die = {1: "blank", 2:"threat", 3: "two threat", 4: "threat", 5: "threat", 6: "threat", 7: "two threat", 8: "failure + threat"}

	@classmethod
	def roll(self):
		print self.die[randint(1, 8)]

class Challenge(object):
	die = {1: "blank", 2:"failure", 3: "failure", 4: "two failure", 5: "two failure", 6: "threat", 7: "threat", 8: "failure + threat", 9: "failure + threat", 10: "two threat", 11: "two threat", 12: "despair"}

	@classmethod
	def roll(self):
		print self.die[randint(1, 12)]

class Force(object):
	die = {1: "dark", 2:"dark", 3: "dark", 4: "dark", 5: "dark", 6: "dark", 7: "two dark", 8: "light", 9: "light", 10: "two light", 11: "two light", 12: "two light"}

	@classmethod
	def roll(self):
		print self.die[randint(1, 12)]

class Decader(object):
	die = {1: "10", 2: "20", 3: "30", 4: "40", 5: "50", 6: "60", 7: "70", 8: "80", 9: "90", 10: "100"}

	@classmethod
	def roll(self):
		print self.die[randint(1, 10)]

class D10(object):
	@classmethod
	def roll(self):
		print randint(1, 10)

def run(pool):
	for i in range(len(pool)):
		type = pool[i]

		if type == "a":
			Ability.roll()
		elif type == "b":
			Boost.roll()
		elif type == "c":
			Challenge.roll()
		elif type == "p":
			Proficiency.roll()
		elif type == "s":
			Setback.roll()
		elif type == "f":
			Force.roll()
		elif type == "d":
			Decader.roll()
		elif type == "0":
			D10.roll()
		else:
			print("type not recognized")

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