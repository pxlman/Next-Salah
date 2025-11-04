import datetime as dt
from datetime import datetime
import salat as st

class PrayerTimeCalculator:
    def __init__(self, lat=30, long=31, time_delta=2, calc_sunrise=True):
        self.lat = lat
        self.long = long
        self.time_delta = time_delta
        self.calc_sunrise = calc_sunrise
        self.calc_method = st.CalculationMethod.EGYPT
        self.asr_method = st.AsrMethod.STANDARD

    def _negative_time_to_delta(self, time):
        pos_time = time % 24
        return dt.timedelta(hours=pos_time)

    def get_time_arr(self, date):
        pt = st.PrayerTimes(self.calc_method, self.asr_method)
        time_delta = self._negative_time_to_delta(self.time_delta)
        zone = dt.timezone(time_delta)
        
        prayer_times = pt.calc_times(date, zone, self.long, self.lat)

        dic = {}
        for name, time in prayer_times.items():
            new_time = datetime.combine(date, time.time())
            if not self.calc_sunrise and name == "sunrise":
                continue
            dic[name] = new_time
        return dic

    def get_all_salah_times(self):
        today = datetime.today()
        tomorrow = today + dt.timedelta(days=1)
        today_times = self.get_time_arr(today)
        next_fajr = self.get_time_arr(tomorrow)['fajr']
        
        prayers = today_times.copy()
        prayers['nfajr'] = next_fajr
        return prayers

    def get_nearest_salah(self, all_times):
        now = datetime.now()
        for name, time in all_times.items():
            diff_seconds = (time - now).total_seconds()
            if diff_seconds > (-25 * 60):
                sign = " "
                if diff_seconds > 0:
                    sign = "-"
                    datetime_obj = (time - now) + dt.datetime(2000,1,1,0,0,0,0)
                elif diff_seconds < 0:
                    sign = "+"
                    datetime_obj = dt.datetime(2000,1,1,0,0,0,0) + dt.timedelta(seconds=abs(diff_seconds))
                else:
                    sign = " "
                    datetime_obj = dt.datetime(2000,1,1,0,0,0,0) + dt.timedelta(seconds=abs(diff_seconds))
                
                if name == 'nfajr':
                    name = 'fajr'
                return [name, datetime_obj, time, sign]
        return None 
