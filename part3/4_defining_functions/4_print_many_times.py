# Write your solution here
def print_many_times(string, times):
    iterations = 0
    while iterations < times:
        print(string)
        iterations += 1
if __name__ == "__main__":
    print_many_times("python", 5)