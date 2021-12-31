from roster import roster


def run_surname_report():
    """Prints a report of surnames shared by at least
    3 people on the roster
    """
    surname_counts = {
        "Bloggs": 1,
    }
    # TODO: Magic goes here
    print("\nHere are some common surnames:")
    for surname, count in surname_counts.items():
        print(f"\t{surname}: {count}")


def run_class_size_report():
    """Prints a report of the school population by grade"""
    grade_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    # TODO: Magic goes here
    print("\nHere are the students in each grade:")
    for grade, count in grade_counts.items():
        print(f"\t{grade}: {count}")


def main():
    print("\n=========================")
    run_surname_report()
    run_class_size_report()
    print("\n=========================")


if __name__ == "__main__":
    main()
