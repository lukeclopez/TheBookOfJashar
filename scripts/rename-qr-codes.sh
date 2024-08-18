#!/bin/bash

# Directory containing the files
directory="./qr-codes"

# Loop through each file in the directory
for file in "$directory"/*.png; do
  # Extract the part of the filename after the last '-cities-' and before '.html.png'
  new_name=$(echo "$file" | sed -e 's/.*-cities-\(.*\)\.html\.png/\1/')

  # Rename the file to just 'cityname.png'
  mv "$file" "$directory/$new_name.png"

  echo "Renamed: $file -> $new_name.png"
done
