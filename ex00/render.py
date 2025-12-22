from settings import *
import sys, os, re

def render_template(template_file):
    with open(template_file, 'r') as file:
        content = file.read()

    for var, value in globals().items():
        content = re.sub(r"{\s*" + var + r"\s*}", str(value), content)

    output_file = template_file.replace(".template", ".html")
    with open(output_file, "w") as file:
        file.write(content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python render.py <template_file>")
        sys.exit(1)

    template_file = sys.argv[1]

    if not os.path.isfile(template_file):
        print(f"Error: File '{template_file}' not found.")
        sys.exit(1)

    if template_file.split(".")[-1] != "template":
        print("Error: Template file must have a .template extension.")
        sys.exit(1)

    try:
        render_template(template_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
