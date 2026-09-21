import sys, antigravity

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 geohashing.py <latitude> <longitude> <datedow>")
        sys.exit(1)

    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
    except ValueError:
        print("Error: Invalid arguments. Latitude and longitude must be numbers.")
        sys.exit(1)

    try:
        datedow = sys.argv[3].encode("utf-8")
        antigravity.geohash(latitude, longitude, datedow)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
