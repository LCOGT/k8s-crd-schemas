# k8s-crd-schemas

Catalog of OpenAPI Schemas for Kubernetes CRDs (Custom Resource Definitions)

## Generate

Enter devenv:

```shell
nix develop --impure
```

Pipe CRDs to genrate script:

```shell
kubectl get crds -o json | generate-tree
```

This will output schemas to `api/<API Group>/<kind name>/<version>.json`.
