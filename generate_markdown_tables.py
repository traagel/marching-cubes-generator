title = "|Configuration  | Complement     |"
row_break = "|-----------|----------|"


def generate_line(config):
    title = f"Configuration {config}       | Complement {255 - config}"
    line = f"|![Configuration: {config}](output/configuration{
        config
    }.png) | ![Configuration: {255 - config}](output/configuration{255 - config}.png)|)"
    return title, line


def generate_tables():
    for config in range(0, 128):
        title, line = generate_line(config)
        # print(title)
        # print(row_break)
        # print(line)
        # print("\n")
        with open("readme_gen.md", "a") as f:
            f.write(title + "\n")
            f.write(row_break + "\n")
            f.write(line + "\n")
            f.write("\n")
