# gloc
Command-line utility for quick geoIP check of specific IP address (or a list of)

usage: gloc.py [-h] [-f FORMAT] [-i INPUT] [-o OUTPUT] ip

positional arguments:
  ip                    ip to geolocate

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        data format to return - json, csv, or xml,
                        default=json
  -i INPUT, --input INPUT
                        name of the file to input list of ip adressess
  -o OUTPUT, --output OUTPUT
                        name of the file to output to
                        
  gloc relies of freegeoip.net database and is capable of reading and writing in json (default), csv and xml formats.
  It is very handy utility for quick geoIP checks of IP lists.
