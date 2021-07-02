# simple-api-gateway
An implementation of the API Gateway microservices pattern. The nginx-ingress controller is used as the API Gateway.

* Create "api-gateway" namespace.
  - ```kubectl create namespace api-gateway```

* Enable ingress:
  - ```minikube addons enable ingress```

* Install helm charts:
  - for app service: ```helm install app ./app-chart``` (from app folder)
  - for auth-proxy service: ```helm install auth ./auth-proxy-chart``` (from auth_proxy folder)

* Apply ingress manifests:
  - ```kubectl apply -f auth-proxy-ingress.yaml```  (from root repository)
  - ```kubectl apply -f app-ingress.yaml```  (from root repository)

* Run newman tests:
  - ```newman run tests/postman/testing-api-gateway.postman_collection.json```
