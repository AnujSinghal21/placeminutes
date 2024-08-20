import requests
import re
import json
import bs4
import threading

num_threads = 1

def split_into_chunks(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    if len(chunks) > num_chunks:
        chunks[-2].extend(chunks[-1])
        chunks.pop()
    return chunks

def scrape_performa_details(data_chunk, index):
    print(f"Thread {index} started")
    for item in data_chunk:
        url = f"https://spo-backend.vercel.app/details/2024/{item['ID']}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Thread {index} successfully scraped ID {item['ID']}")
        else:
            print(f"Thread {index} failed to scrape ID {item['ID']}")

    print(f"Thread {index} finished, {len(data_chunk)} items processed")

def main():
    data = json.load(open('data/performas_data.json'))
    data = data[0:1]
    chunks = split_into_chunks(data, num_threads)
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=scrape_performa_details, args=(chunks[i], i))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print("All threads finished")
    
if __name__ == '__main__':
    main()