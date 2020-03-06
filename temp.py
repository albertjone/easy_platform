target = """
||thumbzilla.com
||wikipedia.org
||github.com
||superuser.com
||vmware.com
||issuehunt.io
||tunnelblick.net
||tonymacx86.com
||amazonaws.com
||majorgeeks.com
||zetam.org
||adobe.com
||oracle.com
||omtrdc.net
||sourceforge.net
||ted.com
||twipu.com
||stalkfest.net
||tunnelblick.net
||github.com
||k8s.io
||opendev.org
||googleapis.com
||hopperapp.com
||stripe.com
||defcon.org
||githubusercontent.com
||vimeo.com
||vimeocdn.com
||stackoverflow.com
||githubassets.com
||projectatomic.io
||haiwaiyy.com
||apple.com
||phncdn.com
||facebook.com
||amd.com
||virtualbox.org
||google.com
||yahoo.com
||katacoda.com
||meijuxia.vip
||jp-nightlife.com
||avgle.com
||press.vin
||qooqlevideo.com
||histats.com
||freenom.com
"""
output = ""

for line in target.split():
    output += ("\"" + line.replace("||", "domain:") + "\",\n")
print(output)
     
