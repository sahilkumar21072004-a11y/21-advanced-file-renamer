import os

def rename_files(folder_path, prefix="", suffix="", replace_text=None,
                 new_text="", change_extension=None, dry_run=False):

    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("⚠ No files found in folder.")
        return

    print(f"\n📂 Processing {len(files)} files...\n")

    for index, filename in enumerate(files, start=1):

        name, extension = os.path.splitext(filename)

        # Replace text if needed
        if replace_text:
            name = name.replace(replace_text, new_text)

        # Change extension if needed
        if change_extension:
            extension = "." + change_extension.strip(".")

        new_name = f"{prefix}{name}_{index}{suffix}{extension}"

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        if dry_run:
            print(f"🔍 Preview: {filename} → {new_name}")
        else:
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {filename} → {new_name}")

    print("\n🎉 Operation Completed!\n")


# ==============================
# CLI Interface
# ==============================

if __name__ == "__main__":

    print("===== Advanced File Renamer PRO =====")

    folder = input("Enter folder path: ").strip()
    prefix = input("Enter prefix (optional): ").strip()
    suffix = input("Enter suffix (optional): ").strip()

    replace = input("Text to replace (leave blank if none): ").strip()
    new_text = ""
    if replace:
        new_text = input("Replace with: ").strip()

    change_ext = input("Change extension (e.g. txt, jpg) or leave blank: ").strip()

    dry = input("Dry run? (yes/no): ").strip().lower() == "yes"

    rename_files(
        folder_path=folder,
        prefix=prefix,
        suffix=suffix,
        replace_text=replace if replace else None,
        new_text=new_text,
        change_extension=change_ext if change_ext else None,
        dry_run=dry
    )