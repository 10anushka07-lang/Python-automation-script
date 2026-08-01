import os
import shutil
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

folder = input("Enter folder path: ")

if not os.path.exists(folder):
    print("Folder does not exist.")
    exit()

rename = input("Rename files? (yes/no): ").lower()

try:
    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            ext = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():

                if ext in extensions:

                    category_path = os.path.join(folder, category)

                    os.makedirs(category_path, exist_ok=True)

                    new_name = file

                    if rename == "yes":
                        count = len(os.listdir(category_path)) + 1
                        new_name = f"{category}_{count}{ext}"

                    shutil.move(
                        file_path,
                        os.path.join(category_path, new_name)
                    )

                    logging.info(f"Moved {file} -> {category}/{new_name}")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(folder, "Others")
                os.makedirs(other_path, exist_ok=True)

                shutil.move(file_path, os.path.join(other_path, file))
                logging.info(f"Moved {file} -> Others")

    print("Organization completed successfully!")

except Exception as e:
    logging.error(str(e))
    print("Error:", e)