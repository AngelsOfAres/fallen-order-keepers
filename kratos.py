import os
from client import client

for filename in os.listdir('./c_kratos'):
    if filename.endswith('.py'):
        client.load_extension(f'c_kratos.{filename[:-3]}')
        
client.run('YOUR BOT TOKEN HERE')