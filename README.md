## Full Stack Application with Monitoring and Logging

This project sets up the infrastructure for the Boss application using Docker Compose, Traefik, and AWS Route53. The setup includes a frontend, backend, database, and monitoring services with Traefik managing SSL certificates and path-based routing.

## Project Structure

The project is organized into the following structure:

- `application/`: Contains the application stack, including frontend, backend, and database services. Also contains configuration files for monitoring services such as Prometheus, Grafana, Loki, and Promtail.
- `frontend/`: Contains the source code for the frontend.
- `backend/`: Contains the source code for the backend.
- `traefik/`: Contains configuration files for the Traefik proxy.

## Features

1. **Traefik Proxy**:
   - Handles path-based routing for all services.
   - Automatically issues SSL certificates via Let's Encrypt.

2. **Route53 Domains**:
   - Two A records are set up for the domain:
     - `www.boss.kapilkumaria.com`
     - `boss.kapilkumaria.com`

3. **Monitoring**:
   - Prometheus, Grafana, Loki, and Promtail for application monitoring and logging.

## Prerequisites

1. Ensure Docker and Docker Compose are installed.
2. Set up the following A records in AWS Route53:
   - `www.boss.kapilkumaria.com`
   - `boss.kapilkumaria.com`
3. Point the A records to your server's IP address.

## Setup

### Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```
## Configure Environment Variables

    Adjust database credentials in the backend/.env file.
    Configure Traefik with the domain names in the docker-compose.yml file.

## Run the Application

Run the application stack and monitoring stack using Docker Compose:
```
docker compose up -d
```

## Access the Services

- Frontend: https://boss.kapilkumaria.com
- Backend API: https://boss.kapilkumaria.com/api
- Backend Docs: https://boss.kapilkumaria.com/docs
- Prometheus: https://boss.kapilkumaria.com/prometheus
- Grafana: https://boss.kapilkumaria.com/grafana
- Database Admin: https://boss.kapilkumaria.com/adminer

## Traefik Configuration

- SSL certificates for boss.kapilkumaria.com are automatically issued via Let's Encrypt.
- HTTP to HTTPS redirection and www to non-www redirection are handled by Traefik.

## Monitoring Setup

After all applications are successfully accessible through the custom domain, configure Grafana for visualizing metrics and logs:
Login to Grafana

## Access Grafana and login using the default credentials:

      Username: admin
      Password: admin

## Set Up Data Sources

### Prometheus:

- Add a new data source with the URL: http://prometheus:9090/prometheus

### Loki:

- Add a new data source with the URL: http://loki:3100

### Import Pre-Built Dashboard

- Import the Container Metrics dashboard using ID: 19792

## Create Custom Dashboard

    Create a new dashboard and configure the following variables in Settings:
        Variable 1:
            Name: container
            Display Name: Container
            Type: Query
            Label Value: container_name
        Variable 2:
            Name: container_search
            Display Name: Search
            Type: Textbox
        Variable 3:
            Name: severity
            Display Name: Severity
            Type: Custom
            Custom Values: info, warn, error
        Variable 4:
            Name: NodeLogs
            Display Name: Node Logs
            Type: Query
            Label Value: filename
        Variable 5:
            Name: varlog_search
            Display Name: NodeLog Filter
            Type: Textbox

- Create a new visualization for Container Logs with the following query:
```
{container_name="$container"} |~ `$container_search` | logfmt level | (level =~ `$severity` or level= "")

Create a new visualization for Node Logs with the following query:

    {job="varlogs"} |~ `$varlog_search`
```

## Functionality

**Container Logs**:
        Search container logs using container_search.
        Filter logs by severity (info, warn, error).

**Node Logs**:
        Search node logs using varlog_search.
        Apply filters for efficient log analysis.

## Verifications

1. Verify that all services are running and accessible via the defined paths.
2. Test HTTP to HTTPS redirection.
3. Test www to non-www redirection.

## Future Enhancements

- Add more services as required with Traefik managing the routing.
- Integrate additional monitoring tools if necessary.

## Troubleshooting

- **SSL Issues**:
        Ensure the domain A records are correctly pointing to your server.
        Check Traefik logs for any SSL certificate errors.

- **Service Connectivity**:
        Verify container logs for errors.
        Ensure environment variables are correctly configured.

