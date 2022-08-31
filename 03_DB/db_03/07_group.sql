-- SQLite

-- 성별 갯수
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;

-- GROUP BY에서 활용하는 컬럼을 제외하고 집계함수 쓰기
-- GROUP BY는 결과 정렬되지 않으므로 정렬 필요할 경우 OREDER BY 사용
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

-- 100번 이상 등장한 성만 출력
-- GROUP BY의 조건이 필요하면 HAVING 사용 (WHERE X)
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;