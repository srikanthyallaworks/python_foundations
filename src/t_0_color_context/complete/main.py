from color import Color
from color_context import ColorContext

def main():
    print("\nBefore")
    with ColorContext(Color.Green):
        print("During")
    print("After\n")


if __name__ == '__main__':
    main()
