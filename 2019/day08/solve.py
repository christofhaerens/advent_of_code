#!/usr/bin/python3

import re
from collections import defaultdict, Counter

day = "--- Day 8 - 2019 ---"
BLACK = '0'
WHITE = '1'
TRANSPARANT = '2'


class Image(object):

    def __init__(self, data, width, height):
        self.data = data
        self.data_size = len(data)
        self.w = width
        self.h = height
        self.image_size = width * height
        self.layers = []
        self.pixels = []
        self.process_data()
        self.process_layers()

    def process_data(self):
        if self.data_size % self.image_size != 0:
            raise RuntimeError('Error: invalid data size (%d, %d)' % (self.image_size, self.data_size))
        for i in range(0, self.data_size, self.image_size):
            self.layers.append(self.data[i:i + self.image_size])

    def process_layers(self):
        self.pixels = self.layers[0]
        for layer in self.layers[1:]:
            c = ''
            for idx, p in enumerate(layer):
                c += p if self.pixels[idx] == TRANSPARANT else self.pixels[idx]
            self.pixels = c.replace(BLACK, ' ').replace(WHITE, '█')

    def layer_with_lowest(self, value):
        lowest = -1
        lowest_idx = -1
        counters = [Counter(d) for d in self.layers]
        for idx, layer in enumerate(counters):
            count = counters[idx][value]
            lowest, lowest_idx = (count, idx) if lowest == -1 or count < lowest else (lowest, lowest_idx)
        return counters[lowest_idx]['1'] * counters[lowest_idx]['2']

    def render(self):
        rendered = []
        for i in range(0, self.image_size, self.w):
            rendered.append(self.pixels[i:i + self.w])
        return '\n'.join(rendered)


def solve1(data):
    img = Image(data, 25, 6)
    return img.layer_with_lowest('0')


def solve2(data):
    img = Image(data, 25, 6)
    return img.render()


def solve(data):
    a1, a2 = (0, 0)
    print("\n%s" % day)
    a1 = solve1(data)
    print("part1 = %r" % a1)
    a2 = solve2(data)
    print("part2 = \n%s" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test.txt', 'r')
    input = [line.strip() for line in fh]
    fh.close()
    data = ''.join(input)
    solve(data)


if __name__ == '__main__':
    main()
