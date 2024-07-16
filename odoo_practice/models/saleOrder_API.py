# from odoo import models, fields, api
# import requests
# import datetime
# import hmac
# import hashlib
# import base64
# import json
#
#
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     def demo(self):
#         self.ensure_one()
#         order = self
#
#         url = "https://apitest.cybersource.com/pts/v2/payments"
#         payload = {
#             "clientReferenceInformation": {
#                 "code": "TC50171_3"
#             },
#             "paymentInformation": {
#                 "card": {
#                     "number": "4111111111111111",
#                     "expirationMonth": "12",
#                     "expirationYear": "2031"
#                 }
#             },
#             "orderInformation": {
#                 "amountDetails": {
#                     "totalAmount": "102.21",
#                     "currency": "USD"
#                 },
#                 "billTo": {
#                     "firstName": "John",
#                     "lastName": "Doe",
#                     "address1": "1 Market St",
#                     "locality": "san francisco",
#                     "administrativeArea": "CA",
#                     "postalCode": "94105",
#                     "country": "US",
#                     "email": "mailto:test@cybs.com",
#                     "phoneNumber": "4158880000"
#                 }
#             }
#         }
#
#         # Prepare the headers
#         merchant_id = "namanjain2002_1720527590"
#         key_id = "e0ecf9b4-23a1-42b8-a79e-d852600f5e5a"
#         secret_key = "LGGe3+rS8fJvtKXwatUNuO6EOUy4WRvDPo/uZ/2lslI="  # Replace with your actual secret key
#         timestamp = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
#         digest = base64.b64encode(hashlib.sha256(json.dumps(payload).encode('utf-8')).digest()).decode('utf-8')
#         print(digest)
#         signature_header = f"host: apitest.cybersource.com\nv-c-date: {timestamp}\nrequest-target: post /pts/v2/payments\ndigest: SHA-256={digest}\nv-c-merchant-id: {merchant_id}"
#         signature = base64.b64encode(
#             hmac.new(base64.b64decode(secret_key), signature_header.encode('utf-8'), hashlib.sha256).digest()).decode(
#             'utf-8')
#         signature = f'keyid="{key_id}", algorithm="HmacSHA256", headers="host v-c-date request-target digest v-c-merchant-id", signature="{signature}"'
#
#         headers = {
#             'host': "apitest.cybersource.com",
#             'v-c-date': timestamp,
#             'digest': f"SHA-256={digest}",
#             'v-c-merchant-id': merchant_id,
#             'signature': signature,
#             'Content-Type': 'application/json'
#         }
#
#         response = requests.post(url, json=payload, headers=headers)
#         if response.status_code == 201:
#             self.message_post(body="Payment successfully captured via CyberSource.")
#         else:
#             self.message_post(body=f"Failed to capture payment: {response.text}")
#
#         return True