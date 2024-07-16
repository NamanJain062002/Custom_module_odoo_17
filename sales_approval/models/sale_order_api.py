from odoo import models, fields, api
import requests
import datetime
import hmac
import hashlib
import base64
import json

from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def get_digest(self, payload):
        hashobj = hashlib.sha256()
        hashobj.update(json.dumps(payload).encode('utf-8'))
        hash_data = hashobj.digest()
        digest = base64.b64encode(hash_data)
        return digest.decode('utf-8')

    def get_signature(self, method, resource, timestamp, digest, secret_key, key_id):
        merchant_id = 'namanjain2002_1720527590'
        signature_header = f"host: apitest.cybersource.com\nv-c-date: {timestamp}\nrequest-target: {method.lower()} {resource}\ndigest: SHA-256={digest}\nv-c-merchant-id: {merchant_id}"
        signature = base64.b64encode(
            hmac.new(base64.b64decode(secret_key), signature_header.encode('utf-8'), hashlib.sha256).digest()).decode(
            'utf-8')
        signature = f'keyid="{key_id}", algorithm="HmacSHA256", headers="host v-c-date request-target digest v-c-merchant-id", signature="{signature}"'
        return signature

    def action_capture_in_cybersource(self):
        self.ensure_one()
        if not self.partner_id.email:
            raise UserError('Customer email is required to process the payment.')

        merchant_id = 'namanjain2002_1720527590'
        key_id = 'e0ecf9b4-23a1-42b8-a79e-d852600f5e5a'
        secret_key = "LGGe3+rS8fJvtKXwatUNuO6EOUy4WRvDPo/uZ/2lslI="
        cybersource_url = 'https://apitest.cybersource.com/pts/v2/payments'

        payment_data = {
            "clientReferenceInformation": {
                "code": "TC50171_3"
            },
            "paymentInformation": {
                "card": {
                    "number": "4111111111111111",
                    "expirationMonth": "12",
                    "expirationYear": "2031"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    "totalAmount": self.amount_total,
                    "currency": "USD"
                },
                "billTo": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "address1": "1 Market St",
                    "locality": "san francisco",
                    "administrativeArea": "CA",
                    "postalCode": "94105",
                    "country": "US",
                    "email": "test@cybs.com",
                    "phoneNumber": "4158880000"
                }
            }
        }

        timestamp = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        digest = self.get_digest(payment_data)
        signature = self.get_signature("POST", "/pts/v2/payments", timestamp, digest, secret_key, key_id)

        headers = {
            'host': "apitest.cybersource.com",
            'v-c-date': timestamp,
            'digest': f"SHA-256={digest}",
            'v-c-merchant-id': merchant_id,
            'signature': signature,
            'Content-Type': 'application/json'
        }

        response = requests.post(cybersource_url, headers=headers, data=json.dumps(payment_data))
        print(response)
        if response.status_code == 201:
            # invioce = self.env['project.create.invoice']
            # invioce.action_create_invoice()

            self._create_invoices()
            self.message_post(body="Payment successfully captured via CyberSource.")
        else:
            self.message_post(body=f"Failed to capture payment: {response.text}")

