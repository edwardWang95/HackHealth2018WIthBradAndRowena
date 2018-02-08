import pandas
import xlrd
from pandas import ExcelWriter
from pandas import ExcelFile




textFile = open("HackathonDataTextFormatted.txt", "w")
reader = pandas.read_csv("city_of_new_york.csv")
print(reader.columns)

for i in reader.index:
    textFile.write(str(reader["NUMBER"][i]))
    textFile.write(" ")
    textFile.write(str(reader["STREET"][i]))
    textFile.write(" ")
    textFile.write(str(reader["POSTCODE"][i]))
    textFile.write("\n")






textFile.close()