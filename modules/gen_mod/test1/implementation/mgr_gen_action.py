from data_module.agent_interface import AgentInterface
from data_module.context_interface import QueryContext
from data_module.data_interface import DataInterface, DataListInterface
from data_module.manager_interface import BaseDataManager
from desc_gen_action import Action, ActionList

class ActionManager(BaseDataManager):
    def set_service_response(self, response, ctx: QueryContext):
        if isinstance(response, (Action, ActionList)):
            ctx.set_response(response)
        else:
            raise ValueError("Response must be an instance of DataInterface or DataListInterface")

    def get_descriptor(self, desc_index:int, d:AgentInterface, ctx:QueryContext) -> DataInterface or DataListInterface:
        if desc_index == 0:
            return self._single(ctx)
        elif desc_index == 1:
            return self._list(ctx)
        elif desc_index == 20:
            return self._current(ctx)
        else:
            raise ValueError("Invalid Descriptor Index")

    def _single(self, ctx: QueryContext) -> DataInterface or DataListInterface:
        #TODO: implement me, this is where connects to a datasource, could be a database or a service
        raise NotImplementedError

    def _list(self, ctx: QueryContext) -> DataInterface or DataListInterface:
        #TODO: implement me, this is where connects to a datasource, could be a database or a service
        raise NotImplementedError

    def _current(self, ctx: QueryContext) -> DataInterface or DataListInterface:
        #TODO: implement me, this is where connects to a datasource, could be a database or a service
        raise NotImplementedError

