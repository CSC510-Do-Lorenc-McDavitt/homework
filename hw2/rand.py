"""
File that includes a function to creates a
random array using a Unix subprocess function.
"""
import subprocess


def random_array(arr):
    "Creates a random array using a Unix subprocess function."
    shuffled_num = None
    for index, _value in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[index] = int(shuffled_num.stdout)
    return arr
