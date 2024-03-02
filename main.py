#!/sbin/python
import salat as st
import datetime as dt
from datetime import datetime
import time as timeModule
#date = datetime.today()
lat = 30
longg = 31
sunrise = True
timeDiff = 2
calcMethod = st.CalculationMethod.EGYPT
asrMethod = st.AsrMethod.STANDARD


def getTimeArr(date):
	# Arguments:
	#	Date: date of the targeted day as dt.date(year,month,day)
	#	lat: latitude of the location
	#	longg: longitude of the location
	#	sunrise: add the sunrise to the list of it's true
	#	timeDiff: UTC+X, it's the X 
	#	calcMethod: prayer calculation method st.CalculationMethod.METHOD
	#	asrMethod: asr prayer calculation method sr.AsrMethod.STANDARD
	# Returns:
	#	dictionary contains the prayers time of the day as "%I:%M:%S %p"
	pt = st.PrayerTimes(calcMethod,asrMethod)

#	date = dt.date(2024,2,27)

#	lat = 30
#	longg = 31
	def negativeTimeToDelta(time):
		posTime = time % 24
		return dt.timedelta(hours=posTime)
	timeDelta = negativeTimeToDelta(timeDiff)
	zone = dt.timezone(timeDelta)
	
	prayer_times = pt.calc_times(date,zone,longg,lat)


	dic = {}
	# fajr 
	# sunrise
	# dhuhr
	# asr
	# maghrib
	# isha
	for name,time in prayer_times.items():
		#newTime = time.strftime("%Y-%m-%d %H:%M:%S")
		newTime = datetime.combine(date,time.time())
		if sunrise == False:
			if name != "sunrise":
				#dic[name]= timeModule.strptime(newTime,"%Y-%m-%d %H:%M:%S")
				dic[name]= newTime
		else:
			dic[name] = newTime
	return dic

def subTime(now, salah):
	# Arguments
	#	now: The time at this moment
	#	salah: The time of the salah to calculate the remaining on it
	# Returns:
	#	the difference in seconds
	return (salah - now).total_seconds()

def allSalahTimes():
	# Returns: 
	# 			dictionary of today's prayer times in a dictionary
	# 			and adds item "nfajr": next Fajr time
	today = datetime.today()
	tomorrow = dt.date(today.year,today.month,today.day+1)
	todayTimes = getTimeArr(today)
	nextFajr = getTimeArr(tomorrow)['fajr']
	now = datetime.now()
	prayers = {}
	for name,time in todayTimes.items():
		prayers[name] = time
	prayers['nfajr'] = nextFajr
	return prayers


def nearestSalah(allTimes):
	# Returns:
	# 			An array [next salah name, time remain]
	now = datetime.now()
	for name,time in allTimes.items():
		if subTime(now,time) > 0:
			if name == 'nfajr':
				name = 'fajr'
			return [name,int(subTime(now,time) / 60)]
	

times = allSalahTimes()
nearestSalahArr = nearestSalah(times)
nearestSalahName = nearestSalahArr[0].capitalize()
nearestSalahMin = int(nearestSalahArr[1])
nearestSalahTime = dt.time(hour=nearestSalahMin // 60,minute=nearestSalahMin % 60)
nearestSalahTimeStr = nearestSalahTime.strftime("%H:%M")
output = nearestSalahName + "-> " + nearestSalahTimeStr

print(output)
# print(nearestSalah(times))
