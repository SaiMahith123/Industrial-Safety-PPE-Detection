from bing_image_downloader import downloader
import os

if not os.path.exists('dataset'):
    os.makedirs('dataset')
    print("Created 'dataset' folder.")

queries = ["construction worker helmet", "person without safety helmet"]

for q in queries:
    print(f"\n🚀 STARTING DOWNLOAD FOR: {q}")
    downloader.download(
        q, 
        limit=20,              
        output_dir='dataset', 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=60, 
        verbose=True           
    )

print("\n✅ ALL DONE! Check your 'dataset' folder now.")
