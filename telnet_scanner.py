# this program will search for open port 21- telent in the local subnet
import nmap
import optparse
def findTargets(subnet):
    nmscan = nmap.PortScanner()
    nmscan.scan(subnet, '21')
    targethosts= []
    for host in nmscan.all_hosts():
       if nmscan[host].has_tcp(21):
           state = nmscan[host]['tcp'][21]['state']
           if state == 'open':
              print '[+] Found Target Host: ' +host+ ' Has open port 21-telnet'
              targethosts.append(host)
    return targethosts
def main():
    parser = optparse.OptionParser("usage%prog "+\
            "-H <Subnet>")
    parser.add_option('-H', dest='subnet', type='string')
    (options, args) = parser.parse_args()
    if (options.subnet == None):
        print parser.usage
        exit(0)
    else:
        subnet = options.subnet
    Host = findTargets(subnet)
    if Host == True:
        exit(0)
    
if __name__ == '__main__':
    main()
