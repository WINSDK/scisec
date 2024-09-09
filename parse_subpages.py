import os
import pandas as pd
from bs4 import BeautifulSoup

attrs = []

def parse_site(content: str):
    global attrs

    soup = BeautifulSoup(content, 'html.parser')
    g_content_divs = soup.find_all(class_='g-content')

    for div in g_content_divs:
        paragraphs = div.find_all('p')
        for p in paragraphs:
            strong_tags = p.find_all('strong')
            if strong_tags and strong_tags[0].get_text().startswith('Headquarters'):
                parsed_info = {}
                content_lines = p.get_text(separator=' ').strip().split('\n')
                for i in range(0, len(content_lines) - 1, 2):
                    key = content_lines[i].replace(':', '').strip()
                    value = content_lines[i + 1].strip()
                    # Add key-value pair only if both key and value exist
                    if key and value:
                        parsed_info[key] = value

                parsed_info["site"] = soup.find('link', {'rel': 'canonical'})['href']

                # Append parsed_info to the list if it contains any data
                if parsed_info:
                    attrs.append(parsed_info)

parse_site(open("output/santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion_archive_prettl-com.html").read())


# Iterate over all files in the output directory
# for path in os.listdir("./output"):
#     content = open(f"./output/{path}").read()
#     parse_site(content)

# Convert list of dicts to a pandas DataFrame
df = pd.DataFrame(attrs)

# Save the DataFrame as a CSV file
df.to_csv('output/data.csv', index=False)

print("CSV file created successfully! (output/data.csv)")
