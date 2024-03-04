#Source: https://stackoverflow.com/questions/56659854/typeerror-nonetype-object-is-not-subscriptable-only-showing-on-second-iterati
while True:
    print_menu();

    try:
      choice = int(input("What is your choice?: "));

    except:
      print("Please enter an integer only");
      continue;

    if choice == 1:
      Process_a_new_data_file(current_set);

    elif choice == 2:
      Choose_units();


def Choose_units():
    global current_units
    if current_units is not None:
            print("a")
    print(current_units)
    units_used = UNITS.get(current_units)[0]
    print("Current units in " + units_used)
    print("Choose new units:\n")
    for i in UNITS:
        print(str(i) + " - " + UNITS[i][0])
    while True:
        current_units = input("Which unit?\n")
        for i in UNITS:
            if(int(current_units) == i):
                return
        print("Please choose a unit from the list")
        continue