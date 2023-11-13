from random import randrange


class HashMapBase:
    def __init__(self, cap=11, p=109345121):
        # create an empty hash-table map
        self._table = cap * [None]
        self._n = 0  # number of entries in the map
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)
        self._items = []  # a list to store key-value pairs

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def __iter__(self):
        self._current_index = 0
        self._current_bucket = None
        self._current_bucket_index = 0
        return self

    def __next__(self):
        while self._current_index < len(self._table):
            if self._current_bucket is None or self._current_bucket_index >= len(self._current_bucket):
                self._current_bucket = self._table[self._current_index]
                self._current_bucket_index = 0
                self._current_index += 1
            else:
                key, value = self._current_bucket[self._current_bucket_index]
                self._current_bucket_index += 1
                return key, value

        raise StopIteration

    def items(self):
        for bucket in self._table:
            if bucket is not None:
                yield from bucket

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

    def _bucket_getitem(self, j, k):
        if self._table[j] is None:
            raise KeyError(f'Key not found: {k}')
        for key, value in self._table[j]:
            if key == k:
                return value
        else:
            raise KeyError(f'Key not found: {k}')

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = []
            # iterates over elements of list stored in hash table at specific index
        for index, (key, value) in enumerate(self._table[j]):
            if key == k:
                self._table[j][index] = (k, v)
                return
        self._table[j].append((k, v))
        self._n += 1

    def _bucket_delitem(self, j, k):
        # iterates over elements of list stored in hash table at specific index
        for index, (key, value) in enumerate(self._table[j]):
            if key == k:
                del self._table[j][index]
                return
        # if the key is not found
        raise KeyError(f'Key not found: {k}')
