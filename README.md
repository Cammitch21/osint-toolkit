# DNS Lookup Tool

A simple Python script to query DNS records (A, AAAA, MX, NS, TXT, CNAME) for a given domain.

## Features

- Queries the following DNS record types:
  - A (IPv4)
  - AAAA (IPv6)
  - MX (Mail Exchange)
  - NS (Name Servers)
  - TXT (Text Records)
  - CNAME (Aliases)
- Uses a visual loading bar with `tqdm` for better UX
- Handles common DNS errors (e.g. missing records or timeouts)

## Usage

Install requirements.txt

Then run:

```bash
py dns_lookup.py
```
Enter a domain when you are prompted

The tools in this OSINT Toolkit are only for educational and ethical use. 
The DNS Lookup tool is only to be run on websites that you own or have gotten explicit permission from.
