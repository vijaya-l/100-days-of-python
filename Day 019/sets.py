# ets don’t have duplicate values,elements in sets are not ordered,not have index

from multiprocessing.reduction import duplicate
from ossaudiodev import SOUND_MIXER_DIGITAL1


set1 = [2, 3, "a", "b", "c", "c"]
print(SOUND_MIXER_DIGITAL1)

# remove item
# set.discard("c")
# print(set)

# join 2 sets together and it removes duplicate

set2 = {"a", "p", 3, 5}
print(set1 | set2)
