-- SQLite

-- 가장 나이가 작은 사람의 수 - 정렬과 그룹화를 통해서만으로도 추출 가능
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;

-- age  COUNT(*)
-- ---  --------
-- 15   39

-- 함수 이용
-- 1) 가장 작은 값 확인
SELECT MIN(age)
FROM users;

-- MIN(age)
-- --------
-- 15

-- 2) 1)에서 얻은 가장 작은 값으로 카운팅
SELECT COUNT(*)
FROM users
WHERE age = 15;

-- COUNT(*)
-- --------
-- 39

-- 서브쿼리로도 확인 가능
SELECT COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);

-- COUNT(*)
-- --------
-- 39


-- 평균 계좌 잔고보다 잔고가 높은 사람의 수
SELECT AVG(balance) FROM users;

SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

-- COUNT(*)
-- --------
-- 222
-- sqlit


-- 유은정과 같은 지역에 사는 사람의 수?
SELECT country
FROM users
WHERE last_name || first_name = '유은정';

-- country
-- -------
-- 강원도

SELECT COUNT(*)
FROM users
WHERE country = (SELECT country FROM users WHERE last_name || first_name = '유은정');

-- COUNT(*)
-- --------
-- 101

-- 전체 인원 수, 계좌 잔고 평균과 나이 평균?
-- 함수를 이용한다면 하기와 같음
SELECT COUNT(*), AVG(balance), AVG(age)
FROM users;

-- COUNT(*)  AVG(balance)  AVG(age)
-- --------  ------------  --------
-- 1000      151456.89     27.346

-- 하지만 테이블이 다르다면 서브쿼리를 이용하여야 함
-- 하기 쿼리는 동일한 테이블에서 조회를 하는 것이지만 다른 테이블이면 테이블명이 상이함
-- 하기 쿼리에서 FROM, LIMIT 생략도 가능함
-- 만약 FROM만 남기고 LIMIT를 생략하면 테이블 행 수만큼 값이 출력됨
SELECT
    (SELECT COUNT(*) FROM users) '총인원',
    (SELECT AVG(balance) FROM users) '평균 계좌잔고',
    (SELECT AVG(age) FROM users) '평균 나이'
FROM users
LIMIT 1;

-- 이은정과 동일한 지역에 사는 사람의 수는?
-- AVG를 이용할 수도 있겠지만 동명이인이 존재할 수 있음
SELECT
    country
FROM users
WHERE last_name || first_name == '이은정';

-- country
-- -------
-- 전라북도
-- 경상북도

-- 하기와 같이 country = (조건) 인 경우 결과를 조회해보면 115명으로 전라북도에 있는 사람만 조회됨
SELECT
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users WHERE last_name || first_name = '이은정');

-- COUNT(*)
-- --------
-- 115

-- 지역 별 총 인원수
SELECT country, COUNT(*)
FROM users
GROUP BY country;
-- country  COUNT(*)
-- -------  --------
-- 강원도      101
-- 경기도      114
-- 경상남도     106
-- 경상북도     103
-- 전라남도     123
-- 전라북도     115
-- 제주특별자치도  118
-- 충청남도     105
-- 충청북도     115

-- 이 경우 전라북도와 경상북도의 인원 모두를 포함하려면 IN 을 사용하여야 함
SELECT
    COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users WHERE last_name || first_name = '이은정');


-- 특정 성씨 별 가장 적은 나이 사람의 이름, 나이 모두 출력
-- 1) 성씨 별 가장 적은 나이 출력
SELECT
    last_name,
    MIN(age)
FROM users
GROUP BY last_name;

-- 2) WHERE 조건에 1)을 반영하여 카운팅
SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;