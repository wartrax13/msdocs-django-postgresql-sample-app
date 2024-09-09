import pulumi
import pulumi_azure_native as azure_native

# Subscription ID e Resource Group
SUBSCRIPTION_ID = "e4185ffd-c704-4d32-b91d-2eb74f9b85e7"
RESOURCE_GROUP = "django-azure-pulumi-123_group"

# Importar Virtual Network
vnet = azure_native.network.VirtualNetwork.get("django-azure-pulumi-123Vnet", 
    f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.Network/virtualNetworks/django-azure-pulumi-123Vnet"
)

# Importar App Service Plan
app_service_plan = azure_native.web.AppServicePlan.get("ASP-djangoazurepulumi123group-a3f7", 
    f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.Web/serverFarms/ASP-djangoazurepulumi123group-a3f7"
)

# Importar App Service
app_service = azure_native.web.WebApp.get("django-azure-pulumi-123", 
    f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.Web/sites/django-azure-pulumi-123"
)

# Importar PostgreSQL Server
postgresql_server = azure_native.dbforpostgresql.Server.get("django-azure-pulumi-123-server", 
    f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.DBforPostgreSQL/flexibleServers/django-azure-pulumi-123-server"
)

# Importar Redis Cache
redis_cache = azure_native.cache.Redis.get("django-azure-pulumi-123-cache", 
    f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.Cache/Redis/django-azure-pulumi-123-cache"
)

# Importar Private DNS Zone para Redis
redis_dns = azure_native.network.PrivateZone.get("privatelink.redis.cache.windows.net", 
    f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.Network/privateDnsZones/privatelink.redis.cache.windows.net"
)

# Importar Private DNS Zone para PostgreSQL
postgres_dns = azure_native.network.PrivateZone.get("privatelink.postgres.database.azure.com", 
    f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.Network/privateDnsZones/privatelink.postgres.database.azure.com"
)

# Exportar saídas para facilitar uso em outras partes do código
pulumi.export("app_service", app_service.name)
pulumi.export("redis_cache", redis_cache.name)
pulumi.export("postgresql_server", postgresql_server.name)
pulumi.export("vnet", vnet.name)