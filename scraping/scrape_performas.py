import requests
import re
import json
import bs4
import threading
from db_handler import conn
from db_handler import store_opening_data
from db_handler import is_id_present
num_threads = 4

def get_performas_data(text):
    pattern = r'<script id="__NEXT_DATA__" type="application/json" crossorigin="">(.*?)</script>'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        json_string = match.group(1).strip()
        json_string = json_string.replace('\\\'', '\'')
        json_string = re.sub(r'\\x([0-9A-Fa-f]{2})', lambda match: chr(int(match.group(1), 16)), json_string) 
        try:
            parsed_json = json.loads(json_string)
        except json.JSONDecodeError:
            print("Invalid JSON:")
            print(json_string)
        return parsed_json
    return None

def split_into_chunks(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    if len(chunks) > num_chunks:
        chunks[-2].extend(chunks[-1])
        chunks.pop()
    return chunks

def scrape_performa_details(data_chunk, index):
    print(f"Thread {index} started")
    f = open(f"log_thread_{index}.txt", 'w')
    for ii, item in enumerate(data_chunk):
        url = f"https://spo-backend.vercel.app/details/2024/{item['ID']}"
        if is_id_present(item['ID']):
            print(f"Thread {index} already scraped ID {item['ID']}")
            continue
        response = requests.get(url, headers={'Priority': 'u=0, i','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0', 'Referer': 'https://spo-backend.vercel.app/2024'})
        if response.status_code != 200:
            f.write(f"Failed to scrape ID: {item['ID']}\n")
            print(f"Thread {index} failed to scrape ID {item['ID']}")
            continue
        # print(response.text)
        data = get_performas_data(response.text)
        if data:
            main_data = data['props']['pageProps']['data']
            stored = store_opening_data(item['ID'], main_data, item)
            if not stored:
                f.write(f"Failed to scrape ID: {item['ID']}\n")
                print(f"Thread {index} failed to store ID {item['ID']}")
                continue
        else:
            f.write(f"Failed to scrape ID: {item['ID']}\n")
            print(f"Thread {index} failed to scrape ID {item['ID']}")
        # print(response.text)
        print(f"Thread {index} scraped ID {item['ID']}, index {ii}")

    f.close()
    print(f"Thread {index} finished, {len(data_chunk)} items processed")

def main():
    data = json.load(open('data/performas_data.json'))
    data = data
    chunks = split_into_chunks(data, num_threads)
    threads = []
    for i in range(num_threads):
        # thread = threading.Thread(target=scrape_performa_details, args=(chunks[i], i))
        scrape_performa_details(chunks[i], i)
        # thread.start()
        # threads.append(thread)
    # for thread in threads:
    #     thread.join()
    print("All threads finished")
    
if __name__ == '__main__':
    main()
    conn.close()