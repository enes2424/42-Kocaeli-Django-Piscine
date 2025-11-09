def main():
    file = open("periodic_table.txt", "r")
    outfile = open("periodic_table.html", "w")

    outfile.write("<!DOCTYPE html>\n")
    outfile.write('<html lang="en">\n')
    outfile.write("  <head>\n")
    outfile.write('    <meta charset="UTF-8" />\n')
    outfile.write(
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
    )
    outfile.write("    <title>Periodic Table</title>\n")
    outfile.write("  </head>\n")
    outfile.write("  <body>\n")
    outfile.write("    <table style='border-collapse: collapse;'>\n")

    elements = {}
    max_row = 0
    max_col = 0
    for line in file:
        parts = line.split("=")
        name = parts[0].strip()
        info = parts[1].strip().split(",")
        pos = info[0].split(":")[1].strip()
        number = info[1].split(":")[1].strip()
        symbol = info[2].split(":")[1].strip()
        molar = info[3].split(":")[1].strip()
        electron = info[4].split(":")[1].strip()
        row = len(electron.split(" "))
        if name == "Palladium":
            row = row + 1

        col = int(pos) + 1
        elements[(row, col)] = (name, number, symbol, molar, electron)

        max_row = max(max_row, row)
        max_col = max(max_col, col)

    for r in range(1, max_row + 1):
        outfile.write("      <tr>\n")
        for c in range(1, max_col + 1):
            if (r, c) in elements:
                name, number, symbol, molar, electron = elements[(r, c)]
                outfile.write(
                    "        <td style='border: 1px solid black; padding:10px'>\n"
                )
                outfile.write(f"          <h4>{name}</h4>\n")
                outfile.write("          <ul>\n")
                outfile.write(f"            <li>No {number}</li>\n")
                outfile.write(f"            <li>{symbol}</li>\n")
                outfile.write(f"            <li>{molar}</li>\n")
                outfile.write("          </ul>\n")
                outfile.write("        </td>\n")
            else:
                outfile.write("        <td></td>\n")
        outfile.write("      </tr>\n")

    outfile.write("    </table>\n")
    outfile.write("  </body>\n")
    outfile.write("</html>\n")

    file.close()
    outfile.close()


if __name__ == "__main__":
    main()
