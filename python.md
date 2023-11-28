- 언더바
for _ in range(3):
    print("ha")

for i in range(3):
    print("ha")

출처: https://g0pher.tistory.com/131 [고퍼:티스토리]

_ 코드에서는 i를 사용하지 않으면서 반복(Iteration)한다. 그렇기 때문에 따로 i를 선언해주지 않아도 된다.

- for in vs. for range
    - for in list : 순회할 리스트가 정해져 있을 때 사용
    - for in range : 순회할 횟수가 정해져 있을 때 사용

- range() 함수
    range([start,] stop [,step])는 for문과 함께 자주 사용되는 함수이다. 이 함수는 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴한다.

```
#인수 1개 - 시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.

>>> list(range(5))
[0, 1, 2, 3, 4]

# 인수 2개 - 입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다.
# 단, 끝 숫자는 해당 범위에 포함되지 않는다는 것에 주의하자.
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

# 인수 3개 - 세 번째 인수는 숫자 사이의 거리를 말한다.
>>> range(1, 10, 3)
[1, 4, 7]
>>> range(20, 10, -2)
[20, 18, 16, 14, 12]
```

- len
- len(s)은 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수이다.

```
>>> len("python")
6
>>> len([1,2,3])
3
>>> len((1, 'a'))
2
```

```
rainbow=["빨","주","노","초","파","남","보"]
for i in range(len(rainbow)):
	color = rainbow[i]
	print('{}번째 색은 {}'.format(i+1,color))
```

- enumerate 함수

- 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
- enumerate는 “열거하다”라는 뜻이다. 이 함수는 **순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴**한다.
- 보통 enumerate 함수는 아래 예제처럼 for문과 함께 자주 사용된다.

```
>>> for i, name in enumerate(['body', 'foo', 'bar']):
...     print(i, name)
...
0 body
1 foo
2 bar
```

for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 enumerate 함수를 사용하면 매우 유용하다.

```
names = ['철수', '영희', '영수']
for i, name in enumerate(names):
  print('{}번: {}'.format(i + 1, name))
```

https://wayhome25.github.io/python/2017/02/24/py-07-for-loop/

- 문자열 포맷팅
- 
```python
first_name = "John"

print("Hello {}, hope you're well!".format(first_name))

#output
#Hello John, hope you're well!
```
```python
first_name = "John"
last_name = "Doe"

print("Hello {} {}, hope you're well!".format(first_name,last_name))

#output
#Hello John Doe, hope you're well!
```

https://www.freecodecamp.org/korean/news/python-print-string-variable/

 - time 함수

import time
time.time()
1444532446.467043

time은 현재 시각을 반환하는 함수인데 1970년 1월 1일 0시 0분 0초를 기준으로 초 단위로 지난 시간을 알려줍니다.

time.ctime()
'Sun Oct 11 12:00:50 2015'

type( _ )
<class 'str'>

IDLE에서 `_`는 가장 최근의 반환값을 바인딩하고 있는 변수입니다.

cur_time = time.ctime() 
print(cur_time.split(' ')[-1]) 
2015

time.ctime 함수의 반환값을 cur_time이라는 변수가 바인딩하게 한 후 문자열 객체가 제공하는 split이라는 메서드를 사용해 공백을 기준으로 문자열을 분리했습니다. 분리된 문자열 중 맨 마지막에 존재하는 원소를 화면에 출력하면 연도가 화면에 출력됩니다.


파이썬 모듈에는 여러 기능을 수행하는 함수와 변수가 있을 수 있는데 모듈 안에 어떤 함수나 변수가 있는지 어떻게 확인할 수 있을까요? 가장 간단한 방법은 다음과 같이 dir 함수를 사용하는 것입니다. 임포트된 모듈에 대해 모듈명을 사용해 dir 내장 함수를 호출하면 해당 모듈의 구성 요소를 확인할 수 있습니다.

```py
>>> import time
>>> dir(time)
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'perf_counter', 'process_time', 'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'timezone', 'tzname']
>>>
```

다음 코드는 time 모듈과 random 모듈을 임포트한 후 해당 모듈의 위치를 확인하는 코드입니다. time 모듈은 내장 모듈이기 때문에 해당 모듈의 위치가 따로 출력되지는 않지만 random 모듈은 해당 모듈이 위치하는 경로가 출력되는 것을 볼 수 있습니다. 

```py
>>> import time
>>> time
<module 'time' (built-in)>
>>> import random
>>> random
<module 'random' from 'C:\\Anaconda3\\lib\\random.py'>
>>>
```


https://wikidocs.net/3140


- 스와프
리스트의 0번째 요소와 3번째 요소의 값을 변경하고 싶다. 임시변수를 사용하지 않고도 요소의 자리 변경이 가능하다.
array = [1,2,3,4,5]
array[0], array[3] = array[3], array[0] print(array) #[4,2,3,1,5]

- sort
파이썬 리스트에는 리스트를 제자리에서(in-place) 수정하는 내장 [`list.sort()`](https://docs.python.org/ko/3/library/stdtypes.html#list.sort "list.sort") 메서드가 있습니다. 또한, 이터러블로부터 새로운 정렬된 리스트를 만드는 [`sorted()`](https://docs.python.org/ko/3/library/functions.html#sorted "sorted") 내장 함수가 있습니다.
- sort()
sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]

a = [5, 2, 3, 1, 4]
a.sort()
a
[1, 2, 3, 4, 5]

[`list.sort()`](https://docs.python.org/ko/3/library/stdtypes.html#list.sort "list.sort") 메서드가 리스트에게만 정의된다는 것입니다. 이와 달리, [`sorted()`](https://docs.python.org/ko/3/library/functions.html#sorted "sorted") 함수는 모든 이터러블을 받아들입니다.

sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]

https://docs.python.org/ko/3/howto/sorting.html

- 몫
3//2 
1  
412 // 4 
103

- 나머지
2%3
3

- **몫과 나머지를 한번에 연산**할 수 있는 **divmod**함수

```
>>>> a, b = divmod(2, 3)
>>>> a
0
>>>> b
2
```
몫과 나머지를 할당받을 변수 a와 b를 지정해주면 몫에 해당하는 값을 a에, 나머지에 해당하는 값을 b에 넣어줍니다. 나중에 변수 a 와 b를 각각 호출해보면 계산 결과로서 몫과 나머지가 들어가 있는 것을 알 수 있습니다. divmod에는 정수형으로 입력하면 정수형 몫과 나머지가 입력이 되고, 실수형으로 입력하면 실수형 몫과 나머지를 리턴합니다.  당연한 이야기지만,  divmod는 나머지 연산이 아닌 몫과 나머지 값만 돌려주기 때문에 나머지 연산을 하려면 '/' 연산자를 이용해야 합니다.

- 나누기 연산
**실수형(float)으로 리턴**
2/3 
0.6666666666666666

https://cross-the-line.tistory.com/m/18

- 할당 연산자

|    | 
|---|---|---|
|=|왼쪽 변수에 오른쪽 값을 할당한다.|a = b 는 <br><br>a = b 를 의미함|
|+=|왼쪽 변수에 오른쪽 값을 더하고 그 결과를 왼쪽 변수에 할당한다.|a += b 는<br><br>a = a+b 를 의미함|
|-=|왼쪽 변수에 오른쪽 값을 빼고 그 결과를 왼쪽 변수에 할당한다.|a -= b 는<br><br>a = a-b 를 의미함|
|*=|왼쪽 변수에 오른쪽 값을 곱하고 그 결과를 왼쪽 변수에 할당한다.|a *= b 는<br><br>a = a*b 를 의미함|
|/=|왼쪽 변수에 오른쪽 값을 나누고 그 결과를 왼쪽 변수에 할당한다.|a /= b는<br><br>a = a/b 를 의미함|
|%=|왼쪽 변수에 오른쪽 값을 나눈 후 그 나머지를 왼쪽 변수에 할당한다.|a %= b 는<br><br>a = a%b 를 의미함|
|//=|왼쪽 변수에 오른쪽 값을 나눈 후 그 몫을 왼쪽 변수에 할당한다.|a //= b 는<br><br>a = a//b 를 의미함|
|**=|왼쪽 변수에 오른쪽 값을 제곱하고 그 결과를 왼쪽 변수에 할당한다.|a **= b 는<br><br>a = a**b 를 의미함|


https://corytips.tistory.com/m/162


- map

**map(function, iterable)**

map 함수의 모양은 위와 같습니다.  
**첫 번째 매개변수로는 함수**가 오고  
**두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)** 이 옵니다.

**map 함수의 반환 값은** map객체 이기 때문에 해당 자료형을 **list 혹은 tuple로 형 변환시켜주어야** 합니다.  

함수의 동작은 **두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을** **첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는** 함수입니다.

**map(적용시킬 함수, 적용할 값들)** 이런 식인 거죠.  
예를 들어 첫 번째 인자가 값에 +1을 더해주는 함수라고 하고 두번째 인자에 [1, 2, 3, 4, 5] 라는 리스트를 집어넣으면

함수의 모양은 아래와 같고   
**map( 값에 +1 을 더해주는 함수, [1,2,3,4,5])**   
함수의 반환을 list(. )로 감싸주면  
**[2,3,4,5,6]** 이 되는 함수입니다.

```python
import math  # math.ceil 함수 사용
#예제1) 리스트의 값을 정수 타입으로 변환
result1 = list(map(int, [1.1, 2.2, 3.3, 4.4, 5.5]))
print(f'map(int, 리스트) : {result1}')

#예제2) 리스트 값 제곱
def func_pow(x):
    return pow(x, 5)  # x 의 5 제곱을 반환

result2 = list(map(func_pow, [1, 2, 3, 4, 5]))
print(f'map(func_pow, 리스트) : {result2}')

#예제3) 리스트 값 소수점 올림
result3 = list(map(math.ceil, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]))
print(f'map(func_ceil, 리스트) : {result3}')
```

출처: [https://blockdmask.tistory.com/531](https://blockdmask.tistory.com/531) [개발자 지망생:티스토리]
(https://dotiromoook.tistory.com/28)

