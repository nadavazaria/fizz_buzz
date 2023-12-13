import icecream




def main():
    for i in range(0,100):
        if i%15==0:
            icecream.ic("fizzbuzz")
        elif i%5==0:
            icecream.ic("buzz")
        elif i%3==0:
            icecream.ic("fizz")
        else: icecream.ic(i)


if __name__ == "__main__":
    main()