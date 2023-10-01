## Despliegue de la Aplicación en Kubernetes

### Backend

Desde la carpeta del backend, ejecuta los siguientes comandos para construir y ejecutar la imagen Docker del backend:

```bash
docker build -t ami-ucsp-ide-backend-k8s-parcial .
docker run -p 5000:5000 ami-ucsp-ide-backend-k8s-parcial
```

Luego, etiqueta la imagen Docker con un nombre más descriptivo:

```bash
docker tag ami-ucsp-ide-backend-k8s-parcial moisessalazar/ami-ucsp-ide-backend-k8s-parcial
```
Inicia sesión


 en Docker (si aún no lo has hecho) y sube la imagen Docker al registro de Docker:

```bash
docker login
docker push moisessalazar/ami-ucsp-ide-backend-k8s-parcial
```
A continuación, aplica los archivos YAML de despliegue y servicio para el backend en Kubernetes:
```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```
Utiliza el siguiente comando para obtener información sobre los servicios y los puertos asignados:

```bash
kubectl get services --all-namespaces
```
#Importante el puerto ponerlo en el index.html para comunidarse con el backend
### Frontend
Desde la carpeta del frontend, crea y ejecuta la imagen Docker del frontend con los siguientes comandos:
```bash
docker build -t ami-ucsp-ide-frontend-k8s-parcial .
docker run -p 8080:8080 ami-ucsp-ide-frontend-k8s-parcial
```
Etiqueta la imagen Docker del frontend con un nombre más descriptivo:

```bash
docker tag ami-ucsp-ide-frontend-k8s-parcial moisessalazar/ami-ucsp-ide-frontend-k8s-parcial
```
Inicia sesión en Docker y sube la imagen al registro de Docker:
```bash
docker login
docker push moisessalazar/ami-ucsp-ide-frontend-k8s-parcial
```

### Validación
Verifica que los pods estén en funcionamiento ejecutando:
```bash
kubectl get pods --all-namespaces
```
Si deseas eliminar un despliegue, puedes usar el siguiente comando:
```bash
kubectl delete deployment nombre_del_despliegue
```
Para eliminar todos los despliegues en el espacio de nombres predeterminado:
```bash
kubectl delete deployment --namespace=default --all
```
### Creación del Dashboard de Kubernetes
Aplica el archivo YAML para crear el Dashboard de Kubernetes:
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```
Luego, aplica los archivos YAML para la autenticación y los permisos necesarios, carpeta k8s:
```bash
kubectl apply -f dashboard-adminuser.yaml
kubectl apply -f cluster-role-binding.yaml
```
Obtén el nombre del enlace de roles del clúster:
```bash
kubectl get clusterrolebinding admin-user
```
Obtén el token de autenticación:
```bash
kubectl -n kubernetes-dashboard create token admin-user
```
Inicia un proxy para acceder al Dashboard:
```bash
kubectl proxy
```

http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

https://github.com/MoisesSalazar/K8S-IDE/assets/42578698/12f5c6ec-448f-4cd4-bd03-78aa5d5e6948
