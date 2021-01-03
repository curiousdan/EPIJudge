from test_framework import generic_test
from test_framework.test_failure import TestFailure


# given stacks, implement queue
class Queue:
	def __init__(self):
		self.instack = []
		self.outstack = []
		
	def enqueue(self, x: int) -> None:
		if not self.instack:
			self.transfer(self.outstack, self.instack)
		
		self.instack.append(x)

	def dequeue(self) -> int:
		if not self.outstack:
			self.transfer(self.instack, self.outstack)
		return self.outstack.pop()
		
	def transfer(self, donor, recepient):
		while donor:
			recepient.append(donor.pop())

# Book insight: you don't need to flip at every eoperation switch.
class Book:
	def __init__(self):
		self.enq = []
		self.deq = []
		
	self.enqueue(self, x):
		self.enq.append(x)
		
	self.dequeue(self):
		if not self.deq:
			while self.enq:
				self.deq.append(self.enq.pop())
		return self.deq.pop()

def queue_tester(ops):
	try:
		q = Queue()

		for (op, arg) in ops:
			if op == 'Queue':
				q = Queue()
			elif op == 'enqueue':
				q.enqueue(arg)
			elif op == 'dequeue':
				result = q.dequeue()
				if result != arg:
					raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
																							str(result))
			else:
				raise RuntimeError('Unsupported queue operation: ' + op)
	except IndexError:
		raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('queue_from_stacks.py',
																																	'queue_from_stacks.tsv', queue_tester))

