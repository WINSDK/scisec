#!/bin/bash
set -e

mkdir -p output

# Read URLs from stdin
while read -r url; do
    # Create a valid filename from the URL by replacing special characters
    filename=$(echo "$url" | sed 's|http://||; s|https://||; s|[/:]|_|g')

    if [ -f "output/$filename.html" ]; then
        echo "File output/$filename.html already exists. Skipping..."
        continue
    fi
    
    # Call curl with the required headers and options, and save the output to the file
    curl "$url" \
        -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' \
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' \
        -H 'Accept-Language: en-US,en;q=0.5' \
        -H 'Accept-Encoding: gzip, deflate, br' \
        -H "Referer: http://santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion" \
        -H 'Connection: keep-alive' \
        -H 'Cookie: dcap=37C8B2EB8AD8FD9CF3D51608F28316E9AA45704F3A1AD50C97E4BA9C0FAC7F89A8584AA9EBF2D6D5DCF9022627A0D5655978B00356147CA9FC8B7ED9FFD391AA4EA0060F0587BE362E2DB3DBBF6D1FAE; grav-site-40d1b2d=09efcnns7lj5ofq5fr368pndbd' \
        -H 'Upgrade-Insecure-Requests: 1' \
        -H 'Sec-Fetch-Dest: document' \
        -H 'Sec-Fetch-Mode: navigate' \
        -H 'Sec-Fetch-Site: same-origin' \
        -H 'Sec-Fetch-User: ?1' \
        --socks5-hostname localhost:5050 \
        -o "output/$filename.html"
    
    echo "Saved $url to $filename.html"
done
