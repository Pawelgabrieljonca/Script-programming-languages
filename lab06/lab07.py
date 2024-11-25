import shutil
import os

# Helper function to prepare environment
def setup_environment():
    # Tworzenie folderów i plików testowych
    if not os.path.exists('source'):
        os.makedirs('source')
    with open('source/test_file.txt', 'w') as f:
        f.write('This is a test file.')

    if not os.path.exists('destination'):
        os.makedirs('destination')
    if os.path.exists('destination/test_file.txt'):
        os.remove('destination/test_file.txt')

# 1. Plik o danej nazwie nie istnieje w katalogu docelowym
def copy_file_no_conflict():
    print("1. Copying when the target file does not exist.")
    shutil.copy('source/test_file.txt', 'destination/test_file.txt')
    print("Copied successfully.\n")

# 2. Plik o podanej nazwie istnieje w katalogu docelowym
def copy_file_with_conflict():
    print("2. Copying when the target file exists.")
    with open('destination/test_file.txt', 'w') as f:
        f.write('Existing file content.')
    shutil.copy('source/test_file.txt', 'destination/test_file.txt')
    print("Copied successfully, overwriting the existing file.\n")

# 3. Katalog docelowy nie istnieje
def copy_file_nonexistent_directory():
    print("3. Copying when the destination directory does not exist.")
    non_existent_dir = 'non_existent_directory'
    if os.path.exists(non_existent_dir):
        shutil.rmtree(non_existent_dir)
    try:
        shutil.copy('source/test_file.txt', os.path.join(non_existent_dir, 'test_file.txt'))
    except FileNotFoundError as e:
        print(f"Error: {e}")
    print("Handled non-existent directory.\n")

# Main script
if __name__ == "__main__":
    setup_environment()

    # Wykonanie testów
    copy_file_no_conflict()
    copy_file_with_conflict()
    copy_file_nonexistent_directory()

    # Sprzątanie po testach
    shutil.rmtree('source')
    shutil.rmtree('destination')
    if os.path.exists('non_existent_directory'):
        shutil.rmtree('non_existent_directory')

    print("Tests completed.")
