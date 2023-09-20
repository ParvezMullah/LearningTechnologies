# Implement Azure App Service web apps

## Explore Azure Web Service
1. Introduction
    Learn about the key components of azure app service and how app service can help you create, maintain, and deploy web apps more efficiently.
2. Learning objectives
    1. describe azure app service key components and value.
    2. explain how azure app service manages authentication and authorization.
    3. identify methods to control inbound and outbound traffic to your web app.
    4. deploy an app to app service using azuzre CLI commands.

### Examine Azure App Service
http based service for hosting web application, REST API and mobile backends.

#### Built-in auto scale support
resource like number of core, RAM, number of machine instances

#### Continous integration/deployment support
cicd with Azure DevOps Services, Github, Bitbucket, FTP, local Git repo.

#### Deployment slots
deploy to another slot and swap the slot.

#### App service on linux
host web app natively for supported tech stacks.

##### Limitation of App service on linux
1. not supported on shared pricing tier.
2. AWS portal shows only features that currently work for linux apps.
3. when deployed to build-in images, your code and content are allocated azure backed storage. disk latency is higher than container file system.

### Examine Azure App Service plans
App service plan defines a set of compute resources for a web app to run.
defines the following
1. Operating System.
2. Region
3. No. of VM instances
4. Size of VM instances(Small, Medium, Large)
5. Pricing tier(free, shared, basic, premium, premiumV2, premiumV3, isolated, isolatedV2)

#### Pricing Tier
1. Shared compute
    Free and shred. same azure vm for other customers. allocate CPU quota to each app.
2. Dedicated compute
    dedicated Azure VMs. only apps in the same App Service plan share the same computer resources.
3. Isolated
    dedicated VMs on deciated Azure virtual networks. it provides maximum scale-out capabilities.

### Deploy to App Service
App service supports both manual and automated deployments.

#### Auto mated deployment
supports from the following sources
1. Azure DevOps Services
    push code to DevOps service, build code in the cloud, run tests and generate release and push it to Azure Web App.
2. Github
3.Bitbucket

#### Manual deployment
1. git
    App Service web aopps feature a Git URL that you can add a remote repo. pushing to remote repo deploys your app.
2. CLI
    *webapp* up is a feature of *az* command that package your app and deploy it. it will create web app if its not already present.
3. Zip deploy
    use *curl* for similar HTTP utility to send a ZIP of you application files.
4. FTP/S: FTP or FTPS is a tradictional way of pushing your code to many hosting environments including App Service.

#### Use deployment slots
deploy on staging and then swap with prod. eliminates downtime.

### Explore Authentication and Authorisation in App Service

App service has built in authentication and authorisation.

#### Identity providers
1. Microsoft identity platform
2. facebook
3. google
4. twitter
5. Any OpenID Connect provider
6. Github

### Discover App Service networking features
by default deployment is accessible publicly.

#### Multi-tenant App service networking features




## Configure web app settings
1. Introduction
    In App Service, app settings are variables passed as environment variables to the application code.
2. Learning objectives
    1. create application settings that are bound to deployment slots.
    2. explain the options for installing SSL/TLS certificates for your app.
    3. enable diagnostic logging for your app to aid in monitoring and dubugging.
    3. create virtual app to directory mappings

### configure application settings
    app settings are the environment passed as environment variables to the application code.

    Go to -> app's management page -> Configuration > application settings

### configure general settings
in the configuration > general settings section you can configure some common settings for your app. like scale up with higher pricing tiers.

1. platform settings : lets you configure hosting platform including followings
    1. Bitness: 32 or 64-bit
    2. WebSocket protocal
    3. Always on
    4. managed pipeline version
    5. http version
    ARR affinity
2. Dubugging
3. incoming client certificates

### Configure path mapping
in the configuration > path mappings section you can configure handler mappings, and virtual application and directory mappings. different based on OS.

1. Windows aopp (uncontainerized)
    IIS handler mappings and virtual application and directories
2. Linux and containerised application
    select New Azure Storage Mount and configure your custom storage as follows
    1. Name
    2. Configuration options
    3. Storage accounts
    4. Storage type
    5. Storage container
    6. Share name
    7. Access Key
    8. Mount path

### Enable diagnostic logging
There are built in diagnostics to assist with debugging an app service app.

### Configure security certificate
you can create, upload or import private certificate or a public certificate in you app service.
applied to same resource group and region combined.

1. Create a free app service managed certificate
2. purchase an app service certificate
3. import a certificate from key vault
4. upload a privatee certificate
5. upload a public certificate

### Scale Apps in Azure app service
1. Introduction
    learn how autoscale operates in app service and how to identify autoscale factor, enable autoscale, and how to create sound autoscale conditions.
2. Learning objectives
    1. identify scenarios for which autoscaling is an appropriate solution.
    2. create autoscaling rules for a web app.
    3. monitor the effects of autoscalling.

#### Examine autoscale factors
trigger according to schedule or if system running out of sources.

#### Identify autoscale factors

##### Metrics for autoscale rules
1. CPU Percentage
2. Memory percentage
3. Disk Queue length
4. Http Queue length
5. Data in
6. Data out

#### Enable autoscaling in App Service

App Service > Choose App > Scale out

#### Explore autoscale best practices

1. Ensure the maximum and minimum vallues are different and have an adequate margin between them.
2. choose the appropriate statistic for your diagnostic metric
3. choose the thresholds carefully for all metric type
4. considerations for scaling when multiple rules are configured in a profile
5. always selecyt a safe default instance count
6. configure autoscale notification

## Explore Azure App Service deployment slots
1. Introduction
    how slot swapping operates and how to perform a swap. learn how to route traffic to differnt slots manually and automatically.
2. Learning objectives
    1. describe the benefits of using deployment slots
    2. understand how slot swapping operates in app service.
    3. perform manual swaps and enable autoswap.
    route traffic manually and automatically

### Explore staging environment
    deploy on staging then swap with the production.
### Examine slot swapping
 to ensure no downtime app service does following during swapping
1. Apply the following setings from the target slot.
    1. slot specific app settings and connections
    2. continous deployment settings
    3. app service authentication settings
2. Wait for every instance in the resource slot ton complate its restart. if failed then revert changes.
3. if local cache is enabled, trigger local cache initialization by making http request.
4. if autoswap is enabled with custom warm-up, trigger applicaation initiation by making an http request to the application root.
5. if all instances on the sources slot are warmed up successfully, then swap and switch routing rules.
6. now the sources slot has the preswap app previously in the target slot, perfrom the same operating by applying all the settings and restart instances.

### Swap deployment slots
1. Manually swapping deployment slots
    1. go to app's deployment slots page and select swap.
    2. select desired source and target slots.
    
2. Swap with preview
before you swap validate if app runs with swapped settings.

3. Configure autoswap
    everytime you code it will autoswap.

#### Roll back and monitor swap
    if anything goes wrong then restore the slot.

### Route traffic in app service
by default all requests goes to http://<appname>.azurewebsites.net. you cna route to another portion for testing or phasewise upgrades.

#### Route production traffic automatically
    1. go to app's resource page and select deployment
    2. in the traffic % collumn of the slot make changes.

#### Route production traffic manually
 useful for beta release.
 x-ms-routing-name


 # Implement Azure functions
 1. Introduction
    lets you develop serverless applications on azure. dont need to worry about whole application or infrastructure.
 2. Learning Objectives
    1. Explain function differences between azure function, azure logic app and webjobs
    2. describe azure function hosting plan options
    3. describe how azure functions scale to meet business needs.

## Explore Azure Functions

### Discover Azure Functions
Azure function supports triggers which are ways to start execution of your code and bindings.
    Azure logic apps is a serverless workflow integration platform.
    webjobs is a code first integration.

### Compare Azure function hosting options
following plans
1. consumption plan (10min duration, 100 instance)
2. premium plan (unlimited, 20-100 instance)
3. dedicated plan (unlimited, 10-20 instance)
4. App serevice environment (100 instance)
5. Kubernetes(Director or Azure Arc) varies by clusture.

### Scale Azure functions
1.5 GB and one CPU per function.

#### Runtime scalling
    scale controller component is used to determine scale in and scale out. if using azure queue storage trigger it scales based on queue length and age of oldest message queue.
#### Scaling behaviors
    1. Maximum instances
        a single function can scale out to 200 instances.
    2. New instance rate
        for http trigger new instances are allocated at most once per second, for non http its once every 30 second
#### Limit scale-out
    define maximum number of instances an app used to scale out.
    functionAppScaleLimit value to setting.


## Develop Azure functions
1. Introduction
    Functions share a few core technical concepts and components
2. Learning objectives
    1. Explain the key components of a function and how they can structured.
    2. create triggers and bindings to control when a function runs and where the output is directed.
    3. connect a function to services in Azure.
    4. create a function by using VSCode and the Azure functions core tools

### Explore Azure function development
function contain code and configuration.
function.json file container trigger, bindings and other config settings.

### Create triggers and bindings
triggers cause a function to run.
{
    "dataType": "binary",
    "type": "httpTrigger",
    "name": "req",
    "direction": "in"
}

### Connect function to azure services
your function project references connection information by name from its configuration provider.

#### configure an identity based connection
some connections in azure function are configured to use an identity instead of a secret.

#### Grant permission to identity
whatever identity is being used must have permissions to perform the intended actions.

### Excercise: create in VS Code
create a function app