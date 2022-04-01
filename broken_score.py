def main():
    score = float(input("Enter score: "))
    generate_results(score)


def generate_results(score):
    if 0 <= score <= 100:
        if score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else:
            print("Bad")
    else:
        print("Invalid score!")


if __name__ == '__main__':
    main()
