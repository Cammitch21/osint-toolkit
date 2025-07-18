# OSINT TOOLKIT

Welcome to my OSINT Toolkit, a collection of Python tools for ethical open-source intelligence gathering.

# Disclaimer

The tools in this OSINT Toolkit are only for educational and ethical use. Tools in this kit are only to be used if you have explicit permission from the user/website. I am not responsible for any misuse or harm caused by using the toolkit.

# Usage
To use the tools in this toolkit
- Install requirements.txt
- Run main.py
- Select which tool you would like to use
- Follow the tools instuctions

## Navigation

- [DNS Lookup](#dns-lookup-tool)
- [Username Lookup](#username-lookup-tool)

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

# Username Lookup Tool

## Features

Allows you to quickly search multiple websites to find a username.
 - Checks each website in the list.
 - If the website returns status 200 it is added to the final list.
 - If then website returns any other status it will not be added to the final list.



