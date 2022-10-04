import os

if __name__ == '__main__':
    print("loading env value...")
    MY_NAME = os.getenv("MY_NAME")
    print(MY_NAME)