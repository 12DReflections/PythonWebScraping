#!/usr/bin/python

import datetime
import random
import sys
def main():
	times_per_week = 5

	run_random_time(times_per_week)





def run_random_time(times_per_week):#      (#script_object, times_per_week):
	day_of_week = datetime.date.today().weekday() # 0 is Monday, 6 is Sunday
	time = datetime.datetime.now().time()
#	
	r_week   = random.randint(0, 6) # 0 is Monday, 6 is Sunday
	
	t_list = time_list(times_per_week) #Generate list of random times
	for t in t_list:
		print t
	# Generates a list of random times 
	times_to_run = times_per_week

	# 1 day of the week Perform action on a day between hours
	# if (day_of_week == r_week) and (time == r_time):
	#      print 'hello'

	# Run any number of times
	count = 0
	while count < times_to_run:
		print 'hello'
		if (day_of_week == r_week) and (time == r_time):
			print 'uncomment object'
			#run script
			#script_object.dosomething()

		count +=1

# Returns a list of random times
def	time_list(times_per_week):
	r_time = []
	count = 0
	while count < times_per_week:
		r = rand_time_gen()
		r_time.append(r)
		count +=1
	return r_time

def rand_time_gen():
	## Generate random time

	r_hour 	 = random.randint(8, 22) 
	r_minute = random.randint(0, 59)
	r_sec    = random.randint(0, 59)
	r_msec   = random.randint(0, 999999)
	r_time   = datetime.time(r_hour, r_minute, r_sec, r_msec)
	return r_time

if __name__ == '__main__':
	main()




# def main():
# 	day_of_week = datetime.date.today().weekday() # 0 is Monday, 6 is Sunday
# 	time = datetime.datetime.now().time()
# #	print time

# 	## Generate random time
# 	r_week   = random.randint(0, 6) 
# 	r_hour 	 = random.randint(8, 22) 
# 	r_minute = random.randint(0, 59)
# 	r_sec    = random.randint(0, 59)
# 	r_msec   = random.randint(0, 999999)
# 	r_time   = datetime.time(r_hour, r_minute, r_sec, r_msec)

# 	## User enter
# 	times_to_run = 5

# 	# 1 day of the week Perform action on a day between hours
# 	# if (day_of_week == r_week) and (time == r_time):
# 	#      print 'hello'

# 	# Run any number of times
# 	count = 0
# 	while count < times_to_run:
# 		if (day_of_week == r_week) and (time == r_time):
# 			#run script
# 			print 'script here'

# 		count +=1