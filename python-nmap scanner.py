import nmap
import optparse

def nmapScan(host, ports):
    nScan = nmap.PortScanner()
    nScan.scan(host, ports)
    state = nScan[host]['tcp'][int(ports)]['state']
    print " [*] " + host + " tcp/"+ ports + " " + state
def main():
    parser=optparse.OptionParser('usage%prog' +\
' -H<target Host> -p<target port>')
    parser.add_option('-H', dest='host')
    parser.add_option('-p' , dest='ports')
    (options, args) = parser.parse_args()
    host = options.host
    tps = str(options.ports).split(', ')
    if (host == "") or (tps == ""):
        print "Please specify target host and target ports"
        exit(0)
    for ports in tps:
        nmapScan(host, str(ports))
if __name__ == '__main__':
    main()