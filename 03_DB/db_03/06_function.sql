-- SQLite

SELECT * FROM users LIMIT 1;

-- 문자열합치기 ||
-- (성+이름)으로 5명만 출력
SELECT
    last_name || first_name 이름,
    age,
    country,
    phone,
    balance
FROM users
LIMIT 5;

-- 문자열 길이 LENGTH
SELECT
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;

-- 문자열 변경 REPLACE
SELECT
    first_name,
    phone,
    REPLACE(phone, '-', '')
FROM users
LIMIT 5;

-- 숫자 활용: MOD 나머지 구하기
SELECT MOD(5, 2)
FROM users
LIMIT 1;

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;

-- 9의 제곱근
SELECT SQRT(9)
FROM users
LIMIT 1;

-- 9^2
SELECT POWER(9, 2)
FROM users
LIMIT 1;