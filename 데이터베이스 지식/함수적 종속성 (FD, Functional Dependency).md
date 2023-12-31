[[#완전 함수적 종속(Full Functional Dependency)]]
[[#부분 함수적 종속(Partial Functional Dependency)]]
[[#이행적 함수 종속(Transitive Functional Dependecy)]]

함수적 종속이란 어떤 릴레이션 R이 있을때 X와 Y를 각각 속성의 부분집합이라고 가정하자.
==X의 값을 알면 Y의 값을 바로 식별할 수 있고, X의 값에 Y의 값이 달라질 때, **Y는 X에 함수적 종속**==이라고 한다. 이 경우 **X를 결정자**, **Y를 종속자**라고 한다.

![[Pasted image 20231202185327.png]]
학번 -> 이름, 나이, 성별 속성 식별 가능
* 학번에 따라 위의 값 달라짐
* 이름, 나이, 성별 속성은 학번에 함수적 종속관계임
전공코드 -> 전공속성(전공명 ...)

#### 완전 함수적 종속(Full Functional Dependency)

^21550c

완전 함수적 종속에서 ==종속자는 기본키에만 종속==되어야 한다.
==기본키가 여러 속성으로 구성==되어 있을 경우(복합키일 경우) 종속자는 모든 기본키의 부분집합에 종속되어야 한다. (C종속자가 A기본키에는 종속되는데 B기본키에는 종속되지 않으면 C는 완전 함수적 종속을 만족하지 않는다.)

![[Pasted image 20231202185535.png]]
위 테이블
- 기본키 : 회원번호
- 회원번호 알아야 -> 이름, 나이, 거주지역 식별 가능
	따라서 이름, 나이, 거주지역은 회원번호에 완전 함수 종속된 관계임

아래 테이블
* 기본키 : 고객ID, 상품코드 -> 이 두개 알아야 수량 속성 식별 가능
	따라서 수량은 완전함수종속된 관계임

#### 부분 함수적 종속(Partial Functional Dependency)

부분 함수적 종속이란, ==종속자가 릴레이션의 기본키가 아닌 다른 속성에 종속==되거나, 기본키가 여러 속성으로 구성되어 있을경우==(복합키일경우) 기본키를 구성하는 속성 중 일부에만 종속==되는 경우이다.
![[Pasted image 20231202190116.png]]
주문상품은 제품코드만 알아도 식별 가능하다.
주문상품 속성은 기본키에 부분 함수 종속된 관계이다.

#### 이행적 함수 종속(Transitive Functional Dependecy)

릴레이션에서 X, Y, Z라는 3 개의 속성이 있을 때 X→Y, Y→Z 이란 종속 관계가 있을 경우, ==X→Z가 성립될 때 이행적 함수 종속==이라고 한다. 즉, X를 알면 Y를 알고 그를 통해 Z를 알 수 있는 경우를 말한다.

![[Pasted image 20231202190850.png]]



[출처](https://dodo000.tistory.com/20#:~:text=%ED%95%A8%EC%88%98%EC%A0%81%20%EC%A2%85%EC%86%8D%EC%9D%B4%EB%9E%80%20%EC%96%B4%EB%96%A4,%EB%A5%BC%20%EC%A2%85%EC%86%8D%EC%9E%90%EB%9D%BC%EA%B3%A0%20%ED%95%A9%EB%8B%88%EB%8B%A4.)