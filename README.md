# simple-api-gateway
An implementation of the API Gateway microservices pattern. The nginx-ingress controller is used as the API Gateway.

1) Create "api-gateway" namespace.

2) Install helm charts:
  - for app service: helm install app ./app-chart
  - for auth-proxy service: helm install auth ./auth-proxy-chart