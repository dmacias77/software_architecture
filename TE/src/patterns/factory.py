# Created by David Macías (MX)
from patterns.csv_utils import parse_file
from patterns.print_report import TextReport
from patterns.web_report import WebReport

# MX: RepCreator acts as the factory method and is
#     expansible in case the same issue rises again.
#     It has two methods: 'generate' for outputs,
#     and 'parse' for inputs.
class RepCreator:
  # MX: It also is a singleton to avoid having many
  #     RepCreator objects in memory, especially if
  #     it will later be connected to more subclasses.
  _instance = None

  @staticmethod
  def factory():
    if not RepCreator._instance:
      RepCreator._instance = RepCreator()
    return RepCreator._instance

  @staticmethod
  def generate(type, data):
    if type == "HTML" or type == "html":
      return WebReport(data)
    elif type == "Text" or type == "text":
      return TextReport(data)
    else:
      raise Exception("On RepCreator.generate: file type", type, "not supported.")

  @staticmethod
  def parse(type, data):
    if type == "CSV" or type == "csv":
      return parse_file(data)
    else:
      raise Exception("On RepCreator.parse: file type", type, "not supported.")
