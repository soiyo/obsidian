- 한 릴레이션을 구성하는 **==모든 도메인이 원자값(Atomic Value)만==으로 구성되도록 하는 정규형**

ex) 한 사람의 이름은 성과 이름으로 구성되어 있다. 만약 업무상으로 성과 이름을 나눠서 저장해야한다면 '임경호' 라는 데이터는 원자값을 만족하지 않는 것이다. '임' 과 '경호' 를 따로 저장해야 원자값을 만족할 수 있다.

ex2) A직원의 생일은 19910617이다 여기서 생년,월,일 모두 포함되어 있는 데이터 값이다. 만약 업무상으로 생년,월,일을 모두 합친 것을 하나의 원자값으로 봐도 무방하다면! 19910617 이란 데이터는 원자값을 만족하는 것이다. 
즉, 원자값은 업무적인 의미로 데이터 값을 더 쪼갤수도 안 쪼갤수도 있는 것이다. 모든 시스템의 절대적인 기준은 없다. 각 시스템에 적합한 단위로 원자값이 정해진다.

ex3)
![[Pasted image 20231202182539.png]]
	두번째 테이블에서의 문제점
	1. 어떤 고객이 전화번호를 가지고 있는지, 어떤 고객들끼리 같은 전화번호를 공유하는지 질의에 답하기 어려움
	2. 고객-전화번호의 유일성을 확보하기 어려움 (789고객이 실수로 Tel1, Tel2가 동일하면 유일성 깨짐)
	3. 전화번후 갯수 3개까지만 입력 가능
	**해결책은? : 제 1 정규화를 통한 테이블 쪼개기**![[Pasted image 20231202182856.png]]


[출처](https://limkydev.tistory.com/162)