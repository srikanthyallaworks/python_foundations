from collections import defaultdict

try:
  from .roster import roster
except:
  from roster import roster


def get_frequencies_by(field):
  """Builds a dictionary counting repeat occurances of the specified field

  Args:
      field to count by. e.g. 'surname'

  """
  counts = defaultdict(int)
  for student in roster:
    counts[student[field]] +=1
  return counts


def sort_by_frequency(frequency_dict):
  """Sorts the specified frequency dictionary

  Returns:
      Sorted list
  """
  frequency_list = []
  for key, value in frequency_dict.items():
    frequency_list.append({
      'key':key,
      'count':value
    })
  return sorted(frequency_list,key=lambda r:r['count'],reverse=True)


def report_top_5_frequencies(field):
  counts = get_frequencies_by(field)
  sorted = sort_by_frequency(counts)
  for item in sorted[:5]:
    print(f'\t{item["key"]}: {item["count"]}')   


def run_surname_report():
  print(f'\nHere are the top 5 surnames:')  
  report_top_5_frequencies('surname')

  
def run_givenName_report():
  print(f'\nHere are the top 5 given names:')  
  report_top_5_frequencies('givenName')


def run_class_size_report():
  print(f'\nHere are the students in each grade:')
  frequencies = get_frequencies_by('grade')
  sorted_by_grade = sorted(frequencies.items(),key=lambda t:t[0])
  for grade,count in sorted_by_grade:
    print(f'\t{grade}: {count}')   



def main():
  print('\n=========================')
  run_surname_report()
  run_givenName_report()
  run_class_size_report()
  print('\n=========================')


if __name__ == "__main__":
    main()
