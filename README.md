# Next-Salah

A python program to print out the next salah comming and the remaining time to it.

I have used [Salah tool](https://pypi.org/project/salat/) to calculate the salat times using the equation of time and elevation angle of the sun, so a big thank to these brilliant guys.

# Installation

## Install the package to your system
To install the package to your system run this command in the root directory

```sh
pip install -e .
```

## Using Docker
You can also use docker to run the program by building the image and running it

```sh
docker build -t next-salah .
docker run --rm next-salah <arguments>
```

# Usage

If you have installed the package to your system then you can use the following command to get the next salah time

```sh
next-salah PRAYER_NAME --lat LAT --long LONG --timedelta TIMEDELTA --sunrise
```

or you can run the main.py file directly without installtion by typing the following command

```sh
python main.py PRAYER_NAME --lat LAT --long LONG --timedelta TIMEDELTA --sunrise
```

# Arguments

lat: latitude
longg: longitude
sunrise: if u want to count duha
timeDiff: time after/before GMT time
prayer_name: the name of the prayer u want to print out it's time

Don't forget that all these are optional arguments you can read the source file to know the default values for them.

Without any argument it will print out the time remain/after the nearest salah till 20min after the azan

But u can also choose a specific salah time by typing it (fajr, sunrise, dhuhr, asr, maghrib, isha)

You can also choose to print out the time of the next salah by typing "next"
