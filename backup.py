import os
import asyncio
import tarfile
import subprocess
import telegram
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']
MINECRAFT_SERVER_DIR = os.environ['MINECRAFT_SERVER_DIR']


def compress():
    with tarfile.open("Backup.tar.gz", "w:gz") as tar:
        tar.add(MINECRAFT_SERVER_DIR, arcname="Backup")

def backup_change_check():
    hash = subprocess.run(['sha256sum', os.getcwd() + '/Backup.tar.gz'], capture_output=True, text=True)
    hash = hash.stdout.split()[0]

    if not os.path.exists(os.getcwd() + '/HASH'):
        with open('HASH', 'w') as hash_file:
            hash_file.write(hash)
    else:
        with open('HASH', 'r') as hash_file:
            prev_hash = hash_file.readline()
        if prev_hash == hash:
            exit()

async def send_backup_tel():
    bot = telegram.Bot(BOT_TOKEN)
    async with bot:
        with open('Backup.tar.gz', 'rb') as file:
            await bot.send_document(chat_id=CHANNEL_ID, document=file)

async def send_backup_gdrive():
    pass


async def main():
    compress()
    backup_change_check()
    tel = asyncio.create_task(send_backup_tel())
    google = asyncio.create_task(send_backup_gdrive())

    await tel
    await google


if __name__ == '__main__':
    asyncio.run(main())
