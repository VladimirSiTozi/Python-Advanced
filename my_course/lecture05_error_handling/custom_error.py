class PaymentError(Exception):
    pass


raise PaymentError('Payment cannot be processed at the moment! Please try again later!')
