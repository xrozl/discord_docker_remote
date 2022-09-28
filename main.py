import docker_lib
import discord
import yaml

def main():
    # Load config
    with open('config.yml', 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    # null check
    if cfg is None:
        print('Config is empty')
        return
    else:
        global token
        token = cfg['token']

    # Create discord client
    intents = discord.Intents.default()
    intents.message_content = True

    global client
    client = discord.Client(intents=intents)

    containers = docker_lib.get_container_list()
    if len(containers) == 0:
        print('No containers found')
    else:
        print('Containers found:')
        for i in range(len(containers)):
            print(str(i) + ': ' + str(containers[i]))


    client.run(token)

if __name__ == '__main__':
    main()
