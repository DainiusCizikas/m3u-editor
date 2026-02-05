import sys
import os
import glob

def get_file_or_folder():
    files = []
    for index, file_path in enumerate(sys.argv[1:]):
        if os.path.isdir(file_path):
            pattern = os.path.join(file_path, "*.m3u")
            found_files = glob.glob(pattern)
            if not found_files:
                print(f"No m3u files found in {file_path}")
            files.extend(found_files)
        elif file_path.endswith(".m3u"):
            files.append(file_path)
        else:
            print(f"Argument {index + 1} ('{file_path}')is not a .m3u")

    return files

def process_files(files):
    print(f"Processing {len(files)} file(s)")
    results = {}

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as playlist:
            original_list = playlist.read().splitlines() #reads the document
            stripped_list = []

            for line in original_list:
                stipped = line.strip()
                if stipped != "":
                    stripped_list.append(stipped)

            unique_list = list(set(stripped_list)) #removes duplicates
            sorted_list = (sorted(unique_list)) #sorts the list
            results[file_path] = sorted_list

    return results

def replace_files(results):
    print("Replacing files")
    for file_path, lines in results.items():
        temp = file_path + ".tmp"

        with open(temp, "w", encoding="utf-8") as playlist:
            playlist.write("\n".join(lines) + "\n")

        os.replace(temp, file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide m3u files or folder")
        exit()

    new_files = get_file_or_folder()
    if new_files:
        print(f"Found {len(new_files)} m3u files")
        new_results = process_files(new_files)
        replace_files(new_results)
        print("Done!")

    else:
        print("No m3u files found")