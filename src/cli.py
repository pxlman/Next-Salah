import argparse
import os
import yaml
from .prayer_times import PrayerTimeCalculator

DEFAULTS = {
    "lat": 30,
    "long": 31,
    "timedelta": 2,
    "sunrise": True
}

def load_config(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config

class Config:
    def __init__(self, lat=30, long=31, timedelta=2, sunrise=True):
        self.lat = lat
        self.long = long
        self.timedelta = timedelta
        self.sunrise = sunrise

def main():
    parser = argparse.ArgumentParser(description="A powerful tool to get the upcoming prayer times")
    parser.add_argument("--lat", type=float, help="Latitude of the location")
    parser.add_argument("--long", type=float, help="Longitude of the location")
    parser.add_argument("--timedelta", type=int, help="The time difference between the location and GMT+0")
    parser.add_argument("--sunrise", action="store_true", help="Consider sunrise in prayer times")
    parser.add_argument("--config", type=str, help="The config file", default="~/.config/salah/config.yml")
    parser.add_argument("salah", type=str, help="Prayer name", nargs="?")


    args = parser.parse_args()
    config_path = os.path.expanduser(args.config)
    config_loaded = load_config(config_path) if args.config else load_config(config_path)
    # print("config file:")
    # print(config_loaded.items() if config_loaded else "No config file found, using default values or command line arguments.")

    config = Config()
    if config_loaded:
        config.lat = config_loaded.get("lat", args.lat)
        config.long = config_loaded.get("long", args.long)
        config.timedelta = config_loaded.get("timedelta", args.timedelta)
        config.sunrise = config_loaded.get("sunrise", args.sunrise)

    if args.lat:
        config.lat = args.lat
    if args.long:
        config.long = args.long
    if args.timedelta:
        config.timedelta = args.timedelta
    if args.sunrise:
        config.sunrise = args.sunrise

    if not config.lat:
        config.lat = DEFAULTS["lat"]
    if not config.long:
        config.long = DEFAULTS["long"]
    if not config.timedelta:
        config.timedelta = DEFAULTS["timedelta"]
    if not config.sunrise:
        config.sunrise = DEFAULTS["sunrise"]
    
    calculator = PrayerTimeCalculator(
        lat=config.lat,
        long=config.long,
        time_delta=config.timedelta,
        calc_sunrise=config.sunrise
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
