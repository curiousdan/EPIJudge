from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
	def __init__(self, capacity: int) -> None:
		#print(capacity)
		self.cap = capacity
		self.q = [None]*capacity
		self.i = self.cnt = 0
		self.e = -1
		return

	def enqueue(self, x: int) -> None:
		#print("enq", self.q)
		if self.cap == self.cnt:
			self.resize()
			
		self.e = (self.e + 1)%self.cap
		self.q[self.e] = x
		self.cnt += 1

	def dequeue(self) -> int:
		#print("deq", self.q)
		if not self.cnt:
			raise RuntimeError("AAAAA")
		
		ret = self.q[self.i]
		self.i = (self.i + 1)%self.cap
		self.cnt -=1

		return ret

	def size(self) -> int:
		return self.cnt
		
	def resize(self):
		#print("resize")
		new = self.q[self.i:]
		if self.e < self.i:
			new += self.q[:self.e+1]
		new += [None] *self.cap
		self.q = new.copy()
		self.cap *= 2
		self.i = 0
		self.e = self.cnt - 1
		
		#print("resized q:", self.q)
		
		
class QueueBookSoln:

    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:

        self._entries = [0] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x: int) -> None:

        if self._num_queue_elements == len(self._entries):  # Needs to resize.
            # Makes the queue elements appear consecutively.
            self._entries = (self._entries[self._head:] +
                             self._entries[:self._head])
            # Resets head and tail.
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [0] * (len(self._entries) * Queue.SCALE_FACTOR -
                                    len(self._entries))

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self) -> int:

        self._num_queue_elements -= 1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return result

    def size(self) -> int:

        return self._num_queue_elements
		


def queue_tester(ops):
	q = Queue(1)

	for (op, arg) in ops:
		if op == 'Queue':
			q = Queue(arg)
		elif op == 'enqueue':
			q.enqueue(arg)
		elif op == 'dequeue':
			result = q.dequeue()
			if result != arg:
				raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' + str(result))
		elif op == 'size':
			result = q.size()
			if result != arg:
				raise TestFailure('Size: expected ' + str(arg) + ', got ' + str(result))
		else:
			raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('circular_queue.py', 'circular_queue.tsv',
																																	queue_tester))

