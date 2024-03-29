#Decorators

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")

def main():
    hello()
    

if __name__ == '__main__':
    main()