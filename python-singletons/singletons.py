"""
Singletons are objects that have exactly one instance during a programs execution.

Singletons are useful but tricky - expecially when theading is involved.
"""

import time
import uuid
import threading

class Singleton:
  def __init__(self):
    self._name = uuid.uuid4()
    self._callbacks = []
    threading.Thread(target=self.execute_callbacks, daemon=True).start()

  def add_callback(self, callback):
    self._callbacks.append(callback)

  def execute_callbacks(self):
    while True:
      print(f"From {self._name}")
      for callback in self._callbacks:
        callback()
      time.sleep(2)
      print('\n')


_SINGLETON = None

def singleton():
  global _SINGLETON
  if _SINGLETON is None:
    _SINGLETON = Singleton()
  return _SINGLETON


class AnotherClass:
  def __init__(self, state):
    singleton().add_callback(self.print_state)
    self._state = state

  def print_state(self):
    print("Hello ", self._state)


def try_to_kill():
  global _SINGLETON
  # singleton()._callbacks = []
  del _SINGLETON
  _SINGLETON = None


def main():
  # Make a class that creates the singleton.
  another_class = AnotherClass("Chris")
  
  # We have exactly 1 callback.
  print(f"{len(singleton()._callbacks)=}")
  
  # Overwrite the "another_class" variable with a new instance, but it references the same singleton.
  # another_class = AnotherClass("Not Chris")
  
  # # Oh no, now we have 2 callbacks.
  # print(f"{len(singleton()._callbacks)=}")
  
  # # Let's try to kill the singleton...
  # # First by setting the global to None
  # # Then by deleting it.
  # # Then by removing the callbacks.
  # try_to_kill()
  
  # # After killing, let's start a new class.
  # another_class = AnotherClass("Really Not Chris")
  # print(f"{len(singleton()._callbacks)=}")
  
  # try_to_kill()
  
  # Assume something is keeping the main process alive => daemon threads do not die!!!
  while True:
    time.sleep(10)

if __name__ == "__main__":
  main()