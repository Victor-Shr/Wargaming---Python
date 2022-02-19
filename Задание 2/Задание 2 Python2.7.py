# coding: utf-8
# Python 2.7, адаптировал из 3.9. Вариант кольцевого буфера в котором при заполнении буфера новые данные перезаписывают старые.
# Минус такой реализации в том, что при переполнении старые данные теряются. С другой стороны данные там наиболее свежие.
# Поддерживает методы вствки данных (.enqueue), извлечения (.dequeue), просмотра след. извлекаемого элемента (.peek) без
# изменений в буфере, количество элементов в буфере (.count)

class RingBuffer(list):

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = [float('inf')] * buffer_size
        self.priority = [float('inf')] * buffer_size
        self.index = self.p_index = 0

    def enqueue(self, n): # ставим в очередь
        if self.index >= self.buffer_size:
            if float('inf') in self.buffer:
                self.index = self.buffer.index(float('inf'))
                self.p_index += 1
            else:
                self.buffer[self.priority.index(min(self.priority))] = n
                self.p_index += 1
                self.priority[self.priority.index(min(self.priority))] = self.p_index
        self.buffer[self.index] = n

        self.priority[self.index] = self.p_index
        self.index += 1
        self.p_index += 1

    def dequeue(self): # берём из очереди если есть данные
        if self.buffer.count(float('inf')) == self.buffer_size:
            print 'Error: Ring buffer empty'
            return None
        else:
            first = min(self.priority)
            dequeue = self.buffer[self.priority.index(first)]
            self.buffer[self.priority.index(min(self.priority))] = float('inf')
            self.priority[self.priority.index(min(self.priority))] = float('inf')
            print dequeue
            return None

    def peek(self): # показывает последующий выдаваемый элемент, если он есть
        if self.buffer.count(float('inf')) == self.buffer_size:
            print 'Error: Ring buffer empty'
            return None
        else:
            dequeue = self.buffer[self.priority.index(min(self.priority))]
            print dequeue
            return None

    def counter(self): # количество элементов в буфере в формате дроби, например 2/7
        inf = self.buffer.count(float('inf'))
        counter = self.buffer_size - inf
        print str(counter) + '/' + str(self.buffer_size)
        return None

    # простые данные для примера, что- то сложнее тестировал, но в пример не включил, т.к. длинно
lst = RingBuffer(7) # создаём буфер размером 7 ячеек
lst.enqueue(7) # добавим несколько данных
lst.enqueue(8)
print lst.buffer
print 'Version1 Добавили несколько данных'
print

lst.counter() # проверим заполненность буфера
print 'Проверим заполненность буфера'
print

lst.peek() # увидим следующее к выдаче значение, не меняя данные
print 'Увидим следующее к выдаче значение, не меняя данные'
print

lst.dequeue() # извлечём самое старое значение (первое в очереди)
print 'Извлечём самое старое значение (первое на выход)'
print

print lst.buffer
print 'Текущее состояние буфера'
print
print


# Python 2.7 Второй вариант кольцевого буфера в который после заполнения новые данные не попадают и выводится сообшене о заполнении.
# Отличается от 1 варианта только этим. Во второй реализации никакие данные не теряются. Взамен при заполнении буфера
# в него не попадают следующие данные пока не будет свободна хотя бы 1 ячейка.
# Поддерживает методы вствки данных (.enqueue), извлечения (.dequeue), просмотра след. извлекаемого элемента (.peek) без
# изменений в буфере, количество элементов в буфере (.count)
class RingBuffer2(list):

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = [float('inf')] * buffer_size
        self.priority = [float('inf')] * buffer_size
        self.p_index  = 0

    def enqueue(self, n): # ставим в очередь
        if float('inf') not in self.buffer:
            print 'Error: Ring buffer full'
            return None
        else:
            ind_inf = self.buffer.index(float('inf'))
            self.buffer[ind_inf] = n
            self.priority[ind_inf] = self.p_index
            self.p_index += 1

    def dequeue(self): # берём из очереди если есть данные
        if self.buffer.count(float('inf')) == self.buffer_size:
            print 'Error: Ring buffer empty'
            return None
        else:
            first = min(self.priority)
            dequeue = self.buffer[self.priority.index(first)]
            self.buffer[self.priority.index(min(self.priority))] = float('inf')
            self.priority[self.priority.index(min(self.priority))] = float('inf')
            print dequeue
            return None

    def peek(self): # показывает последующий выдаваемый элемент, если он есть
        if self.buffer.count(float('inf')) == self.buffer_size:
            print 'Error: Ring buffer empty'
            return None
        else:
            dequeue = self.buffer[self.priority.index(min(self.priority))]
            print dequeue
            return None

    def counter(self): # количество элементов в буфере в формате дроби, например 2/7
        inf = self.buffer.count(float('inf'))
        counter = self.buffer_size - inf
        print str(counter) + '/' + str(self.buffer_size)
        return None

# простые данные для примера, что- то сложнее тестировал, но в пример не включил, т.к. длинно
lst2 = RingBuffer2(7) # создаём буфер размером 7 ячеек
lst2.enqueue(7) # добавим несколько данных
lst2.enqueue(8)
print lst2.buffer
print 'Version2 Добавили несколько данных'
print

lst2.counter() # проверим заполненность буфера
print 'Проверим заполненность буфера'
print

lst2.peek() # увидим следующее к выдаче значение, не меняя данные
print 'Увидим следующее к выдаче значение, не меняя данные'
print

lst2.dequeue() # извлечём самое старое значение (первое в очереди)
print 'Извлечём самое старое значение (первое на выход)'
print

print(lst2.buffer)
print 'Текущее состояние буфера'