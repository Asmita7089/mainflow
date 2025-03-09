import re
from collections import Counter

def parse_logs(file_path):
    ip_counter = Counter()
    url_counter = Counter()
    response_counter = Counter()
    
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*\] "(?P<method>\w+) (?P<url>/\S*) HTTP/\d+\.\d+" (?P<status>\d+)')

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                match = log_pattern.match(line)
                if match:
                    data = match.groupdict()
                    ip_counter[data["ip"]] += 1
                    url_counter[data["url"]] += 1
                    response_counter[data["status"]] += 1

        return ip_counter, url_counter, response_counter
    

    except FileNotFoundError:
        print("\n Error: Log file not found. Please check the file path.")
        return None, None, None

def display_top_counts(counter, title, top_n=5):
    print(f"\n🔹 {title}")
    print("=" * 40)
    for item, count in counter.most_common(top_n):
        print(f"{item}: {count} times")
    print("=" * 40)

def save_summary_to_file(ip_counter, url_counter, response_counter):
    with open("log_summary.txt", "w") as file:
        file.write("🔹 Top 5 Frequent IP Addresses\n")
        file.write("=" * 40 + "\n")
        for item, count in ip_counter.most_common(5):
            file.write(f"{item}: {count} times\n")
        file.write("\n")

        file.write("🔹 Top 5 Accessed URLs\n")
        file.write("=" * 40 + "\n")
        for item, count in url_counter.most_common(5):
            file.write(f"{item}: {count} times\n")
        file.write("\n")

        file.write("🔹 Response Code Distribution\n")
        file.write("=" * 40 + "\n")
        for item, count in response_counter.most_common():
            file.write(f"{item}: {count} times\n")
    
    print("\n Log Summary has been saved to 'log_summary.txt' 📜.")

if __name__ == "__main__":
    log_file_path = "server.log"  

    ip_counts, url_counts, response_counts = parse_logs(log_file_path)

    if ip_counts:
        display_top_counts(ip_counts, "Top 5 Frequent IP Addresses")
        display_top_counts(url_counts, "Top 5 Accessed URLs")
        display_top_counts(response_counts, "Response Code Distribution")
        
        save_summary_to_file(ip_counts, url_counts, response_counts)
