import os
import sys
import gzip
import tldextract
import time
import socket
import ipwhois


def locate_the_mainland(domain):
    if domain.endswith(".cn"):
        return True

    try:
        addr = socket.gethostbyname(domain.encode('utf-8'))
    except socket.gaierror:
        return None

    try:
        result = ipwhois.IPWhois(addr).lookup_rdap(depth=1)['asn_country_code']
        return True if result == 'CN' else False
    except ipwhois.exceptions.IPDefinedError:
        return False
    except ipwhois.exceptions.ASNRegistryError:
        return False


def line_analyzing(lines):
    domains = []

    for line in lines:
        line = line.split()

        if 'dnsmasq' not in line[4]:
            continue

        ext = tldextract.extract(line[6])
        if ext.registered_domain not in domains:
            domains.append(ext.registered_domain)

    return domains


def log_parsing(path):
    lines = []

    for filename in os.listdir(path):
        if 'syslog' not in filename:
            continue

        log = os.path.abspath(os.path.join(path, filename))

        if log.endswith('.gz'):
            with gzip.open(log, 'rt', encoding='utf-8') as data:
                lines += [line.rstrip() for line in data]
        else:
            with open(log, encoding='utf-8') as data:
                lines += [line.rstrip() for line in data]

    return lines


if __name__ == '__main__':
    if sys.argv[1] and os.path.exists(sys.argv[1]):
        current = []

        with open('whitelist.txt', 'r') as output:
            whitelist = [line.rstrip() for line in output]

        with open('master.txt', 'r') as output:
            for line in output:
                if line.startswith('127.0.0.1'):
                    current.append(line.split()[1].rstrip('\n'))

        with open('master.txt', 'w') as output:
            lines = log_parsing(sys.argv[1])
            domains = line_analyzing(lines)
            output.write('''#
# This file is created to be used with Algo VPN adblock
# See adblock.sh for more info:
#   https://github.com/trailofbits/algo/blob/master/roles/dns_adblocking/templates/adblock.sh.j2
#\n''')

            for domain in domains:
                if locate_the_mainland(domain) and domain not in current:
                    current.append(domain)
                    print("Positive: {}".format(domain))
                else:
                    print("Negative: {}".format(domain))

            for domain in whitelist:
                current.remove(domain)

            for domain in current:
                output.write("127.0.0.1\t{}\n".format(domain))

