from bitarray import bitarray
from hashlib import md5, sha256, sha512


class BloomFilter:
    def __init__(self, size) -> None:
        self.hash_funcs = [md5, sha256, sha512]
        self.size = size
        self.bit_arr = bitarray(size)
        self.bit_arr[:] = 0

    def add(self, data) -> None:
        for i in self._cal(data):
            self.bit_arr[i] = 1

    def _cal(self, data: str) -> list:
        return [
            int(hash_f(data.encode("ascii")).hexdigest(), 16) % self.size
            for hash_f in self.hash_funcs
        ]

    def is_data_exists(self, data) -> bool:
        res = [self.bit_arr[i] for i in self._cal(data)]
        if len(res) * [int(True)] == res:
            return True
        return False


if __name__ == "__main__":
    bf = BloomFilter(10)
    bf.add("123")
    bf.add("456")
    print(bf.is_data_exists("456"))
    print(bf.is_data_exists("789"))
