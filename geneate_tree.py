import sys
import json
from pathlib import Path

data = json.load(sys.stdin)

for crd in data.get("items", [data]):
  spec = crd["spec"]
  group = spec["group"]
  name = spec["names"]["singular"]

  for version in spec["versions"]:
    vname = version["name"]

    if "schema" not in version:
      print("%s/%s/%s does not have a schema; skipping" % (group, vname, name))
      continue

    schema = version["schema"]["openAPIV3Schema"]

    path = Path("api", group,  vname,  "%s.json" % name)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as f:
      json.dump(schema, f, indent=2)

    print("wrote %s" % path)
