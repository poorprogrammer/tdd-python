from datetime import *
from dateutil.relativedelta import *
import calendar

def get_effective_date(year, month, day, duration):
	current_date = date(year, month, day)
	current_business_date = get_current_business_date(current_date)
	next_business_date = get_next_business_date(current_date)
	
	if duration == 0 : 
		if current_business_date == current_date :
			return current_business_date
		else : 
			return next_business_date

	while duration > 0 :
		effective_date = next_business_date + timedelta(days=1)
		next_business_date = next_business_date + timedelta(days=1)
		if is_work_date(effective_date) :
			duration = duration - 1

	return effective_date
	
def get_current_business_date(current_date) :
	if is_work_date(current_date) :
		return current_date
	else : 
		return get_current_business_date(current_date - timedelta(days = 1))

def get_next_business_date(current_date):
	if is_work_date(current_date) :
		return current_date
	else : 
		return get_next_business_date(current_date + timedelta(days = 1))

def is_work_date(current_date) :
	return current_date.isoweekday() in range(1, 6)
