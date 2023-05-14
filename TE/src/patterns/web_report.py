# Edited by David Macías (MX)
from patterns.report import Report

# MX: Now WebReport is a dependent object from Report, so it
#     can be implemented as a subclass of an Abstract Factory.
#     Now create_content is defined in the superclass.
class WebReport(Report):
  def __init__(self, data):
    self.content = self.create_content(data)

  # MX: Added tabs and endls to the generation for aesthetics.
  def build(self):
    with open("financial-report.html", "w") as report:
      report.write(self.content)

  def _add_ride(self, ride):
    return "".join([
      "\t\t<tr>\n",
      f"\t\t\t<td>{ride.taxi_id}</td>\n",
      f"\t\t\t<td>{ride.pick_up_time.isoformat()}</td>\n",
      f"\t\t\t<td>{ride.drop_of_time.isoformat()}</td>\n",
      f"\t\t\t<td>{ride.passenger_count}</td>\n",
      f"\t\t\t<td>{ride.trip_distance} km</td>\n",
      f"\t\t\t<td>{_format_amount(ride.tolls_amount)}</td>\n",
      "\t\t</tr>\n"
    ])

  def _create_headers(self, title: str):
    return f"<!DOCTYPE html>\n<head>\n\t<title>{title}</title>\n</head>\n<body>\n\t<h1>{title}</h1>"

  def _create_table_headers(self):
    return """
    <table>
      <tr>
        <th> TaxiID </th>
        <th> Pickup time </th>
        <th> Dropoff time </th>
        <th> Passenger count </th>
        <th> Trip Distance </th>
        <th> Total amount </th>
      </tr>
    """

  def _close_table_headers(self):
    return "\t</table>"

# Auxiliary function to format negative numbers.
# MX: I was going to add it to the abstract methods, but
#     maybe not all formats will need a special formatting
#     for negatives. Just, coincidentially, these two
#     need it.
def _format_amount(amount):
  if amount < 0:
    return f"<span style='color:red'>{amount}</span>"
  return str(amount)
