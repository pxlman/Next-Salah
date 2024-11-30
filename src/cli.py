import argparse
from .prayer_times import PrayerTimeCalculator

def main():
    parser = argparse.ArgumentParser(description="A powerful tool to get the upcoming prayer times")
    parser.add_argument("--lat", type=float, help="Latitude of the location", default=30)
    parser.add_argument("--long", type=float, help="Longitude of the location", default=31)
    parser.add_argument("--timedelta", type=int, help="The time difference between the location and GMT+0", default=2)
    parser.add_argument("--sunrise", action="store_true", help="Consider sunrise in prayer times", default=True)
    parser.add_argument("salah", type=str, help="Prayer name", nargs="?")

    args = parser.parse_args()

    calculator = PrayerTimeCalculator(
        lat=args.lat,
        long=args.long,
        time_delta=args.timedelta,
        calc_sunrise=args.sunrise
    )

    times = calculator.get_all_salah_times()
    nearest_salah_arr = calculator.get_nearest_salah(times)
    
    if nearest_salah_arr:
        nearest_salah_name = nearest_salah_arr[0].capitalize()
        nearest_salah_remain = nearest_salah_arr[1]
        sign = nearest_salah_arr[3]
        
        if sign == "+":
            time_str = nearest_salah_remain.strftime("%M:%S")
        else:
            time_str = nearest_salah_remain.strftime("%H:%M")

        try:
            if args.salah in ["fajr", "sunrise", "dhuhr", "asr", "maghrib", "isha"]:
                print(times[args.salah].strftime("%I:%M"))
            elif args.salah == "next":
                print(nearest_salah_name)
            else:
                print(f"{sign}{time_str}")
        except:
            print(f"{sign}{time_str}")

if __name__ == "__main__":
    main() 