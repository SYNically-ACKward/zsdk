"""
Bulk URL Lookup Example

This script demonstrates how to perform bulk URL lookups using the ZSDK.
This example looks up the URLs associated with Microsoft PowerBI Desktop
    found here: https://tinyurl.com/power-automate-desktop

Prerequisites:
- Install ZSDK using pip (`pip install zsdk`)
- Obtain API key from your Zscaler ZIA management portal

Overview:
1. Set up SDK with API key and credentials and instantiate as `tenant`
2. Read URLs from input file `urls.txt`
3. Perform bulk lookup.
4. Write results to output file `output.txt`
"""
from zsdk.zia import ZIA as zscaler

tenant = zscaler("username@example.com", "P@ssw0rd", "your_api_key", "your_cloud_name")

with open("urls.txt", "r") as f:
    data = f.readlines()
    urls = [line.strip() for line in data]


def bulk_lookup(urls):
    data = tenant.url_categories.lookup(urls)
    if len(data) <= 100:
        with open("output.txt", "w") as f:
            for url in data:
                application_str = (
                    ", ".join(url["application"])
                    if isinstance(url.get("application"), list)
                    else url.get("application", "None")
                )
                output_str = (
                    f"URL: {url.get('url')}\n"
                    f"    Categorization: {', '.join(cat for cat in url.get('urlClassifications'))}\n"
                    f"    Pre-defined Applications: {application_str}\n"
                )
                f.write(output_str + "\n")
    else:
        print("Too many URLs entered. Please try again with 100 max.")


bulk_lookup(urls)
