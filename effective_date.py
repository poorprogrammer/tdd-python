from datetime import *

def get_effective_date(year, month, day, duration):
	given_date = date(year, month, day)
	current_business_date = get_current_business_date(given_date)
	next_business_date = get_next_business_date(given_date)
	
	if duration == 0 : 
		if is_work_date(given_date) :
			return current_business_date
		else : 
			return next_business_date

	while duration > 0 :
		effective_date = next_business_date + timedelta(days=1)
		next_business_date = next_business_date + timedelta(days=1)
		if is_work_date(effective_date) :
			duration = duration - 1

	return effective_date
	
def get_current_business_date(given_date) :
	if is_work_date(given_date) :
		return given_date
	return get_current_business_date(given_date - timedelta(days = 1))

def get_next_business_date(given_date):
	if is_work_date(given_date) :
		return given_date
	return get_next_business_date(given_date + timedelta(days = 1))

def is_work_date(given_date) :
	return given_date.isoweekday() in range(1, 6)
