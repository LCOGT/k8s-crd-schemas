import sys
import json
from pathlib import Path

data = json.load(sys.stdin)

for crd in data.get("items", [data]):
  spec = crd["spec"]
  group = spec["group"]
  name = spec["names"]["singular"]

  for version in spec["versions"]:
    if "schema" not in version:
      print("%s/%s does not have schema; skipping" % (group, name))
      continue

    vname = version["name"]
    schema = version["schema"]["openAPIV3Schema"]

    path = Path("api", group,  name,  "%s.json" % vname)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as f:
      json.dump(schema, f, indent=2)

    print("wrote %s" % path)
