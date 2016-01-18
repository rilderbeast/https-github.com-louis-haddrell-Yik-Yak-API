import requests
import settings

ENDPOINT = "https://beta.yikyak.com/api/proxy/v1/"


class YikYak(object):
    def __init__(self, country_code, phone_number, pin):
        self.auth_token = self._login(country_code, phone_number, pin)

    def init_pairing(self, user_id):
        """
        Initialise web pairing and retrieve authentication PIN

        Arguments:
            user_id (string): YikYak user ID

        Returns:
            6 digit PIN code for use with pairing
        """
        url = "https://beta.yikyak.com/api/auth/initPairing"
        data = {
            'userID': user_id
        }
        response = requests.post(url, data=data)
        return response.json()['pin']

    def _login(self, country_code, phone_number, pin):
        """
        Login to YikYak to retrieve authentication token

        Arguments:
            country_code (string): 3-letter string representing country
            phone_number (string): phone number
            pin (string): authentication PIN generated by mobile app

        Returns:
            Authentication token required for further YikYak access
        """
        url = "https://beta.yikyak.com/api/auth/pair"

        headers = {
            'Referer': 'https://beta.yikyak.com/',
        }

        payload = {
            'countryCode': country_code,
            'phoneNumber': phone_number,
            'pin': pin,
        }

        response = requests.post(url, headers=headers, json=payload)
        return response.json()


if __name__ == "__main__":
    yakker = YikYak("GBR", settings.PHONE_NUMBER, "258928")
