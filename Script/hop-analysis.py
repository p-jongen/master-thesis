import pandas as pd
import numpy as np

def process_traceroute_results(file_path):
def process_traceroute_results(file_path):
    df = pd.read_excel(file_path)

    for hop_number, group in df.groupby('hop'):
        ip_addresses = group['from'].drop_duplicates().dropna().tolist()

        percentile_10 = np.nanpercentile(group['rtt'], 10)

        print(f"Hop Number: {hop_number}")
        print(f"IP Addresses: {ip_addresses}")
        print(f"10th Percentile RTT: {percentile_10}\n")

file_path = ''
process_traceroute_results(file_path)