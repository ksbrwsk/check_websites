import sys
import requests

url_dict = {
    "Homepage": "https://ksbrwsk.de",
    "Düxer-Stammtisch": "https://ksbrwsk.de:3333",
    "QRCode-Generator": "https://ksbrwsk.de:9080",
    "Vocabulary-Trainer": "https://ksbrwsk.de:8080",
}
success = "\u2705"
error = "\u2718"


def check_webseite(name: str, url: str):
    try:
        response = requests.get(url, verify=False, timeout=10)
        status = response.status_code
        if status == 200:
            print(f"Status Webseite {name:<18} --> {success}")
        else:
            print(f"Status Webseite {name:<18} --> {error}")
    except:
        print(f"Status Webseite {name:<18} --> {error}")


def main():
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
    for entry in url_dict.keys():
        url = url_dict.get(entry)
        check_webseite(str(entry), str(url))


if __name__ == '__main__':
    main()
