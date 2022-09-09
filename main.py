import requests,os,base64,json
os.system("cls")


sub_ids = []
guild_id = input("Guild ID: ")

def get_x_properties():
    data = {
        "os": "Windows",
        "browser": "Chrome",
        "device": "",
        "system_locale": "en-US",
        "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
        "browser_version": "102.0.5005.61",
        "os_version": "10",
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": 130153,
        "client_event_source": None
    }
    return base64.b64encode(json.dumps(data).encode())

response = requests.get('https://discord.com/register')

dcfduid = response.headers['Set-Cookie'].split('__dcfduid=')[1].split(';')[0]
sdcfduid = response.headers['Set-Cookie'].split('__sdcfduid=')[1].split(';')[0]

try:
    with open("tokens.txt", "r") as f:  
        tokens = f.read().splitlines()
    for token in tokens:
        data = requests.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", 
        headers={
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "authorization": token,
            "cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==",
            "referer": "https://discord.com/channels/967617613960187974/981260247807168532",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "x-discord-locale": "en-US",
            "x-super-properties":  get_x_properties()}) 
        try:
            for sub in data.json(): sub_ids.append(sub['id'])
            if sub_ids != []: 
                for i in range(len(sub_ids)):
                    r = requests.put(url=f"https://discord.com/api/v9/guilds/{guild_id}/premium/subscriptions", 
                    headers= {
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US,en;q=0.9",
                        "authorization": token,
                        "content-length": "67",
                        "content-type": "application/json",
                        "cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==",
                        "origin": "https://discord.com",
                        "referer": "https://discord.com/@me",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "sec-gpc": "1",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
                        "x-debug-options": "bugReporterEnabled",
                        "x-discord-locale": "en-US",
                        "x-super-properties": get_x_properties()},
                        json={"user_premium_guild_subscription_slot_ids":[f"{sub_ids[i]}"]})
                    if r.status_code == 201:
                        print(f"Boosted {i+1} of {len(sub_ids)} from {token[25:]}")
                    elif r.status_code == 400: 
                        print(f"Boost already used {i+1} of {len(sub_ids)} from {token[25:]}")
                sub_ids.clear()
            else: 
                print(f"Tokens doesn't have Nitro Boost {token[25:]}") 
        except:
            pass
except:pass  
