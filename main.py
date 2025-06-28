import sys
from modules import dns_lookup
from modules import username_lookup

def dns_lookup_interface():
    domain = input("Enter the Domain to lookup: ").strip()
    records = dns_lookup.get_dns_records(domain)
    print(f"\nDNS records found for {domain}:\n")
    for rtype, values in records.items():
        print(f"{rtype}:")
        if values:
            for v in values:
                print(f"  -  {v}")
        else:
            print("No records found.")   

def username_lookup_interface():
    username = input("Enter Username to check: ").strip()
    results = username_lookup.check_username(username)
    # Printing the list
    print(f"\n Results found for '{username}':\n")
    for site, url in results.items():
        if url:
            print(f"{site}: {url}")
        else:
            print(f"{site}: Not Found")

def main():
    options = {
        "1": ("DNS Lookup", dns_lookup_interface),
        "2": ("Username Lookup", username_lookup_interface),
        "0": ("Exit", None)
    }

    while True:
        print("\nOSINT Toolkit")
        for key, (desc, _) in options.items():
            print(f"{key}.{desc}")

        choice = input("Select an option: ").strip()

        if choice == "0":
            sys.exit(0)
        elif choice in options:
            _, func = options[choice]
            func()
        else:
            print("Invalid Selection")

if __name__ in "__main__":
    main()