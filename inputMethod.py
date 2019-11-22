from sys import stdin, stdout

def main():
    n = stdin.readline()

    arr = [int(x) for x in stdin.readline().split()]
    summation = 0
    for x in arr:
        summation += x

    stdout.write(str(summation))

if __name__ == "__main__":
    main()
