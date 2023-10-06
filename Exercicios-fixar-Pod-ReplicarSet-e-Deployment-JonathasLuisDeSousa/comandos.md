# Setup
```shell
kind create cluster
```

# POD
## declarativo
```shell
kubectl apply -f pod.yaml
```

## imperativa
```shell
kubectl run myfirstpod --image=nginx
```

## listar pod's
```shell
kubectl get pod
```

## Inspeção
```shell
kubectl describe pod/myfirstpod
```

## Deleção
```shell
kubectl delete pod/myfirstpod
```

# RelicaSet

## create
```shell
kubectl apply -f my-replicaset.yaml 
```

## status
```shell
kubectl get pod
```

## delete
```shell
kubectl delete rs/myfirstrs
```

# Deployment

## create
```shell
kubectl apply -f my-deployment.yaml 
```

## status
```shell
kubectl get pod
```

## update
```shell
kubectl apply -f my-deployment.yaml 
```

## status update
```shell
kubectl get pod -w
```

## rollBack
```shell
kubectl rollout undo deployment/my-deployment
```

## delete
```shell
kubectl delete deployment/my-deployment
```
