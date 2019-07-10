# odoo-k8s-health-check
Let K8S know if the app is ready or alive/dead

## Synopsis

By default Odoo will log every web request.

When running in OpenShift/K8S we want to verify if the web pod is ready to accept traffic,
or verify if it is alive or dead, without polluting the logs.

## Installation

0. Navigate to your custom Odoo addons directory: `cd <odoo_custom_addons>`
0. Clone this project by running the following command: `git clone https://github.com/trimentor/odoo-k8s-health-check.git k8s_health_check`
0. Activate the Odoo developer mode (Settings)
0. Update Apps List (Apps)
0. Remove "Apps" from the search field
0. Search and Install the "k8s_health_check" module

## OpenShift

In the Deployment Config or your web app, configure your Readiness Probe with:
* Type: HTTP GET
* Path: /k8s_health_check/status
* Port: 8069
* Initial Delay: 10 seconds
* Timeout: 5 seconds

To check if the web app is alive/dead we can execute a command inside the container.
