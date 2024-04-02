import threading
import concurrent.futures
import requests
import os


"""1. დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. შედეგი დაბეჭდეთ ეკრანზე"""

# # with threading
# def print_even():
#     even_numbers = [str(i) for i in range(2, 51, 2)]
#     even_string = ', '.join(even_numbers)
#     print("Even thread:", even_string)

# def print_odd():
#     odd_numbers = [str(i) for i in range(1, 51, 2)]
#     odd_string = ', '.join(odd_numbers)
#     print("Odd thread:", odd_string)

# if __name__ == "__main__":
#     even_thread = threading.Thread(target=print_even)
#     odd_thread = threading.Thread(target=print_odd)

#     even_thread.start()
#     odd_thread.start()

#     even_thread.join()
#     odd_thread.join()

#     print("Both threads have finished.")




# # with concurrent.futures
# def print_even():
#     even_numbers = [str(i) for i in range(2, 51, 2)]
#     even_string = ', '.join(even_numbers)
#     print("Even thread:", even_string)

# def print_odd():
#     odd_numbers = [str(i) for i in range(1, 51, 2)]
#     odd_string = ', '.join(odd_numbers)
#     print("Odd thread:", odd_string)

# if __name__ == "__main__":
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         executor.submit(print_even)
#         executor.submit(print_odd)

#     print("Both threads have finished.")



"""2. დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან."""

# # with threading
# MP3 file_ების გადმოსაწერი ფუნქცია:
# def download_mp3(url, filename):
#     try:
#         response = requests.get(url, stream=True)
#         if response.status_code == 200:
#             with open(filename, 'wb') as f:
#                 for chunk in response.iter_content(chunk_size=1024):
#                     f.write(chunk)
#             print(f"Downloaded: {filename}")
#         else:
#             print(f"Failed to download: {filename} - HTTP Error {response.status_code}")
#     except Exception as e:
#         print(f"Error downloading {filename}: {str(e)}")

# # URLs_ები MP3 ფაილებისთვის
# mp3_files = [
#     {"url": "https://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Sevish_-__nbsp_.mp3", "filename": "song1.mp3"},
#     {"url": "https://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/theme_01.mp3", "filename": "song2.mp3"},
#     {"url": "https://codeskulptor-demos.commondatastorage.googleapis.com/descent/background%20music.mp3", "filename": "song3.mp3"},
# ]

# # დირექტორიის შექმნა ფაილების შესანახად
# if not os.path.exists("downloads"):
#     os.makedirs("downloads")

# # თითოეული გადმოწერისთვის Thread_ის შექმნა
# threads = []
# for file in mp3_files:
#     thread = threading.Thread(target=download_mp3, args=(file["url"], os.path.join("downloads", file["filename"])))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print("All downloads completed.")



# with concurrent.futures
# MP3 file_ების გადმოსაწერი ფუნქცია:
# def download_mp3(url, filename):
#     try:
#         response = requests.get(url, stream=True)
#         if response.status_code == 200:
#             with open(filename, 'wb') as f:
#                 for chunk in response.iter_content(chunk_size=1024):
#                     f.write(chunk)
#             print(f"Downloaded: {filename}")
#         else:
#             print(f"Failed to download: {filename} - HTTP Error {response.status_code}")
#     except Exception as e:
#         print(f"Error downloading {filename}: {str(e)}")

# # URLs_ები MP3 ფაილებისთვის
# mp3_files = [
#     {"url": "https://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Sevish_-__nbsp_.mp3", "filename": "song1.mp3"},
#     {"url": "https://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/theme_01.mp3", "filename": "song2.mp3"},
#     {"url": "https://codeskulptor-demos.commondatastorage.googleapis.com/descent/background%20music.mp3", "filename": "song3.mp3"},
# ]

# # დირექტორიის შექმნა ფაილების შესანახად
# if not os.path.exists("downloads"):
#     os.makedirs("downloads")

# # ფაილების ერთდროული გადმოწერა
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = [executor.submit(download_mp3, file["url"], os.path.join("downloads", file["filename"])) for file in mp3_files]
#     concurrent.futures.wait(futures)

# print("All downloads completed.")