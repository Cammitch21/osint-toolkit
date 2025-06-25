import dns.resolver
from tqdm import tqdm

# Get the different record types (ipv4, ipv6, mail exchange, name servers, canonical names)
def get_dns_records(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME'] 
    results = {}

    print(f"\nLooking up DNS Records for {domain}:\n")

# Send a dns query with the record type
    for rtype in tqdm(record_types, desc="Checking DNS", unit='record', ncols=80):
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records = [] 
            
            # Store data into records
            for rdata in answers:
                if rtype == 'MX':
                    records.append(str(rdata.exchange))
                else:
                    records.append(str(rdata))

                results[rtype] = records
        except(dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoNameservers):
            results[rtype] = []
        except Exception as e:
            results[rtype] = [f"ERROR: {e}"]            
    return results

if __name__ == "__main__":
    domain = input("Enter the Domain to lookup: ").strip()
    records = get_dns_records(domain)
    print(f"\nDNS records found for {domain}:\n")
    for rtype, values in records.items():
        print(f"{rtype}:")
        if values:
            for v in values:
                print(f"  -  {v}")
        else:
            print("No records found.")       
        