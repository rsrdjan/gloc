# gloc - geolocate IP adress or FQDN
# Copyright (C) 2017 Srdjan Rajcevic srdjan[@]rajcevic.net

import urllib.request
import argparse
import sys
import json


def convert(ip,req,method,input_file,output_file):
    print("Geolocating list of ip adresses... Could take a while (depending on the size of INPUTFILE)")

    with open(input_file,"r") as f:
        with open(output_file,"w") as o:
            for line in f:
                result = urllib.request.urlopen(req).read()
                if method == "json/":
                    wdata = json.loads(result)
                    o.write(str(wdata) + "\n")
                else:
                    o.write(str(result.rstrip()).lstrip('b') + "\n")
                    pass
        o.close()
    f.close()
    sys.exit()


parser = argparse.ArgumentParser()
parser.add_argument("ip", help="ip to geolocate", type=str)
parser.add_argument("-f", "--format", help="data format to return - json, csv, or xml, default=json", type=str)
parser.add_argument("-i", "--input", help="name of the file to input list of ip adressess", type=str)
parser.add_argument("-o", "--output", help="name of the file to output to", type=str)
args = parser.parse_args()

fgurl = 'http://freegeoip.net/'
if args.format == 'csv':
    method = 'csv/'
elif args.format == 'xml': 
    method = 'xml/'
else: 
    method = 'json/'

input_file = args.input
output_file = args.output

ip = args.ip
req = fgurl + method + ip

if input_file != None and output_file != None:
    convert(ip,req,method,input_file,output_file)
elif input_file != None:
    print("Missing OUTFILE to write to. Exiting...")
    sys.exit()
elif output_file != None:
    print("Missing INFILE to read from. Exiting...")
    sys.exit()
else:
    try:
        result = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        print(e.reason)
        sys.exit()

    rez = json.loads(result.decode('utf-8'))

    print("\nGeolocation results")
    print("==============================================")
    print("IP Address:      " + rez['ip'])
    print("Country code:    " + rez['country_code'])
    print("Country name:    " + rez['country_name'])
    print("Region code:     " + rez['region_code'])
    print("Region name:     " + rez['region_name'])
    print("City:            " + rez['city'])
    print("Zip code:        " + rez['zip_code'])
    print("Time zone:       " + rez['time_zone'])
    print("Latitude:        " + str(rez['latitude']))
    print("Longitude:       " + str(rez['longitude']))
    print("Metro code:      " + str(rez['metro_code']))
    print("==============================================")  
