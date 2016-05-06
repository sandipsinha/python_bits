from datetime import date
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


if __name__ == "__main__":
    day, month, year = [int(x) for x in "20/03/1967".split("/")]
    born = date(year, month, day)
    print calculate_age(born)
