import pulumi
import pulumi_azure_native as azure_native

# Grupo de recursos
resource_group = azure_native.resources.ResourceGroup("django-azure-pulumi-123_group", location="brazilsouth")

# Private DNS Zones
private_dns_redis = azure_native.network.PrivateZone(
    "privatelink.redis.cache.windows.net",
    resource_group_name=resource_group.name,
    location="global",
    private_zone_name="privatelink.redis.cache.windows.net"
)

private_dns_postgres = azure_native.network.PrivateZone(
    "privatelink.postgres.database.azure.com",
    resource_group_name=resource_group.name,
    location="global",
    private_zone_name="privatelink.postgres.database.azure.com"
)

# Virtual Network
vnet = azure_native.network.VirtualNetwork(
    "django-azure-pulumi-123Vnet",
    resource_group_name=resource_group.name,
    location="brazilsouth",
    address_space=azure_native.network.AddressSpaceArgs(
        address_prefixes=["10.0.0.0/16"]
    )
)

# Redis Cache
redis_cache = azure_native.cache.Redis(
    "django-azure-pulumi-123-cache",
    resource_group_name=resource_group.name,
    location="brazilsouth",
    sku=azure_native.cache.SkuArgs(
        name="Standard",
        family="C",
        capacity=1
    )
)

# App Service Plan
app_service_plan = azure_native.web.AppServicePlan(
    "ASP-djangoazurepulumi123group-a3f7",
    resource_group_name=resource_group.name,
    location="brazilsouth",
    sku=azure_native.web.SkuDescriptionArgs(
        tier="Basic",
        name="B1"
    )
)

# Web App (App Service)
web_app = azure_native.web.WebApp(
    "django-azure-pulumi-123",
    resource_group_name=resource_group.name,
    server_farm_id=app_service_plan.id,
    site_config=azure_native.web.SiteConfigArgs(
        linux_fx_version="PYTHON|3.10"
    )
)

# PostgreSQL Server
postgres_server = azure_native.dbforpostgresql.FlexibleServer(
    "django-azure-pulumi-123-server",
    resource_group_name=resource_group.name,
    location="brazilsouth",
    sku=azure_native.dbforpostgresql.SkuArgs(
        name="Standard_B2ms",
        tier="Burstable",
    ),
    storage=azure_native.dbforpostgresql.StorageArgs(storage_size_gb=32),
    backup=azure_native.dbforpostgresql.BackupArgs(
        backup_retention_days=7
    )
)

# Private Endpoints for Redis and Postgres
redis_private_endpoint = azure_native.network.PrivateEndpoint(
    "django-azure-pulumi-123-cache-privateEndpoint",
    resource_group_name=resource_group.name,
    subnet=azure_native.network.SubnetArgs(id=vnet.id),
    private_link_service_connections=[azure_native.network.PrivateLinkServiceConnectionArgs(
        private_link_service_id=redis_cache.id,
        group_ids=["redisCache"]
    )]
)

postgres_private_endpoint = azure_native.network.PrivateEndpoint(
    "django-azure-pulumi-123-server-privateEndpoint",
    resource_group_name=resource_group.name,
    subnet=azure_native.network.SubnetArgs(id=vnet.id),
    private_link_service_connections=[azure_native.network.PrivateLinkServiceConnectionArgs(
        private_link_service_id=postgres_server.id,
        group_ids=["postgresqlServer"]
    )]
)

# Managed Identity
managed_identity = azure_native.managedidentity.UserAssignedIdentity(
    "django-azure-pul-id-9dc1",
    resource_group_name=resource_group.name,
    location="brazilsouth"
)

# Exports (opcional, para visualizar recursos)
pulumi.export("resource_group_name", resource_group.name)
pulumi.export("app_service_url", web_app.default_host_name)
pulumi.export("postgres_server", postgres_server.name)
pulumi.export("redis_cache_host", redis_cache.host_name)
