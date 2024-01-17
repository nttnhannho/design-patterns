class MomoPaymentAdapter:
    def __init__(self, momo_payment):
        self.momo_payment = momo_payment

    def pay_by_visa(self, visa_payment):
        payment_converted = MomoPaymentAdapter.convert_to_visa_payment(self.momo_payment)
        visa_payment.pay(payment_converted)

    @staticmethod
    def convert_to_visa_payment(momo_payment):
        conversion_rate = 24000
        visa_amount = momo_payment.amount / conversion_rate
        visa_payment = {
            'card_number': momo_payment.card_number,
            'expired_date': momo_payment.expired_date,
            'cvv': momo_payment.cvv,
            'amount': visa_amount,
        }

        return visa_payment


class VisaPayment:
    @staticmethod
    def pay(payment):
        print(f'Paying {payment["amount"]} USD with Visa card {payment["card_number"]}')


class MomoPayment:
    def __init__(self, card_number, expired_date, cvv, amount):
        self.card_number = card_number
        self.expired_date = expired_date
        self.cvv = cvv
        self.amount = amount


def main():
    momo_payment = MomoPayment('123456', '12/25', 555, 24000)
    momo_adapter = MomoPaymentAdapter(momo_payment)
    visa_payment = VisaPayment()
    momo_adapter.pay_by_visa(visa_payment)


if __name__ == '__main__':
    main()
