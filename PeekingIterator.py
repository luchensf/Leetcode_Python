class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.haspeeked = False


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.haspeeked:
            self.n = self.iterator.next()
        self.haspeeked = True
        return self.n

    def next(self):
        """
        :rtype: int
        """
        if not self.haspeeked:
            return self.iterator.next()
        self.haspeeked = False
        return self.n

    def hasNext(self):
        """
        :rtype: bool
        """

        return self.haspeeked or self.iterator.hasNext()


# class PeekingIterator:
#     def __init__(self, iterator):
#         """
#         Initialize your data structure here.
#         :type iterator: Iterator
#         """
#         self.iterator = iterator
#         self.helper()
#
#     def peek(self):
#         """
#         Returns the next element in the iteration without advancing the iterator.
#         :rtype: int
#         """
#         return self.n
#
#     def next(self):
#         """
#         :rtype: int
#         """
#         val = self.n
#         self.helper()
#         return val
#
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.hasnext
#
#     def helper(self):
#         self.hasnext = self.iterator.hasNext()
#         if self.hasnext:
#             self.n = self.iterator.next()
