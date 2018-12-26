__author__ = "HanHui"

from utilities import classproperty


class SupplierFields:
    @classproperty
    def brief(self):
        return {
            "id": True,
            "name": True,
            "phone": True,
            "wechat": True,
            "location": True,
            "premium": True,
            "qualifications": True
        }
