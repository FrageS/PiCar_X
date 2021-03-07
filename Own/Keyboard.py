import sys, termios, tty, os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
  while True:
    char = getch()

    if (char == "q"):
        print("q pressed")  

    if (char == "a"):
        print("a pressed")

    if (char == "d"):
        print("d pressed")         

    elif (char == "w"):
        print("w pressed")

    elif (char == "s"):
        print("s pressed")

if __name__ == "__main__":
    try:
      main()
    except:      
      print('Program cancelled')