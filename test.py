import os

input_folder = '/Users/santhiya/Documents/multimedia/DCIM/ila-619'
root = '/Users/santhiya/Documents/'

print(input_folder[len(root):])

os.makedirs("/Users/santhiya/Documents/multimedia/compressed/a/b/c/.mp3", exist_ok=True)

test = os.path.join("a/b/c/", "d.d")
print(test)