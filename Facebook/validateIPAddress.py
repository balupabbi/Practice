def validIPAddress2(IP):
    def isIPv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(s):
        if len(s) > 4: return False
        try:
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False

    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
        return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
        return "IPv6"
    return "Neither"

def validateIP_mine(IP):


    """
    Ipv4 checks = check for 01,0234 etc, check for 0-255
    :param ip:
    :return:
    """
    if not IP:
        return "Neither"

    result = ['IPv6', 'IPv4']

    res = IP.split('.')

    if len(res) == 4:
        for i in res:
            if i.isdigit():
                if i[0] == '0':
                    return "Neither"
                elif not 0 <= int(i) <= 255:
                    return "Neither"
            else:
                return "Neither"
        return "IPv4"

    res = IP.split(':')

    hexa = set('0123456789abcdefABCDEF')

    if len(res) == 8:
        # check IPv6
        for seg in res:
            if not seg or not 0 <= len(seg) <= 4:
                return "Neither"
            elif all([False for i in seg if i not in hexa]):
                return "Neither"
        return "IPv6"
    else:
        return "Neither"

def validIPAddress(IP):
    def is_hex(s):
        hex_digits = set("0123456789abcdefABCDEF")
        for char in s:
            if not (char in hex_digits):
                return False
        return True

    ary = IP.split('.')
    if len(ary) == 4:
        for i in range(len(ary)):
            if not ary[i].isdigit() or not 0 <= int(ary[i]) < 256 or (ary[i][0] == '0' and len(ary[i]) > 1):
                return "Neither"
        return "IPv4"
    ary = IP.split(':')
    if len(ary) == 8:
        for i in range(len(ary)):
            tmp = ary[i]
            if len(tmp) == 0 or not len(tmp) <= 4 or not is_hex(tmp):
                return "Neither"
        return "IPv6"
    return "Neither"


def validIPAdress(IP):
    """
    regex method: https://leetcode.com/articles/validate-ip-address/
    :param IP:
    :return:
    """

    return



if __name__ == "__main__":
    test_cases = ["20EE:FGb8:85a3:0:0:8A2E:0370:7334",'172.16.254.1', '172.16.254.01','2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                  '2001:db8:85a3:0:0:8A2E:0370:7334','2001:0db8:85a3::8A2E:0370:7334','02001:0db8:85a3:0000:0000:8a2e:0370:7334']

    for test in test_cases:
        # print(test + ": "+ validIPAddress(test))
        print(test + ": "+ validateIP_mine(test))