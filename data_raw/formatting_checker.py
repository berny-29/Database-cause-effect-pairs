import os
import re
import glob

def validate_tubingen_format(folder_path):
    """
    Validates all text files in a folder for proper Tubingen format.
    
    Acceptable formats:
    - Two numbers separated by space: "-10.1 26.4"
    - Single number: "6.4"
    - Single number with leading space: " 6.8"
    
    Args:
        folder_path (str): Path to the folder containing text files
    """
    
    # Regular expression pattern for valid Tubingen format
    # Matches: optional whitespace + number + optional (whitespace + number) + optional whitespace
    pattern = r'^\s*[+-]?\d+(?:\.\d+)?(?:\s+[+-]?\d+(?:\.\d+)?)?\s*$'
    
    # Get all text files in the folder
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    
    if not txt_files:
        print(f"No .txt files found in {folder_path}")
        return
    
    print(f"Checking {len(txt_files)} text files in {folder_path}")
    print("=" * 50)
    
    total_errors = 0
    files_with_errors = 0
    
    for file_path in sorted(txt_files):
        file_name = os.path.basename(file_path)
        file_errors = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    # Remove newline character for checking
                    line_content = line.rstrip('\n\r')
                    
                    # Skip completely empty lines (optional - remove this if empty lines should be flagged)
                    if line_content.strip() == '':
                        print(f"ERROR: {file_name} - Line {line_num}: Empty line")
                        file_errors += 1
                        continue
                    
                    # Check if line matches the pattern
                    if not re.match(pattern, line_content):
                        print(f"ERROR: {file_name} - Line {line_num}: Invalid format: '{line_content}'")
                        file_errors += 1
        
        except Exception as e:
            print(f"ERROR: Could not read {file_name}: {e}")
            file_errors += 1
        
        if file_errors > 0:
            files_with_errors += 1
            total_errors += file_errors
    
    print("=" * 50)
    print(f"Validation complete!")
    print(f"Files checked: {len(txt_files)}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total errors found: {total_errors}")
    
    if total_errors == 0:
        print("[OK] All files are properly formatted!")
    else:
        print("[ERROR] Formatting issues found - see details above")

def validate_single_file(file_path):
    """
    Validates a single text file for proper Tubingen format.
    
    Args:
        file_path (str): Path to the text file
    """
    pattern = r'^\s*[+-]?\d+(?:\.\d+)?(?:\s+[+-]?\d+(?:\.\d+)?)?\s*$'
    
    file_name = os.path.basename(file_path)
    errors = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line_content = line.rstrip('\n\r')
                
                # Check empty lines
                if line_content.strip() == '':
                    print(f"ERROR: {file_name} - Line {line_num}: Empty line")
                    errors += 1
                    continue
                
                # Check format
                if not re.match(pattern, line_content):
                    print(f"ERROR: {file_name} - Line {line_num}: Invalid format: '{line_content}'")
                    errors += 1
    
    except Exception as e:
        print(f"ERROR: Could not read {file_name}: {e}")
        errors += 1
    
    if errors == 0:
        print(f"[OK] {file_name} is properly formatted!")
    else:
        print(f"[ERROR] {file_name} has {errors} formatting issues")
    
    return errors

# Example usage
if __name__ == "__main__":
    # Option 1: Validate all files in a folder
    #folder_path = input("Enter the path to your folder containing the 105 data pairs: ").strip()
    folder_path = r"C:\Users\Samuel\Desktop\Uni_Wien\Semester_2\Praktikum\Datasets\USGS_final\ALL_WITH_MISSING"
    
    if os.path.exists(folder_path):
        validate_tubingen_format(folder_path)
    else:
        print(f"Error: Folder '{folder_path}' does not exist!")
    
    # Option 2: Uncomment below to validate a specific file
    # file_path = "path/to/your/specific/file.txt"
    # validate_single_file(file_path)