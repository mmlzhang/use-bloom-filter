
import os

from code.pybloom import ScalableBloomFilter

bloom_file_path = ".bloom_filter"


def get_bloom(bloom_file_path):
    if os.path.exists(bloom_file_path):
        with open(bloom_file_path, "rb") as f1:
            bloom = ScalableBloomFilter.fromfile(f1)
    else:
        bloom = ScalableBloomFilter(initial_capacity=1024, error_rate=1 / 10000 / 1000)
    return bloom


def save_bloom_to_file(bloom_file_path, bloom):
    with open(bloom_file_path, "wb") as f:
        bloom.tofile(f)


def main():
    bloom = get_bloom(bloom_file_path)

    test_data = [1, 1, 2, 3, 4, 5, 5]
    result = [bloom.add(d) for d in test_data]
    print(result)


if __name__ == '__main__':
    main()
