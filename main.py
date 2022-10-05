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
        "client_build_number": 999999,
        "client_event_source": None
    }
    return base64.b64encode(json.dumps(data).encode())

response = requests.get('https://discord.com/register')

dcfduid = response.headers['Set-Cookie'].split('__dcfduid=')[1].split(';')[0]
sdcfduid = response.headers['Set-Cookie'].split('__sdcfduid=')[1].split(';')[0]
stripe_mid = response.headers['Set-Cookie'].split('__stripe_mid=')[1].split(';')[0]
stripe_sid = response.headers['Set-Cookie'].split('__stripe_sid=')[1].split(';')[0]
cf_bm = response.headers['Set-Cookie'].split('__cf_bm=')[1].split(';')[0]

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
            "cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; locale=en-US; __stripe_mid={stripe_mid}; __stripe_sid={stripe_sid}; __cf_bm={cf_bm}",
            "referer": "https://discord.com/channels/967617613960187974/981260247807168532",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "x-discord-locale": "en-US",
            "x-super-properties":  get_x_properties()}) 
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
                    "cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; locale=en-US; __stripe_mid={stripe_mid}; __stripe_sid={stripe_sid}; __cf_bm={cf_bm}",
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
                if r.status_code == 201:print(f"Boosted")
                elif r.status_code == 400:print(f"Boosts used")
            sub_ids.clear()
        else:print("No Nitro detected") 
except:pass  
