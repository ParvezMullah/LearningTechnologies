GIL: Global Lock Interpreter. It is a mechanism or feature to lock interpreter globally so that 
only one thread can be executed by interpreter at any given time.

memory management is done by reference counting. when no reference is there for object it is garbage collected.complex
    

Memory management:
1. Reference counting
2. cyclic garbage collector or tracing 
    mark and sweep
    remove not reachable objects.


stack -> references are stored(function and local variable)
private heap -> objects are stored.
code area -> python bytecode

GC automatically calls.