데이터베이스 병행제어를 위해 데이터 항목에 타임스탬프를 부여하여 직렬가능성을 보장하는 기법

- 트랜잭션에서 읽기 또는 쓰기 작업이 ==정상적으로 완료되면 타임스탬프를 기록==한다.
- 트랜잭션에서 읽기 또는 쓰기 작업을 ==수행하려고 하는 경우 타임스탬프를 확인==한다.
- 트랜잭션 수행 도중에 타임스탬프가 갱신된 경우 트랜잭션 작업을 중단한다.


[출처](https://peimsam.tistory.com/259)