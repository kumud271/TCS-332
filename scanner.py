import nmap

def scan_network(target):
    nm = nmap.PortScanner()

    try:
        # Scan services only (no root privileges required)
        nm.scan(hosts=target, arguments='-sV')

        results = []

        for host in nm.all_hosts():

            hostname = nm[host].hostname()

            if 'tcp' in nm[host]:

                for port in nm[host]['tcp']:

                    service = nm[host]['tcp'][port]['name']
                    state = nm[host]['tcp'][port]['state']

                    # Risk calculation
                    if port in [21, 23]:
                        risk = "High"
                    elif port in [22, 80, 443]:
                        risk = "Medium"
                    else:
                        risk = "Low"

                    results.append({
                        "host": host,
                        "hostname": hostname,
                        "port": port,
                        "state": state,
                        "service": service,
                        "risk": risk
                    })

        return results

    except Exception as e:
        return {"error": str(e)}                                                                                                       