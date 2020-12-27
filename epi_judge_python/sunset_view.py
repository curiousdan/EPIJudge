from typing import Iterator, List

from test_framework import generic_test

#Given buildings of various height running east to west, 
# any building EAST of a building of equal or greater height cannot see the sunset
# Algo should process buildings East to West
# Algo returns buildings that CAN see the sunset.

# this is a sorting algorithm..

# 12/26/20
def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
	happy_buildings = []
	happy_index = []
	for i, evald in enumerate(sequence):
		while happy_buildings and happy_buildings[-1] <= evald:
			happy_buildings.pop()
			happy_index.pop()
		happy_buildings.append(evald)
		happy_index.append(i)

	return happy_index[::-1]

# The fundamental algo is identical
# a bit cleaner by using namedtuple rather than double stack. This is the more 
# effective approach.
import collections
def book_soln(seqeuence):
	HeightIndex = collections.namedtuple("HI", ('id', 'height'))
	stack: List[HeightIndex] = []
	for i, height in enumerate(seqeuence):
		while stack and height >= stack[-1].height:
			stack.pop()
		stack.append(HeightIndex(i,height))
	return [c.id for c in reversed(stack)]

def examine_buildings_with_sunset_wrapper(sequence):
	print("seq", sequence)
	return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
																																	examine_buildings_with_sunset))

