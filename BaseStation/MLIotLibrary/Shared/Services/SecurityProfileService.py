
from ..Schema import SecurityProfile

class SecurityProfileService:
    def get_security_profile_by_parent_id(self, id):
        return SecurityProfile.get_security_profile_by_parent_id(id)

    def get_security_profile_config_by_parent_id(self, id):
        return SecurityProfile.get_config(self.get_security_profile_by_parent_id(id))