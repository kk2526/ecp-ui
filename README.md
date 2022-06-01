# ECP Support UI

- Interactive interface which displays all the Kubernetes objects which are not being used (referred) to any deployment.
- Developer can multi select their objects from the UI and update them accordinly. Below are three options provided to Developer/Support persons:

   ```Can be deleted```  Confirms that objects can be permanently be deleted

   ```In-Review``` Being reviewed. [ Will be removed if not confirmed within 20 days ]

   ```Keep-It``` Temporarily not being used. [ Please email our team with appropriate reason]  
 
![Output sample](https://github.com/kk2526/ecp-ui/raw/demo/ecp-ui.gif)

## K8s Unused Objects

### k8s_unused-objs.py

Above script loops through all the k8s objects which are currently not being used and pushed the objects into postgres database running as a container in kubernetes.

#### Selection Criteria
 - Secret -> If the secret is not mounted on any running pod via env variable or as volume
 - ConfigMap -> If ConfigMap is not mounted on any running pod via env variable or as volume
 - PVC -> Is PVC is not mounted on any running pod
 - Services -> If services do not any endpoint
 - ServiceAccount -> If no running pod use that service account
 - Ingress -> If ingress pointing to any services which either do not exist or do not have any endpoint
 - RoleBinding -> If RoleBindding to any Services account which does not exist or that Services account is not used by any running pod.
 - Deployment -> If deployment have zero replica.
 - StateFullset -> If StateFullset have zero replica.

### ui.py

Built on python flask. Uses java script and html

Project Organization
------------

    ├ README.md            <- The top-level README file
    |
    ├ data
    │   ├ sampledata_unused-objects.json  <- sample data of unused objects
    │  
    ├ demo                 <- Contains any demos related to the projects.
    │   └ ecp-ui           <- Quick demo for initial ui
    │
    └ ui-backend           <- Backend source
        │
        ├ static           <- Static css and js files
        │   └ css
        |   └ js 
        │
        ├ template         <- HTML Files
        │   └ index.html
        |   └ base.html
        │
        ├ config           <- Configuration files for backend database
        │   │                 
        │   ├ database.ini    Database details
        │   └ config.py       Read db details
        │
        ├ k8s_unused-objs.py <- Scripts to get all unused data and insert them into databse
        |
        ├ ui.py              <- Script for UI


## Upcoming changes:
1. Create docker image for this
2. Add functionality to select multiple clusters
  
