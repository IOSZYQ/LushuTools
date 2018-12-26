__author__ = "swolfod"

from utilities import classproperty


class UserFields:

    @classproperty
    def brief(cls):
        return {
            "id"        : True,
            "name"      : True,
            "avatar"    : True,
        }


    @classproperty
    def full(cls):
        fields = cls.brief
        fields.update({
            "email"         : True,
            "phone"         : True,
            "sex"           : True,
            "birthday"      : True
        })

        return fields


class OrganizationFields:

    @classproperty
    def brief(cls):
        return {
            "id"            : True,
            "name"          : True,
            "logo"          : True,
            "serial"        : True,
            "description"   : True,
            "solo"          : True,
            "leader"        : UserFields.brief
        }
