from pathlib import Path


p = Path(r'C:\Users\Thomas Mercer\AppData\Roaming\com.audient.iD')

print(Path(p).is_dir())
print(p)

for file in Path(p).iterdir():
    print(file)
    Path.unlink(file)