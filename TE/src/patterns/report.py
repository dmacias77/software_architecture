# Created by David Macías (MX)
from abc import ABC, abstractmethod

# MX: Class Report works as an Abstract Factory. It is
#     the definition of the interface to create different
#     types of report. This superclass contains five
#     abstract classes that create a common interface for
#     different reports. Only create_content is defined,
#     considering it's a standard for all subclasses'
#     initialization, hence it's always called.
class Report(ABC):
  def create_content(self, data):
    builder = [self._create_headers("Taxi Report"), self._create_table_headers()]
    for i in data:
      builder.append(self._add_ride(i))
    builder.append(self._close_table_headers())
    return self._join(builder)

  # Write to file.
  @abstractmethod
  def build(self, content: str):
    pass

  # Add element in file's format.
  @abstractmethod
  def _add_ride(self, ride):
    pass

  # End file definition in format.
  @abstractmethod
  def _close_table_headers(self):
    pass

  # Define title in file's format.
  @abstractmethod
  def _create_headers(self, title):
    pass

  # Print table titles in format.
  @abstractmethod
  def _create_table_headers(self):
    pass

  # Auxiliary to join all elements.
  def _join(self, content):
    return "".join(content)
