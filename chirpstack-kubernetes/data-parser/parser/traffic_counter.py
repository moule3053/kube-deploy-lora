from math import floor

def bin16dec(bin_):
    num = bin_ & 0xFFFF
    if 0x8000 & num:
        num = -(0x010000 - num)
    return num
#' Decoder Version 2.2 ' : app_payload_v2_decoder
def traffic_counter(payload_hex):
    bytes_ = bytearray.fromhex(payload_hex)
    decoded_payload = {'SBX_BATT': '', 'SBX_PV': '', 'TEMP': '', 'L0_CNT': '', 'L0_AVG': '', 'R0_CNT': '', 'R0_AVG': '',
                       'L1_CNT': '', 'L1_AVG': '', 'R1_CNT': '',
                       'R1_AVG': '', 'L2_CNT': '', 'L2_AVG': '', 'R2_CNT': '', 'R2_AVG': '', 'L3_CNT': '', 'L3_AVG': '',
                       'R3_CNT': '', 'R3_AVG': ''}

    if len(bytes_) != 33:
        print('ERROR: Wrong payload length')
        return None

    # Check for Parametric TCR v2 payload
    if bytes_[0] == 0xbe and bytes_[1] == 0x02 and bytes_[2] == 0x02:

        decoded_payload['SBX_BATT'] = (bytes_[3] << 8 | bytes_[4])
        decoded_payload['SBX_PV'] = (bytes_[5] << 8 | bytes_[6])
        temp = (bytes_[7] << 8) | (bytes_[8])
        decoded_payload['TEMP'] = floor(bin16dec(temp) / 10)

        # Speed class 1
        decoded_payload['L0_CNT'] = (bytes_[9] << 8 | bytes_[10])
        decoded_payload['L0_AVG'] = bytes_[11]
        decoded_payload['R0_CNT'] = (bytes_[12] << 8 | bytes_[13])
        decoded_payload['R0_AVG'] = bytes_[14]

        # Speed class 2
        decoded_payload['L1_CNT'] = (bytes_[15] << 8 | bytes_[16])
        decoded_payload['L1_AVG'] = bytes_[17]
        decoded_payload['R1_CNT'] = (bytes_[18] << 8 | bytes_[19])
        decoded_payload['R1_AVG'] = bytes_[20]

        # Speed class 3
        decoded_payload['L2_CNT'] = (bytes_[21] << 8 | bytes_[22])
        decoded_payload['L2_AVG'] = bytes_[23]
        decoded_payload['R2_CNT'] = (bytes_[24] << 8 | bytes_[25])
        decoded_payload['R2_AVG'] = bytes_[26]

        # Speed class 4
        decoded_payload['L3_CNT'] = (bytes_[27] << 8 | bytes_[28])
        decoded_payload['L3_AVG'] = bytes_[29]
        decoded_payload['R3_CNT'] = (bytes_[30] << 8 | bytes_[31])
        decoded_payload['R3_AVG'] = bytes_[32]

    else:
        print('ERROR: TCR application payload V2 should start with be0202..')

    return decoded_payload

# payload = 'be0202000000000128000000000000000110000000000000000000000000000000'