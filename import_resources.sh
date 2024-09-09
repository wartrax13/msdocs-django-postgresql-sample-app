#!/bin/bash

# Definir o resource group e a subscription id
RESOURCE_GROUP="django-azure-pulumi-123_group"
SUBSCRIPTION_ID="e4185ffd-c704-4d32-b91d-2eb74f9b85e7"

# Importar a Virtual Network
pulumi import azure-native:network:VirtualNetwork django-azure-pulumi-123Vnet \
/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/virtualNetworks/django-azure-pulumi-123Vnet

# Importar o App Service Plan
pulumi import azure-native:web:AppServicePlan ASP-djangoazurepulumi123group-a3f7 \
/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Web/serverFarms/ASP-djangoazurepulumi123group-a3f7

# Importar o App Service
pulumi import azure-native:web:WebApp django-azure-pulumi-123 \
/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Web/sites/django-azure-pulumi-123

# Importar o PostgreSQL Server
pulumi import azure-native:dbforpostgresql:Server django-azure-pulumi-123-server \
/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DBforPostgreSQL/flexibleServers/django-azure-pulumi-123-server

# Importar o Redis Cache
pulumi import azure-native:cache:Redis django-azure-pulumi-123-cache \
/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Cache/Redis/django-azure-pulumi-123-cache

# Importar a Private DNS Zone para Redis
pulumi import azure-native:network:PrivateZone privatelink.redis.cache.windows.net \
/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/privateDnsZones/privatelink.redis.cache.windows.net

# Importar a Private DNS Zone para PostgreSQL
pulumi import azure-native:network:PrivateZone privatelink.postgres.database.azure.com \
/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/privateDnsZones/privatelink.postgres.database.azure.com
