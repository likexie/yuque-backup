from abc import ABCMeta, abstractmethod

class Users(metaclass=ABCMeta):
    
    @abstractmethod
    def get_user_info(self, name)->dict:
        '''
        获取指定用户信息
        '''
        pass


class Common(metaclass=ABCMeta):

    @abstractmethod
    def get_list(self, offset, limit):
        '''
        获取列表信息
        '''
        pass


    @abstractmethod
    def get_info_by_id(self,id):
        '''
        获取详细信息
        '''
        pass