# Next-Salah
A python program to print out the next salah comming and the remaining time to it.

I have used [Salah tool](https://pypi.org/project/salat/) to calculate the salat times using the equation of time and elevation angle of the sun, so a big thank to these brilliant guys.

# Notes

U have a part in the [main.py](./main.py) at the start which is the constants u want to use

```py
lat = float
long = float
sunrise = bool
timeDiff = int
calcMethod = st.CalculationMethod.<Method u want>
asrMethod = st.AsrMethod.<Asr method u want>
```
lat: latitude
longg: longitude
sunrise: if u want to count duha
timeDiff: time after/before GMT time
calcMethod: one of these (ISNA,EGYPT,JAFARI,KARACHI,MAKKA)
asrMethod: one of these (STANDARD,HANAFI)

# Arguments
Without any argument it will print out the time remain/after the nearest salah till 20min after the azan

But u can also choose a specific salah time by typing it (fajr,sunrise,asr,maghrib,isha)
