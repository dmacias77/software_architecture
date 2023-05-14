# Created by David Macías (MX)
from patterns.report import Report

# MX: TextReport is a subclass of Report.
class TextReport(Report):
  def __init__(self, data):
    self.content = self.create_content(data)

  def build(self):
    with open("financial-report.txt", "w") as file:
      file.write(self.content)

  def _add_ride(self, ride):
    return f"{_fit(ride.taxi_id, 6, 'l')} | {ride.pick_up_time.isoformat()} | {ride.drop_of_time.isoformat()} | {_fit(ride.passenger_count, 10, 'c')} |   {_fit(str(ride.trip_distance)+'  km', 9, 'r')}   | {_fit(_format_amount(ride.tolls_amount),8,'r')}\n"

  def _create_headers(self, title: str):
    return f"{title.upper()}\n\n"

  def _create_table_headers(self):
    return f"TaxiID | {_fit('Pickup time', 19, 'c')} | {_fit('Dropoff time', 19, 'c')} | Passengers | Trip Distance | Total amount\n{_line(95)}\n"

  def _close_table_headers(self):
    return ""

# Auxiliary functions to beautify table printing.
def _fit(element, size, align):
  if not isinstance(element, str):
    element = str(element)
  if align == "c":
    spl = int((size - len(element)) / 2)
    if (size - len(element)) % 2 == 1:
      spr = int((size - len(element)) / 2) + 1
    else: spr = spl
    return (" " * spl) + element + (" " * spr)
  elif align == "l":
    sp = size - len(element)
    return element + (" " * sp)
  else:
    sp = size - len(element)
    return (" " * sp) + element

def _line(size):
  return "-" * size

# Auxiliary function to format negative numbers.
def _format_amount(amount):
  if amount < 0:
    return f"(-{abs(amount)})"
  return str(amount)
