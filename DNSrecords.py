import dns
from dns import resolver 
#Ask user for domain
#Check each DKIM prefix iteration
#Check SPF, MX
#check cname
#print output

domain_name = input("Hello, please input the domain you are querying: ")

cname_input = (f"email.{domain_name}")

dkim_prefixes = ["mx.", "smtp.", "pic.", "krs.", "k1.", "mta.", "mailto."]

#return (prefix) for prefix in dkim_prefixes

new_dkim = [ (prefixes + "_domainkey." + domain_name) for prefixes in dkim_prefixes]

#test dkim

def dkim_record(domain):
    try:
        results = dns.resolver.resolve(domain, 'TXT')  
        for val in results:
            print('DKIM Record : ', val.to_text())
    except resolver.NXDOMAIN:
            pass
    except:
            manual_dkim = input('No DKIM, try entering the DKIM subdomain here: ')
            results = dns.resolver.query(manual_dkim, 'TXT')  
            for val in results:
                print('DKIM Record : ', val.to_text())
                
for i in range(len(new_dkim)):
    dkim_record(new_dkim[i]) 
   
def mx_record():
    result = dns.resolver.resolve(domain_name, 'MX')
    for val in result:
        print ('MX Record(s) ', val.preference, val.exchange)

mx_record()

def spf_record():
    result = dns.resolver.resolve(domain_name, 'TXT')
    for val in result:
        return val.to_text()

print ('SPF Record ', spf_record())
    
def cname_record():
    result = dns.resolver.resolve(cname_input, 'CNAME')
    for val in result:
        return val.to_text()

print ('CNAME Record ', cname_record())
