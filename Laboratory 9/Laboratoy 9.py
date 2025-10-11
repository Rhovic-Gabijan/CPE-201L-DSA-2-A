import time

def CreateQueue():
    queue = []
    return queue

def Enqueue(queue, item):
    queue.append(item)
    print("Enqueued Element: ", item)
    
def isEmpty(queue):
    return len(queue) == 0
    
def Dequeue(queue):
    if isEmpty(queue):
        return "The queue is empty"
    return queue.pop(0)

queue = CreateQueue()

while True:
    element = input("Enter Elements to Enqueue: (Type 'exit' to stop): ").strip()
    if element == 'exit':
        break
    Enqueue(queue, element)
    
print("\nElement in the Queue:")
for i in queue:
    print(i)

print("")   
x = ["E",[0.1], 
     "x",[0.2], 
     "i",[0.2], 
     "t",[0.2], 
     "i",[0.2], 
     "n",[0.2], 
     "g",[0.2], 
     ".",[0.2], 
     ".",[0.2], 
     ".",[0.2]]
time.sleep(1)
for i in x:
    if isinstance(i, list):
        time.sleep(i[0])
    else:
        print(i, end='', flush=True)