__author__ = "swolfod"

from secretKeys import *
from apiadapter import structureClient

UserFields = structureClient.makeStructureClient(ACCOUNT_STRUCTURE_HOST, API_AUTH_TOKEN, "UserFields")
OrganizationFields = structureClient.makeStructureClient(ACCOUNT_STRUCTURE_HOST, API_AUTH_TOKEN, "OrganizationFields", ["brief"])
worldFields = structureClient.makeStructureClient(WORLD_STRUCTURE_HOST, API_AUTH_TOKEN, "WorldFields")
