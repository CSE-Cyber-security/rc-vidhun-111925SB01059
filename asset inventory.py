class Asset:
    def __init__(self, asset_id, name, asset_type, ip, os, dept, risk, status):
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.ip = ip
        self.os = os
        self.dept = dept
        self.risk = risk
        self.status = status

assets = []

n = int(input("Enter number of assets: "))

for i in range(n):
    print(f"\nAsset {i+1}")

    asset_id = input("Asset ID: ")
    name = input("Asset Name: ")
    asset_type = input("Asset Type: ")
    ip = input("IP Address: ")
    os = input("Operating System: ")
    dept = input("Department: ")
    risk = input("Risk Level: ")
    status = input("Security Status: ")

    assets.append(
        Asset(asset_id, name, asset_type, ip, os, dept, risk, status)
    )

print("\n=========================================")
print("CYBERSECURITY ASSET INVENTORY")
print("=========================================")

critical = high = medium = vulnerable = 0

for a in assets:
    print(f"\nAsset ID : {a.asset_id}")
    print(f"Asset Name : {a.name}")
    print(f"Asset Type : {a.asset_type}")
    print(f"IP Address : {a.ip}")
    print(f"OS : {a.os}")
    print(f"Department : {a.dept}")
    print(f"Risk Level : {a.risk}")
    print(f"Status : {a.status}")
    print("-----------------------------------------")

    if a.risk.lower() == "critical":
        critical += 1
    elif a.risk.lower() == "high":
        high += 1
    elif a.risk.lower() == "medium":
        medium += 1

    if a.status.lower() == "vulnerable":
        vulnerable += 1

print("=========================================")
print("Total Assets :", len(assets))
print("Critical Assets :", critical)
print("High Risk Assets :", high)
print("Medium Risk Assets :", medium)
print("Vulnerable Assets :", vulnerable)
print("=========================================")