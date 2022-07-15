import pandas as pd
import csv, sys, getopt


def main(file_name):
    sensor_data = pd.read_csv(file_name, names=["Reading Date", "Sensor Identifier", "Num Entities"], dtype={"Reading Date": "str", "Sensor Identifier": "str", "Num Entities": "int64"})
    grouped_frame = sensor_data.groupby(by=["Sensor Identifier"]).max()
    if grouped_frame.empty:
        print('No sensor readings found')
    else:
        print('Sensor Statistics:')
        print(str(grouped_frame))

if __name__ == "__main__":
   inputfile = ''
   try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile="])
   except getopt.GetoptError:
      print('main.py -f <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('main.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   main(inputfile)