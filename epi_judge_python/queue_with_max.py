from test_framework import generic_test
from test_framework.test_failure import TestFailure

# 1/3/21
# max operation doesn't remove the elemtn
# you can use another a data structure other than a queue
class QueueWithMax:
	def __init__(self):
		self.q = []
		self.maxs = []
		
	def enqueue(self, x: int) -> None:
		while self.maxs and self.maxs[-1] < x:
			self.maxs.pop()
		self.q.append(x)
		self.maxs.append(x)

	def dequeue(self) -> int:
		# check for notempty
		if self.q[0] == self.maxs[0]:
			self.maxs.pop(0)

		return self.q.pop(0)

	def max(self) -> int:
		# check notempty
		return self.maxs[0]

# wtf use stacks
class AltSolution:
	def __init__(self):
		# THESE ARE STACKS
		self.enq = []
		self.deq = []
		
	def enqueue(self, x):
		self.enq.append(x)
		
	def dequeue(self):
		if not self.deq:
			while self.enq:
				self.deq.append(self.enq.pop())
		return self.deq.pop()
	
	def max(self):
		# this feels like cheating just to use the max method lol
		if self.enq:
			return max(self.enq) if not self.deq else max(max(self.enq),max(self.deq))
		return max(self.deq)

def queue_tester(ops):

	try:
		q = QueueWithMax()

		for (op, arg) in ops:
			if op == 'QueueWithMax':
				q = QueueWithMax()
			elif op == 'enqueue':
				q.enqueue(arg)
			elif op == 'dequeue':
				result = q.dequeue()
				if result != arg:
					raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
																							str(result))
			elif op == 'max':
				result = q.max()
				if result != arg:
					raise TestFailure('Max: expected ' + str(arg) + ', got ' + str(result))
			else:
				raise RuntimeError('Unsupported queue operation: ' + op)
	except IndexError:
		raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('queue_with_max.py', 'queue_with_max.tsv',
																																	queue_tester))

