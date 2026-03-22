import os
import re

files_to_fix = [
    "index.md",
    "google-ads.md",
    "meta-ads.md",
    "zoho-crm.md",
    "ga4-gtm.md",
    "revenue-system.md",
    "about.md",
    "contact.md",
]

for file in files_to_fix:
    if not os.path.exists(file):
        continue
    
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix double borders in cards which broke pricing
    content = content.replace('bg-[#238636] border border-[rgba(240,246,252,0.1)] border', 'bg-[#161b22] border')
    
    # Fix the </div><div> where it was used as a generic background for a <section> or container
    content = content.replace('bg-[#238636] border border-[rgba(240,246,252,0.1)] relative', 'bg-[#010409] relative')
    content = content.replace('bg-[#238636] border border-[rgba(240,246,252,0.1)] rounded-2xl', 'bg-[#161b22] rounded-2xl')

    # Fix invisible text spans
    content = content.replace('bg-[#238636] border border-[rgba(240,246,252,0.1)] bg-clip-text text-transparent', 'text-white')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Green blocks reverted.")
