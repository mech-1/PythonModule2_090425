# "Генерация простых множителей числа"
# Напишите генераторную функцию, которая принимает целое число n и генерирует его простые множители по одному.
# (Например, для 12 генератор должен выдавать 2, 2, 3
def primfacs(n: int) -> int:                     
    i = 2                                       
    while i * i <= n:                           
        while n % i == 0:                       
            n = n // i                          
            yield i                             
        i += 1                                  
    if n > 1:                                   
        yield n                                 
                                                
                                                
if __name__ == '__main__':                      
    print(list(primfacs(15)))                   
    print(list(primfacs(12)))                   
    assert (list(primfacs(15))) == [3, 5]       
    assert (list(primfacs(12))) == [2, 2, 3]    
