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

    gvk = "%s/%s/%s" % (group, vname, name)

    if "schema" not in version:
      print("%s does not have a schema; skipping" % gvk)
      continue

    schema = version["schema"]["openAPIV3Schema"]

    if "properties" in schema:
      schema["properties"]["apiVersion"]["enum"] = ["%s/%s" % (group, vname)]
      schema["properties"]["kind"]["enum"] = ["%s" % spec["names"]["kind"]]

      required = schema.get("required", [])
      required.extend(["apiVersion", "kind"])
      schema["required"] = list(set(required))

    path = Path("api", group,  vname,  "%s.json" % name)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as f:
      json.dump(schema, f, indent=2)

    print("wrote %s" % path)
