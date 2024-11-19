# Next-Salah
A python program to print out the next salah comming and the remaining time to it.

I have used [Salah tool](https://pypi.org/project/salat/) to calculate the salat times using the equation of time and elevation angle of the sun, so a big thank to these brilliant guys.

# Notes

U have a part in the [main.py](./main.py) at the start which is the constants u want to use

```py
python main.py PRAYER_NAME --lat LAT --long LONG --timedelta TIMEDELTA --sunrise 
```
Or if you have installed the ELF file then you can execute it without the python command
```bash
salah PRAUER_NAME --lat LAT --long LONG --timedelta TIMEDELTA --sunrise 
```
lat: latitude
longg: longitude
sunrise: if u want to count duha
timeDiff: time after/before GMT time
prayer_name: the name of the prayer u want to print out it's time

Don't forget that all these are optional arguments you can read the source file to know the default values for them.

# Arguments
Without any argument it will print out the time remain/after the nearest salah till 20min after the azan

But u can also choose a specific salah time by typing it (fajr, sunrise, dhuhr, asr, maghrib, isha)

You can also choose to print out the time of the next salah by typing "next"
