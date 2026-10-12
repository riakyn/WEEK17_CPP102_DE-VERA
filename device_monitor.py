def get_initial_readings():
    readings = [28, 31, 35, 37, 29]
    return readings


def display_menu():
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    print("CURRENT READINGS")
    print("----------------")

    for i in range(len(readings)):
        print("Reading", i + 1, ":", readings[i], "°C")


def classify_reading(reading, warning_limit, critical_limit):
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def add_reading(readings, lowest, highest):
    text = input("Enter new reading: ")

    if text == "":
        print("Invalid input. The reading cannot be empty.")
    elif not text.isdigit():
        print("Invalid input. Enter a whole number only.")
    else:
        reading = int(text)

        if reading < lowest or reading > highest:
            print("Invalid reading. Enter a value from 0 to 100.")
        else:
            readings.append(reading)
            print("Reading added successfully.")


def display_classifications(readings, warning_limit, critical_limit):
    print("READING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(
            reading, warning_limit, critical_limit
        )
        print(reading, "°C ->", category)


def compute_total(readings):
    total = 0

    for reading in readings:
        total = total + reading

    return total


def compute_average(readings):
    total = compute_total(readings)
    number = len(readings)

    return total / number


def find_minimum(readings):
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    count = 0

    for reading in readings:
        result = classify_reading(
            reading, warning_limit, critical_limit
        )

        if result == category:
            count = count + 1

    return count


def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    warning_limit = 30
    critical_limit = 35

    number = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(
        readings, warning_limit, critical_limit, "NORMAL"
    )
    warning_count = count_category(
        readings, warning_limit, critical_limit, "WARNING"
    )
    critical_count = count_category(
        readings, warning_limit, critical_limit, "CRITICAL"
    )

    normal_percentage = normal_count / number * 100
    warning_percentage = warning_count / number * 100
    critical_percentage = critical_count / number * 100

    status = determine_overall_status(
        warning_count, critical_count
    )

    print("MONITORING SUMMARY")
    print("------------------")
    print("Number of readings  :", number)
    print("Total of readings   :", total)
    print("Average temperature : {:.2f} °C".format(average))
    print("Minimum temperature :", minimum, "°C")
    print("Maximum temperature :", maximum, "°C")

    print()
    print("NORMAL   : {} ({:.2f}%)".format(
        normal_count, normal_percentage
    ))
    print("WARNING  : {} ({:.2f}%)".format(
        warning_count, warning_percentage
    ))
    print("CRITICAL : {} ({:.2f}%)".format(
        critical_count, critical_percentage
    ))

    print("Overall Status:", status)


def main():
    readings = get_initial_readings()

    while True:
        print()
        display_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            display_readings(readings)

        elif choice == "2":
            add_reading(readings, 0, 100)

        elif choice == "3":
            display_classifications(readings, 30, 35)

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()