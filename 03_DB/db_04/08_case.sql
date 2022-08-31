-- SQLite

-- 단순 조회
SELECT id, gender
FROM healthcare
LIMIT 5;


--id  gender
----  ------
--1   1
--2   2
--3   2
--4   1
--5   2

-- 성별 1(남자), 2(여자
SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
    END AS 성별
FROM healthcare
LIMIT 5;

-- id  성별
-- --  --
-- 1   남자
-- 2   여자
-- 3   여자
-- 4   남자
-- 5   여자

-- 흡연(smoking)
SELECT
    id,
    smoking,
    CASE
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비스모커'
    ELSE '무응답'
    END AS '흡연여부'
FROM healthcare
LIMIT 5;

-- id  smoking  흡연여부
-- --  -------  ----
-- 1   1        비흡연자
-- 2   1        비흡연자
-- 3   1        비흡연자
-- 4   1        비흡연자
-- 5   1        비흡연자


-- 나이에 따라서 구분
-- 청소년 (~18), 청년(~40), 중장년(~90), 그 외 노년
SELECT
    first_name,
    last_name,
    age,
    CASE
        WHEN age <= 18 THEN '청소년'
        WHEN age > 18 AND age <= 40 THEN '청년'
        WHEN age > 40 AND age <= 90 THEN '중장년'
        ELSE '노년'
    END '연령대'
FROM users
LIMIT 5;

-- first_name  last_name  age  연령대
-- ----------  ---------  ---  ---
-- 정호          유          40   청년
-- 경희          이          36   청년
-- 정자          구          37   청년
-- 미경          장          40   청년
-- 영환          차          30   청년