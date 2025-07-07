import threading

def download_file(file_id):
    print(f"Downloading file {file_id}...")
    # Simulate time delay
    import time; time.sleep(2)
    print(f"File {file_id} downloaded.")

# Create threads
t1 = threading.Thread(target=download_file, args=(1,))
t2 = threading.Thread(target=download_file, args=(2,))

# Start them
t1.start()
t2.start()

# Wait for them to finish
t1.join()
t2.join()

print("All downloads complete!")
