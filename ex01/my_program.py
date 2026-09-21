from path import Path


def main():
    try:
        dir = Path("enes")
        dir.mkdir_p()
        file = dir / "ates.txt"
        file.write_text("Hello, World!\n")
        print(file.read_text(), end="")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
