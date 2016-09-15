import re

logPath = "D:\\DataScience\\access_log.txt"
format_pat = re.compile(r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
                        )

URLCounts = {}
with open(logPath,'r') as f:
    for line in (l.rstrip() for l in f):
        match = format_pat.match(line)
        if match:
            access = match.groupdict()
            request = access['request']
            fields = request.split()
            if len(fields)==3 :
                print  fields
                URL = fields[1]



                if URLCounts.has_key(URL):
                    URLCounts[URL] = URLCounts[URL]+1
                else:
                    URLCounts[URL]=1

results = sorted(URLCounts, key=lambda i: int(URLCounts[i]),reverse=True)

for result in results[:30]:
    print result + ": " +str(URLCounts[result])