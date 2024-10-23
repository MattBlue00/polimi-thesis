class Prompt:

  def __init__(self, prompt_id, user_message, system_message=None):
    self.id = prompt_id
    self.user_message = user_message
    self.system_message = system_message