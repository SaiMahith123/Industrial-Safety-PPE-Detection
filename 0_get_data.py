from bing_image_downloader import downloader
import os

# Create the folder first just in case
if not os.path.exists('dataset'):
    os.makedirs('dataset')
    print("Created 'dataset' folder.")

queries = ["construction worker helmet", "person without safety helmet"]

for q in queries:
    print(f"\n🚀 STARTING DOWNLOAD FOR: {q}")
    downloader.download(
        q, 
        limit=20,              # Lower limit just to test quickly
        output_dir='dataset', 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=60, 
        verbose=True           # This will show progress in terminal
    )

print("\n✅ ALL DONE! Check your 'dataset' folder now.")