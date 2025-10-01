import os

# Original folder
folder1 = r"C:\Users\user\Desktop\suresh\Python_Lib"
# Temp folder
folder2 = r"C:\Users\user\Desktop\suresh\Python_Lib_temp"

def list_files(base):
    files_set = set()
    for root, dirs, files in os.walk(base):
        for f in files:
            # relative path from base folder
            rel_path = os.path.relpath(os.path.join(root, f), base)
            files_set.add(rel_path)
    return files_set

files1 = list_files(folder1)
files2 = list_files(folder2)

missing_in_temp = files1 - files2
missing_in_original = files2 - files1

print("Files missing in temp folder:")
for f in sorted(missing_in_temp):
    print(f)

print("\nFiles missing in original folder:")
for f in sorted(missing_in_original):
    print(f)

print(f"\nTotal missing in temp: {len(missing_in_temp)}")
print(f"Total missing in original: {len(missing_in_original)}")
