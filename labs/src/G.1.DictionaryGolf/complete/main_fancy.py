"""



"""

from roster import roster
from collections import defaultdict


def sort(frequencies):
  return sorted(frequencies,key=lambda t: t[1],reverse=True)


def frequencies_by(students,field):
  """

  Args:
      students: list of student records
      field: field that we're counting on. i.e. 'surname'

  Returns: Sorted list of frequent fields
  """
  counts = defaultdict(int)
  for student in roster:
    counts[student[field]] +=1
  return sort(counts.items())


def report_frequencies(frequencies):
  for item in frequencies:
    print(f'\t{item[0]}: {item[1]}')


def main():
  print(f'\nHere are the top 5 surnames:')
  top_5_surnames = frequencies_by(roster,'surname')[:5]
  report_frequencies(top_5_surnames)

  print(f'\nHere are the top 5 given names:')
  top_5_givenNames = frequencies_by(roster,'givenName')[:5]
  report_frequencies(top_5_givenNames)

  print(f'\nHere are the class sizes:')  
  class_sizes = sorted(frequencies_by(roster,'grade'),key=lambda pair: pair[0])
  report_frequencies(class_sizes)

  print(f'\n')



if __name__ == "__main__":
    main()
