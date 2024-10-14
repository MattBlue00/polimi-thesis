class Prompt:

  def __init__(self, prompt_id, json_object):
    self.id = prompt_id
    self.user_message = json_object.get("user")
    self.system_message = json_object.get("system")