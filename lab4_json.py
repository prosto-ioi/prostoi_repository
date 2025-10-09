import json

with open("sample-data.json") as f:
    data = json.load(f)

interfaces = data["imdata"]

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<8}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 8)

for intf in interfaces:
    attrs = intf["l1PhysIf"]["attributes"]
    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")
    print("{:<50} {:<20} {:<8} {:<8}".format(dn, descr, speed, mtu))
