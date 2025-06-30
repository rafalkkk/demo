import sys

def to_upper(text: str) -> str:
    return text.upper()

if __name__ == "__main__":
    print(to_upper(sys.argv[1]))