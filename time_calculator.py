def add_time(base: str, addon: str, dow: str = "") -> str:
    DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday")

    base_arr = base.split()
    base_hour, base_minute = map(int, base_arr[0].split(":"))
    meridiem = base_arr[1]

    addon_hour, addon_minute = map(int, addon.split(":"))
    addon_day = 0

    minutes = (base_minute + addon_minute) % 60

    total_hours = base_hour + addon_hour + (base_minute+addon_minute)//60

    hours = 12 if total_hours % 12 == 0 else total_hours % 12

    # if change meridiem
    if total_hours // 12 % 2 != 0:
        if meridiem == "AM":
            meridiem = "PM"
        else:
            addon_day += 1
            meridiem = "AM"

    addon_day += total_hours // 24
    if addon_day == 1:
        day = '(next day)'
    elif addon_day > 1:
        day = f"({addon_day} days later)"
    else:
        day = ""

    if dow:
        dow = ", " + DAYS_OF_WEEK[(DAYS_OF_WEEK.index(
            dow.capitalize()) + addon_day) % 7]

    return f"{hours}:{minutes:02} {meridiem}{dow} {day}".rstrip()


def main(args=None):
    print(add_time("3:00 PM", "3:10"))
    # Returns: 6:10 PM

    print(add_time("5:01 AM", "0:00") == '5:01 AM')
    # Returns: 5:01 AM

    print(add_time("11:30 AM", "2:32", "Monday"))
    # Returns: 2:02 PM, Monday

    print(add_time("11:43 AM", "00:20"))
    # Returns: 12:03 PM

    print(add_time("10:10 PM", "3:30"))
    # Returns: 1:40 AM (next day)

    print(add_time("11:43 PM", "24:20", "tueSday"))
    # Returns: 12:03 AM, Thursday (2 days later)

    print(add_time("6:30 PM", "205:12"))
    # Returns: 7:42 AM (9 days later)


if __name__ == '__main__':
    main()
