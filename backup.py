import os
import asyncio
import hashlib
import tarfile


BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']
MINECRAFT_SERVER_DIR = os.environ['MINECRAFT_SERVER_DIR']


def compress():
    pass

def backup_change_check():
    pass

async def send_backup_tel():
    pass

async def send_backup_gdrive():
    pass

async def post_backups():
    send_backup_tel()    
    send_backup_gdrive()


async def main():
    pass


if __name__ == '__main__':
    asyncio.run(main())
