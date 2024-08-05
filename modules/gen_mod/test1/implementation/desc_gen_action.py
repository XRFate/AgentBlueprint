from data_module.data_interface import DataInterface, overwrite_descriptor, DataListInterface

class Action(DataInterface):
    def __init__(self, data: dict = None):
        default_prop = {"action_description": None,"duration": None,"start_time": None,"end_time": None,}
        default_prop.update(data)
        super().__init__(default_prop)
        self.description_overwrite()
    def description_overwrite(self):
        #@overwrite_descriptor #add this decorator at the overwriting properties
        #def action_description(self):
        #    return f" Action NEW Description is : {self.get_data_str('action_description')}"
        # action_description(self)
        return
    def get_property_from_index(self,index: int):
        if index == 0:
            return self.default(),self.default_str()
        elif index == 1:
            return self.default(),self.action_description
        elif index == 2:
            return self.default(),self.duration
        elif index == 3:
            return self.default(),self.start_time
        elif index == 4:
            return self.default(),self.end_time

class ActionList(DataListInterface):
    def __init__(self, data: list):
        super().__init__(data)
