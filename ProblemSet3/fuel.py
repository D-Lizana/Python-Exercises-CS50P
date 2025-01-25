def main():
    result = convert(input("Fraction: "))
    print(gauge(result))


def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            z = x / y

            if z <= 1.0:
                return int(round(float(z) * 100))
            else:
                raise ValueError


        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if int(percentage) <= 1:
        return "E"
    elif int(percentage) > 1 and int(percentage) < 99:
        return f"{percentage}%"
    elif int(percentage) >= 99:
        return "F"


if __name__ == "__main__":
    main()