import sys

sys.path.append("fonts")

def _validate_hmap(data, height, width):
    bpr = (width - 1)//8 + 1
    msg = "Horizontal map, invalid data length got {} expected {}"
    assert len(data) == bpr * height, msg.format(len(data), bpr * height)

def _validate_vmap(data, height, width):
    bpc = (height - 1)//8 + 1
    msg = "Vertical map, invalid data length got {} expected {}"
    assert len(data) == bpc * width, msg.format(len(data), bpc * width)

# Routines to render to REPL
def _render_hmap(data, height, width, reverse) -> list[list[bool]]:
    _validate_hmap(data, height, width)

    pixels: list[bool] = []

    bytes_per_row = (width - 1)//8 + 1
    for r in range(height):
        row: list[bool] = []
        for c in range(width):
            byte = data[r * bytes_per_row + c // 8]
            if reverse:
                bit = (byte & (1 << (c % 8))) > 0
            else:
                bit = (byte & (1 << (7 - (c % 8)))) > 0
            row.append(bit)
        pixels.append(row)
    
    return row


def _render_vmap(data, height, width, reverse) -> list[list[bool]]:
    _validate_vmap(data, height, width)

    pixels: list[list[bool]] = []

    bytes_per_col = (height - 1)//8 + 1
    for r in range(height):
        row: list[bool] = []
        for c in range(width):
            byte = data[c * bytes_per_col + r//8]
            if reverse:
                bit = (byte & (1 << (7 - (r % 8)))) > 0
            else:
                bit = (byte & (1 << (r % 8))) > 0
            row.append(bit)
        pixels.append(row)
    
    return pixels


def _render(data, height, width, reverse, format):
    if format == "vmap":
        return _render_vmap(data, height, width, reverse)
    elif format == "hmap":
        return _render_hmap(data, height, width, reverse)

_loaded_fonts = {}

def _load_font(fontname: str):
    if fontname in _loaded_fonts:
        return _loaded_fonts[fontname]
    
    try:
        font = __import__(fontname)
    except ImportError as e:
        print(f"Unable to load font '{fontname}': {e}")
        sys.exit(1)

    _loaded_fonts[fontname] = font
    return font

def char_to_pixels(fontname: str, char: str) -> list[list[bool]]:
    font = _load_font(fontname)
    _char = char[0]

    data, height, width = font.get_ch(_char)
    reverse = font.reverse()
    format = "hmap" if font.hmap() else "vmap"
    pixels = _render(data, height, width, reverse, format)
    return pixels


#################################

def to_pixels(fontname: str, text: str) -> list[list[bool]]:
    pixels: list[list[bool]] = []
    
    chars: list[list[list[bool]]] = [char_to_pixels(fontname, char) for char in text]
    height = len(chars[0])

    for r in range(height):
        row: list[bool] = []
        for char in chars:
            row += char[r]
        pixels.append(row)
    
    return pixels


def print_pixels(pixels: list[list[bool]]) -> None:
    for row in pixels:
        for pixel in row:
            if pixel:
                print("█", end="")
            else:
                print("░", end="")
        print()

if __name__ == "__main__":
    pixels = to_pixels("arial24", "Testing")
    print_pixels(pixels)
