#!/usr/bin/env fontforge

if len(sys.argv) < 3:
    print("Usage: ./scale.py <scaling_factor> <font_files>")
    print()
    print("Example: ./scale.py 1.2 myfont.ttf myotherfont.ttf")
    sys.exit(1)

try:
    scale_factor = float(sys.argv[1])
except ValueError:
    print("Error: Scaling factor must be a numeric value.")
    sys.exit(1)

suffix = "ScaledForEmacs"


def green(text):
    return "\033[92m" + text + "\033[0m"


for font_file in sys.argv[2:]:
    try:
        font = fontforge.open(font_file)

        font.selection.all()
        font.transform(psMat.scale(scale_factor))

        font.familyname += suffix

        new_font_path = font.fontname + suffix + ".ttf"
        font.generate(new_font_path)

        font.close()

        print(
            green(
                f"Font '{font_file}' scaled by {scale_factor} and saved as '{new_font_path}'."
            )
        )
    except Exception as e:
        print(f"Error processing '{font_file}': {e}")

print("All fonts processed successfully.")
