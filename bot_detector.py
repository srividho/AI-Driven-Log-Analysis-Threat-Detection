#Bot vs Human Classification

#!/usr/bin/env python3
"""
bot_detector.py
Classifies traffic as Bot or Human based on User-Agent and Referrer.
"""

import re
from collections import defaultdict

LOG_FILE = "access.log"

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+).+?"[A-Z]+\s+.+?\s+HTTP.*?"\s+\d{3}.+?"(?P<referrer>.*?)"\s+"(?P<agent>.*?)"'
)

bot_indicators = ["bot", "crawl", "spider", "wget", "curl", "python-requests"]

ip_data = defaultdict(lambda: {"requests": 0, "type": "Human"})

with open(LOG_FILE, "r") as f:
    for line in f:
        match = log_pattern.search(line)
        if match:
            ip = match.group("ip")
            agent = match.group("agent").lower()
            referrer = match.group("referrer").lower()

            ip_data[ip]["requests"] += 1
            # Check bot indicators
            if any(keyword in agent for keyword in bot_indicators) or referrer == "-":
                ip_data[ip]["type"] = "Bot"

print("\n🤖 Bot vs Human Traffic Classification:\n")
print("{:<15} {:<10} {:<10}".format("IP Address", "Requests", "Type"))
print("-" * 40)

for ip, data in sorted(ip_data.items(), key=lambda x: x[1]["requests"], reverse=True):
    print(f"{ip:<15} {data['requests']:<10} {data['type']:<10}")


