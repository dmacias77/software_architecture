# Edited by David Macías (MX)
from patterns.factory import RepCreator

CSV_FILE = "taxi-data.csv"

def main():
  # MX: Creation of RepCreator singleton.
  xrep = RepCreator.factory()
  # MX: Because of Factory Method Pattern, main can
  #     create reports of different types without
  #     having to know the exact class of object that
  #     will be needed. RepCreator returns different
  #     report objects based on its arguments.
  rides = xrep.parse("CSV", CSV_FILE)
  xrep.generate("HTML", rides).build()
  xrep.generate("text", rides).build()

if __name__ == '__main__':
  main()
