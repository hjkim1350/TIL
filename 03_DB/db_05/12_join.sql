-- SQLite

-- A와 B 테이블에서 값이 일치하는 것들만
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- A테이블에서 name, B테이블에서 title만 조회
SELECT
    users.name,
    role.title
FROM users INNER JOIN role
    ON users.role_id = role.id;

-- name  title
-- ----  -----
-- 관리자   admin
-- 김철수   staff
-- 이영희   staff


-- staff만 출력
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff


-- 이름을 내림차순으로 입력
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id
ORDER BY users.name DESC;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 3   이영희   2        2   staff
-- 2   김철수   2        2   staff
-- 1   관리자   1        1   admin


-- LEFT OUTER JOIN : 왼쪽의 테이블을 기준으로 JOIN
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444


-- LEFT OUTER JOIN : NULL 값이 아닌 데이터만 조회
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1


-- FULL OUTER JOIN: 중복은 제거한 모든 테이블의 값을 조회 (합집합 개념)
SELECT *
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;

-- CROSS JOIN: 두 테이블 데이터의 모든 조합을 가져옴
SELECT * 
FROM users CROSS JOIN role;

-- id  name  role_id  id  title
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin
-- 1   관리자   1        2   staff
-- 1   관리자   1        3   student
-- 2   김철수   2        1   admin
-- 2   김철수   2        2   staff
-- 2   김철수   2        3   student
-- 3   이영희   2        1   admin
-- 3   이영희   2        2   staff
-- 3   이영희   2        3   student


-- 3개 테이블 JOIN
SELECT *
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;
-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   김철수   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin