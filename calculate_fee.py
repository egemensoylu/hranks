def calculate_fee(lines):
    line1 = lines[0].split(' ')
    line2 = lines[1].split(' ')

    day, month, year = map(int, line1)
    returnDate = datetime.date(year, month, day)

    day, month, year = map(int, line2)
    dueDate = datetime.date(year, month, day)

    delta = returnDate - dueDate
    print(delta)

    if returnDate.year - dueDate.year > 0:
        return 10000
    elif delta.days <= 0:
        return 0
    elif 0 < delta.days <= 31:
        return 15 * delta.days
    elif 31 < delta.days < 365:
        return 500 * ( returnDate.month - dueDate.month)



