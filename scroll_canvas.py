from web3 import Web3, Account
import time
import random
import datetime
import requests
import json
import string

# ПРОКСИ ВКЛЮЧИТЬ ИЛИ ВЫКЛЮЧИТЬ? ФОРМАТ (IP:PORT:USERNAME:PASSWORD)
PROXY = False
# ЖДАТЬ КОГДА ЕБАНЫЙ ЧЕЙН РАЗДУПЛИТСЯ ИЛИ ПРОСТО ПИЗДОВАТЬ ВПЕРЕД?
WAIT_FOR_SUCCESS = False
# СОН МЕЖДУ АККАМИ
SLEEP = 10, 30

# НЕ ТРОГАЙ, СЫНОК, ЕБАНЕТ, РАЗВЕ ЧТО RPC_SCROLL.
RPC_SCROLL = 'https://scroll.drpc.org'
# НУ ЭТО ТОЧНО НЕ НУЖНО ТРОГАТЬ!
SCROLL_CHAIN_ID = 534352
CONTRACT_ADDRESS = '0xB23AF8707c442f59BDfC368612Bd8DbCca8a7a5a'
CONTRACT_ABI = '[{"inputs":[{"internalType":"address","name":"_logic","type":"address"},{"internalType":"address","name":"admin_","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},{"stateMutability":"payable","type":"receive"}]'
scanner_link = 'https://scrollscan.com/tx/'

with open('private_keys.txt', 'r') as file:
    private_keys = [line.strip() for line in file]

with open('proxy.txt', 'r') as proxy_file:
    proxies = [line.strip() for line in proxy_file]

base_names = [
    "Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Ivy", "Jack",
    "Katherine", "Liam", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Rachel", "Sophia", "Tom",
    "Uma", "Vera", "William", "Xena", "Yara", "Zane", "KFC", "MCDONALDS", 'Degen', 'Huesos', 'Pedro', 'Ebaklak', 'Friend', 'Donald', 'Trump', 'Biden',
    "Daun", 'Clown', 'Homunculus', 'Sabaka', 'Christiano', 'Racer', 'Flamingo', 'Skoobidoo', 'Papandos', 'Dikiy', 'Uganda'
]

print(random_ref)
def modify_name(name):
    modified_name = ""
    for char in name:
        if random.random() < 0.2:
            modified_name += random.choice(string.ascii_letters)
        else:
            modified_name += char
    insert_position = random.randint(0, len(modified_name))
    modified_name = modified_name[:insert_position] + modified_name[insert_position:]

    return modified_name


def generate_human_like_name():
    base_name = random.choice(base_names)
    return modify_name(base_name)


def get_signature(wallet):
    refs = [ "OV4HI", "6CC2Z"]
    random_ref = random.choice(refs)
    url = f"https://canvas.scroll.cat/code/{random_ref}/sig/{wallet}"
    headers = {
        "Host": "canvas.scroll.cat",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
        "Accept-Language": "ru-RU",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Accept": "*/*",
        "Origin": "https://scroll.io",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://scroll.io/",
        "Priority": "u=1, i"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    signature = data.get("signature")
    return signature

def check_minted():
    contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=CONTRACT_ABI)
    getprofile = contract.functions.getProfile(account.address).call()
    is_claimed = contract.functions.isProfileMinted(getprofile).call()
    print(f"CANVAS Profile already minted!", is_claimed)
    return is_claimed

def mint_shit():
    contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=CONTRACT_ABI)
    random_name = generate_human_like_name()
    signature = get_signature(account.address)
    tx = contract.functions.mint(random_name, signature).build_transaction({
        'chainId': SCROLL_CHAIN_ID,
        'gas': '0',
        'gasPrice': '0'
        'nonce': w3.eth.get_transaction_count(w3.to_checksum_address(account.address)),
        'value': w3.to_wei(0.0005, 'ether'),
    })
    gasPrice = int(web3.eth.gas_price * (1 + (random.randint(1, 9) / 10)))
    time.sleep(1)
    gas_info = web3.eth.estimate_gas(token_txn)
    time.sleep(1)
    gas = int(gas_info*(1+(random.randint(1,9)/10)))
    tx.update({'gas': int(gas),'gasPrice': gasPrice})
    print(f"gas:{gas} | gasPrice: {gasPrice}")
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"SIGNED TX: {tx_hash.hex()} (pending...)")
    if WAIT_FOR_SUCCESS is False:
        return 1
    else:
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        success = receipt['status']
        link_to_scan = scanner_link + tx_hash.hex()
    if success == 1:
        print(f"SUCCESS MINT! | TX: {link_to_scan}")
        return success
    else:
        print(f"FAIL MINT! | TX: {link_to_scan}")


num = 0
for private_key, proxy_info in zip(private_keys, proxies):
    proxy_ip, port, username, password = proxy_info.split(":")
    if username == 'PweFh8Mc':  # FIX SOCKS TO HTTP
        newport = int(port) - 1
        proxy_url = f"http://{username}:{password}@{proxy_ip}:{newport}"
    else:
        proxy_url = f"http://{username}:{password}@{proxy_ip}:{port}"
    num += 1
    if PROXY is True:
        w3 = Web3(Web3.HTTPProvider(endpoint_uri=RPC_SCROLL, request_kwargs={"proxies": {'https': proxy_url, 'http': proxy_url}}))
    else:
        w3 = Web3(Web3.HTTPProvider(RPC_SCROLL))
    account = Account.from_key(private_key)
    address = account.address
    tx_count = w3.eth.get_transaction_count(address)
    balance = w3.from_wei(w3.eth.get_balance(address), 'ether')
    print(f"№{num} | {address} | TX: {tx_count} | {balance} | PROXY: {proxy_ip}")
    is_minted = check_minted()
    if is_minted is True:
        continue
    else:
        success = mint_shit()
        if success == 1:
            print(f"СПИМ МЕЖДУ АККАМИ.... zZz...Zzz...")
            time.sleep(random.randint(SLEEP[0], SLEEP[1]))
