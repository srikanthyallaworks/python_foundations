try:
    from .roster import roster
except:
    from roster import roster


def run_surname_report():
    """Prints a report of surnames shared by 
       at least 3 people on the roster.
    """
    print(f'\nHere are some common surnames:')
    surname_counts = {}
    for surname in [s['surname'] for s in roster]:
        surname_counts[surname] = surname_counts.setdefault(surname, 0)+1

    for surname, count in surname_counts.items():
        if count > 2:
            print(f'\t{surname}: {count}')


def run_class_size_report():
    """Prints a report of the school population 
       by grade
    """
    print(f'\nHere are the students in each grade:')
    grade_counts = {}
    for grade in [student['grade'] for student in roster]:
        grade_counts[grade] = grade_counts.setdefault(grade, 0) + 1

    for grade, count in grade_counts.items():
        print(f'\t{grade}: {count}')


def main():
    print('\n=========================')
    run_surname_report()
    run_class_size_report()
    print('\n=========================')


if __name__ == "__main__":
    main()
