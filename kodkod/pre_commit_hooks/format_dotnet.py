import glob
import os
import subprocess


def main():
    # Find all .sln files
    sln_files = glob.glob("**/*.sln", recursive=True)
    # Check if the list is empty
    if not sln_files:
        print("Error: No .sln files found.")
        return 1

    # Process each .sln file
    for sln_file in sln_files:
        # Get the directory of the .sln file
        sln_directory = os.path.dirname(sln_file)

        # Print the directory being processed (for visibility)
        print(f"Processing .sln in {sln_directory}")

        # Execute dotnet format in the directory of the .sln file
        subprocess.run(["dotnet", "format"], cwd=sln_directory)

    return 0


if __name__ == "__main__":
    exit(main())
