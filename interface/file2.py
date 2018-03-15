import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1,self).__init__('Robot')

        #Definition of the forms fields
        self._currency     = ControlText('Currency pair')
        self._middlename    = ControlText('Middle name')
        self._lastname      = ControlText('Lastname name')
        self._fullname      = ControlText('Full name')
        self._button        = ControlButton('Press this button')


#Execute the application
if __name__ == "__main__":
    pyforms.start_app( SimpleExample1 )