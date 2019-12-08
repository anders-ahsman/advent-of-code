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
    print(ones * twos)

if __name__ == '__main__':
    image = read_input()
    main(image)
