from src.time_decorator import timeit
import os
@timeit
def save_summary_in_file(summary, filename):
    folder_path = "summaries"
    file_path = os.path.join(folder_path, filename)

    # Create the summaries folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Check if file exists, create if it doesn't
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            pass  # Create empty file

    # Write content to the file
    with open(file_path, 'w') as file:
        file.write(summary)

    print(f"Successfully wrote to {file_path}")