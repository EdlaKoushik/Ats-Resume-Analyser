from backend.core.role_templates import ROLE_TEMPLATES

def get_role_template(role:str)->dict |None:
    """
    Safe accessor  for role templates
    """
    
    return ROLE_TEMPLATES.get(role)