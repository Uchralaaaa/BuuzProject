import os

folder = r"C:\Users\tugsu\Downloads\iCloud Photos(2)\iCloud Photos"
files = sorted(os.listdir(folder))

count = 70
for f in files:
    if f.lower().endswith((".jpg", ".jpeg", ".png")):
        old_path = os.path.join(folder, f)
        new_name = f"buuz{count}.jpg"
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        count += 1

print("Renaming complete!")
