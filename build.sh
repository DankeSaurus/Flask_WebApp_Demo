podman stop flask
podman rm flask
podman build -t flask_demo .
podman run -d --name flask -p 8080:8080 localhost/flask_demo

