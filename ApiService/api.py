__author__ = "swolfod"

from secretKeys import *
from apiadapter import apiClient

accountApi = apiClient.makeApiClient(ACCOUNT_API_HOST, API_AUTH_TOKEN, "account", [
    "emailAuthorize",
    "phoneAuthorize",
    "authorizeUser",
    "accountAccesses",
    "read",
    "update",
    "create",
    "delete"
])

organizationApi = apiClient.makeApiClient(ACCOUNT_API_HOST, API_AUTH_TOKEN, "organization")
organizationMemberApi = apiClient.makeApiClient(ACCOUNT_API_HOST, API_AUTH_TOKEN, "organizationMember")

resetPasswordApi = apiClient.makeApiClient(ACCOUNT_API_HOST, API_AUTH_TOKEN, "resetPassword", [
    "createResetToken",
    "checkResetToken",
    "resetPassword"
])


poiApi = apiClient.makeApiClient(CORE_API_HOST, API_AUTH_TOKEN, "poi", ['read'])
destinationApi = apiClient.makeApiClient(CORE_API_HOST, API_AUTH_TOKEN, "destination", ['read'])
worldApi = apiClient.makeApiClient(WORLD_API_HOST, API_AUTH_TOKEN, "world", ['read', 'create'])
areaApi = apiClient.makeApiClient(WORLD_API_HOST, API_AUTH_TOKEN, "area")
