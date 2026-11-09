#!/bin/bash

# Define the folder containing your wallpapers
WALLPAPER_DIR="."

# Loop through common image extensions (case-insensitive)
shopt -s nocaseglob
for img in "$WALLPAPER_DIR"/*.{jpg,jpeg,png,webp}; do
    # Check if the file actually exists (handles empty folders cleanly)
    [ -e "$img" ] || continue

    # Extract the filename without the path and extension
    filename=$(basename "$img" | sed 's/\.[^.]*$//')
    
    echo "Processing: $(basename "$img")..."
    
    # Convert and resize to raw BMP format
    magick "$img" -resize 1920x1080\! "$WALLPAPER_DIR/BMP/${filename}.bmp"
done
shopt -u nocaseglob

echo "All images converted to optimized BMP format!"

