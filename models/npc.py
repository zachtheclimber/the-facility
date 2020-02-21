class NPC():

    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._conversation = None

    def set_conversation(self, words):
        self._conversation = words

    def describe(self):
        print(f"{self._name} stands before you.")
        print(self._description)

    def talk(self):
        if self._conversation:
            print(f"{self._name} says: {self._conversation}")
        else:
            print(f"{self._name} doesn't want to talk to you.")

    def fight(self, combat_item):
        print(f"You raise your {combat_item}, but {self._name} backs away.")
        return True