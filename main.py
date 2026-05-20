import os
import shutil

extensions = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.avif', '.svg', '.ico', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.rtf', '.odt', '.epub'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.iso'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg'],
    'Programs': ['.exe', '.msi', '.jar', '.bat', '.sh', '.bin'],
    'Development': ['.py', '.js', '.html', '.css', '.php', '.cpp', '.c', '.java', '.ts', '.sql'],
    'Data': ['.json', '.md', '.xml', '.yaml', '.yml', '.db'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2']
}

directory = input(r"entree a directory: ")

if os.path.isdir(directory):
    fils_lifih = os.listdir(directory)

    for x in fils_lifih:
        old_file_path = os.path.join(directory, x)

       
        if os.path.isfile(old_file_path):
            ext = os.path.splitext(x)[1].lower()
            found = False 

            for category, list_ext in extensions.items():
                if ext in list_ext:
                    target = os.path.join(directory, category)
                    if not os.path.exists(target):
                        os.makedirs(target)

                    new_file_path = os.path.join(target, x)
                    shutil.move(old_file_path, new_file_path)
                    print(f"MOVED: {x} ===> {category}")
                    found = True 
                    break 

            
            if not found:
                others_path = os.path.join(directory, "Others")
                if not os.path.exists(others_path):
                    os.makedirs(others_path)
                shutil.move(old_file_path, os.path.join(others_path, x))
                print(f"MOVED TO OTHERS: {x}")
else:
    print("Error")