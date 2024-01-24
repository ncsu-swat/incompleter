# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55094961/typeerror-unsupported-operand-types-for-nonetype-and-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def askuser(prompt):
  _l_(359791)

  userAnswer = None
  _l_(359770)
  while _n_(359771, "userAnswer", lambda: userAnswer) is None:
    _l_(359790)

    try:
      _l_(359789)

      userAnswer = _c_(359776, _n_(359772, "float", lambda: float), _c_(359775, _n_(359773, "input", lambda: input), "Enter: " + _n_(359774, "prompt", lambda: prompt) + ":"))
      _l_(359777)
      if _n_(359778, "userAnswer", lambda: userAnswer) < 0:
        _l_(359782)

        userAnswer = None
        _l_(359779)
        raise _n_(359780, "ValueError", lambda: ValueError)
        _l_(359781)
    except:
      _l_(359788)

      _c_(359784, _n_(359783, "print", lambda: print), "Number must be greater than 0.")
      _l_(359785)
      aux = _n_(359786, "userAnswer", lambda: userAnswer)
      _l_(359787)
      return aux

def calcm(male,female):
  _l_(359796)

  aux = (_n_(359792, "male", lambda: male) / _n_(359793, "male", lambda: male) + _n_(359794, "female", lambda: female)) * 100
  _l_(359795)
  return aux

def calcf(female,male):
  _l_(359801)

  aux = (_n_(359797, "female", lambda: female)/ _n_(359798, "male", lambda: male) + _n_(359799, "female", lambda: female)) * 100
  _l_(359800)
  return aux

def diplay(percent_female,percent_male):
  _l_(359810)

  _c_(359804, _n_(359802, "print", lambda: print), "Percent of Females is: ", _n_(359803, "percent_female", lambda: percent_female))
  _l_(359805)
  _c_(359808, _n_(359806, "print", lambda: print), "Percent of Males is: ", _n_(359807, "percent_male", lambda: percent_male))
  _l_(359809)

def main():
  _l_(359832)

  number_females = _c_(359812, _n_(359811, "askuser", lambda: askuser), "number of females")
  _l_(359813)
  number_males = _c_(359815, _n_(359814, "askuser", lambda: askuser), "number of males")
  _l_(359816)

  percent_female = _c_(359820, _n_(359817, "calcf", lambda: calcf), _n_(359818, "number_males", lambda: number_males),_n_(359819, "number_females", lambda: number_females))
  _l_(359821)
  percent_male = _c_(359825, _n_(359822, "calcm", lambda: calcm), _n_(359823, "number_males", lambda: number_males),_n_(359824, "number_females", lambda: number_females))
  _l_(359826)

  _c_(359830, _n_(359827, "display", lambda: display), _n_(359828, "percent_male", lambda: percent_male),_n_(359829, "percent_female", lambda: percent_female))
  _l_(359831)


_c_(359834, _n_(359833, "main", lambda: main))
_l_(359835)