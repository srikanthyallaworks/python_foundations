from roster import roster


def run_surname_report():
  """Prints a report of surnames shared by at least
  3 people on the roster
  """
  print(f'\nHere are some common surnames:')  
  surname_counts = {}
  
  # TODO: Magic goes here 

  for surname,count in surname_counts.items():
    print(f'\t{surname}: {count}')  



def run_class_size_report():
  """Prints a report of the school population by grade
  """

  print(f'\nHere are the students in each grade:')  
  grade_counts = { 1:0, 2:0, 3:0,4:0,5:0}

  # TODO: Magic goes here 

  for grade,count in grade_counts.items():
    print(f'\t{grade}: {count}')   



def main():
  print('\n=========================')
  run_surname_report()
  run_class_size_report()
  print('\n=========================')



if __name__ == "__main__":
    main()
