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
    "_includes/hero.html",
    "_layouts/default.html",
    "_layouts/landing.html"
]

for file in files_to_fix:
    if not os.path.exists(file):
        continue
    
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Simplify gigantic paddings
    content = re.sub(r'py-20 md:py-24|py-24|pt-[0-9]+ pb-[0-9]+ md:pt-[0-9]+ md:pb-[0-9]+', 'py-10 md:py-14', content)
    content = re.sub(r'py-16|py-12', 'py-8 md:py-10', content)

    # 2. Tone down typography sizes (No big fonts)
    content = re.sub(r'text-4xl md:text-5xl lg:text-6xl|text-4xl md:text-5xl lg:text-5xl|text-5xl', 'text-3xl md:text-4xl', content)
    content = re.sub(r'text-3xl md:text-5xl|text-3xl md:text-4xl', 'text-2xl md:text-3xl', content)
    content = re.sub(r'text-lg md:text-xl|text-xl', 'text-[15px] md:text-[16px]', content)
    content = re.sub(r'text-[0-9]+px', lambda m: m.group(0) if int(m.group(0).strip('text-px[]')) <= 16 else m.group(0), content)

    # 3. Tone down font weights
    content = content.replace('font-extrabold', 'font-semibold')
    content = content.replace('font-black', 'font-bold')
    
    # 4. Remove all crazy glowing background blobs (Web3 style -> standard Git style)
    content = re.sub(r'<div class="absolute[^>]*(blur-xl|blur-2xl|blur-3xl|bg-gradient)[^>]*></div>\n*', '', content)
    content = re.sub(r'<div class="absolute inset-0 bg-\[radial-gradient[^>]+></div>\n*', '', content)
    
    # 5. Tone down Shadows
    content = content.replace('shadow-2xl', 'shadow-sm')
    content = content.replace('shadow-xl', 'shadow-sm')
    content = content.replace('shadow-lg', 'shadow-sm')

    # 6. Simplify Buttons (standard Git style)
    content = content.replace('px-8 py-4', 'px-5 py-2.5 text-[14px]')
    content = content.replace('px-6 py-3.5', 'px-4 py-2 text-[14px]')
    content = content.replace('px-6 py-3', 'px-4 py-2 text-[14px]')

    # Change gradients on buttons to github green
    content = re.sub(r'bg-gradient-to-[r|br|l|t|b|bl]+ from-[a-z0-9\-]+ to-[a-z0-9\-]+', 'bg-[#238636] border border-[rgba(240,246,252,0.1)]', content)

    # Convert generic background classes to pure hex
    content = content.replace('bg-gh-canvas-dark', 'bg-[#0d1117]')
    content = content.replace('bg-gh-inset-dark', 'bg-[#010409]')
    content = content.replace('bg-gh-subtle-dark', 'bg-[#161b22]')
    content = content.replace('bg-gh-border-dark/20', 'bg-[#0d1117]')

    # Specific hero fixes
    content = content.replace('text-4xl md:text-5xl lg:text-5xl font-extrabold text-white', 'text-3xl md:text-4xl font-semibold text-white')
    content = content.replace('shadow-[0_0_8px_#238636]', '') # Remove excessive node shadows

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Design optimizations completed successfully.")
