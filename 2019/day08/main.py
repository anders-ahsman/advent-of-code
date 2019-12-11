import sys

def read_input():
    image = next(sys.stdin)
    return image

def main(image):
    layers = []
    pos = 0

    cols = 25
    rows = 6
    try:
        while True:
            layer = []
            for _ in range(rows):
                for _ in range(cols):
                    layer.append(int(image[pos]))
                    pos += 1
            layers.append(layer)
    except IndexError:
        pass

    print(f'checksum: {calc_checksum(layers)}')

    render(layers, rows, cols)

def calc_checksum(layers):
    max_zeros_idx = None
    min_zeros = None
    for idx, layer in enumerate(layers):
        zeros = sum([1 for x in layer if x == 0])
        if not min_zeros or zeros < min_zeros:
            min_zeros =  zeros
            max_zeros_idx = idx

    layer = layers[max_zeros_idx]
    ones = sum([1 for x in layer if x == 1])
    twos = sum([1 for x in layer if x == 2])
    return ones * twos

def render(layers, rows, cols):
    rendered = []
    for _ in range(rows):
        rendered.append([2] * cols)

    for layer in layers:
        for row_idx, row in enumerate(range(rows)):
            for col in range(cols):
                if rendered[row][col] == 2:
                    rendered[row][col] = layer[row_idx * cols + col]

    for row in rendered:
        for char in row:
            print(char, end='')
        print()

if __name__ == '__main__':
    image = read_input()
    main(image)
