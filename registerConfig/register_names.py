from enum import Enum

class UART(Enum):
    LCRH = "UARTLCRH"


class ADC(Enum):
    ACTSS = "ADCACTSS"
    RIS = "ADCRIS"
    IM = "ADCIM"
    ISC = "ADCISC"
    PSSI = "ADCPSSI"
    SSMUX = "ADCSSMUX"
    SSCTL = "ADCSSCTL"
    SSFIFO = "ADCSSFIFO"
    SSFSTAT = "ADCSSFSTAT"
    SSOP = "ADCSSOP"
    CC = "ADCCC"