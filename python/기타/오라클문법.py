


-- 1. 특정열 가져오기
SELECT 
    empno
    , ename
    , job
    , sal
FROM emp;






-- 3. 컬럼명 변경
SELECT
    empno as employee_no
FROM emp;






-- 4. 연결 연산자 사용
-- 두개의 컬럼값을 서로 붙여서 출력
SELECT ename || sal FROM emp;
SELECT ename || '의 작업은 ' || job || ' 입니다.' as 작업정보 FROM emp;








-- 5. 중복된 데이터 제거 후 출력
SELECT DISTINCT job FROM emp;
SELECT UNIQUE job FROM emp;







-- 6. 데이터 정렬해서 출력하기
-- ORDER BY 컬럼명 ASC (오름차순) / DESC (내림차순)
SELECT ename, sal FROM emp ORDER BY sal;
SELECT ename, sal FROM emp ORDER BY sal DESC;
SELECT ename, sal FROM emp ORDER BY sal ASC;







-- 7. WHERE절
SELECT ename, sal, job FROM emp 
WHERE sal = 3000;

SELECT ename, sal, job FROM emp 
WHERE sal > 1000;








-- 8. 문자와 날짜 검색
-- 조회 : ename, sal, job, hiredate, deptno
-- WHERE절 : ename = 'SCOTT':
SELECT ename, sal, job, hiredate, deptno FROM emp 
WHERE ename = 'SCOTT';


-- 날짜 검색
-- 날짜 형식 변경
-- 날짜 형식 관련 PPT 참조. 
-- RR/MM/DD

-- 날짜 형식 확인
SELECT * FROM NLS_SESSION_PARAMETERS WHERE PARAMETER = 'NLS_DATE_FORMAT';

-- 날짜 형식 변경
ALTER SESSION SET NLS_DATE_FORMAT='YY/MM/DD';

--날짜 형식이 변경되서 검색이 안됨
SELECT ename, sal FROM emp WHERE hiredate='82/12/22';

-- 날짜 형식 변경
ALTER SESSION SET NLS_DATE_FORMAT='RR/MM/DD';

-- 검색됨
SELECT ename, sal FROM emp WHERE hiredate='82/12/22';







-- 9. 산술 연산자 (*, /, +, -)
SELECT * FROM emp;
SELECT ename, sal, comm, sal + comm FROM emp;

-- NULL값을 0으로 처리    
SELECT
    ename, sal, sal + comm, sal + NVL(comm, 0)  
FROM emp;







-- 10. 기타 비교 연산자
-- BETWEEN 사용하기
-- sal 1000 이상, sal 3000 이하
-- 1000 <= sal <= 3000

SELECT 
    ename, sal
FROM emp
WHERE (sal >= 1000) AND (sal <= 3000);

SELECT 
    ename, sal
FROM emp
WHERE sal BETWEEN 1000 AND 3000;


-- hiredate 82/01/01에서 82/12/31 사이 입사한 사람 구하기
-- 조회 ename, sal, hiredate
SELECT 
    ename, sal, hiredate
FROM emp
WHERE hiredate BETWEEN '82/01/01' AND '82/12/31';







-- 11. 문자로 데이터 검색
-- A가 끝에서 2번째에 있는 데이터 검색
SELECT ename FROM emp
WHERE ename LIKE '%A_';

-- A가 2번째에 있는 데이터 검색
SELECT ename FROM emp
WHERE ename LIKE '_A%';

-- A가 들어있는 모든 데이터 검색
SELECT ename FROM emp
WHERE ename LIKE '%A%';







-- 12. 대소문자 변환 함수
-- Upper(전체대문자), Lower(전체소문자), Initcap(첫글자만 대문자)

SELECT ename 
    , UPPER(ename)
    , LOWER(ename)
    , INITCAP(ename)
FROM emp;






-- 13. 문자에서 특정 글자 추출
-- SUBSTR
-- 첫번자와 3번째 글자
SELECT SUBSTR('smith', 1, 3) FROM DUAL;
--2번째 글자부터 2글자
SELECT SUBSTR('smith', -2, 2) FROM DUAL;
-- 2번쨰 글자부터 다가져오기
SELECT SUBSTR('smith', 2) FROM DUAL;






-- 14. 문자열의 길이 출력
-- 이름 ename 출력, LENGTH() 활용
-- 길이구하고 길이순으로 정렬
SELECT ename, LENGTH(ename) FROM emp
ORDER BY LENGTH(ename);

-- 길이구하고 역정렬
SELECT ename, LENGTH(ename) FROM emp
ORDER BY LENGTH(ename) DESC;







-- 15. 특정 철자를 다른 철자로 변경하기
-- REPLACE()
SELECT ename, sal FROM emp;
-- 숫자0을 *로 변경
SELECT ename, REPLACE(sal, 0, '*') FROM emp;
-- 숫자1을 --로 변경
SELECT ename, REPLACE(sal, 1, '--') FROM emp;

-- 여러문자를 변환시 REGEXP_REPLACE 사용
SELECT ename, REGEXP_REPLACE(sal, '[0-3]', '*') FROM emp;







-- 16. 테이블 생성
CREATE TABLE TEST_ENAME ( ename varchar2(20) );

-- ename 컬럼에 내용 추가
INSERT INTO TEST_ENAME VALUES('LDH');
INSERT INTO TEST_ENAME VALUES('abcdefg');
INSERT INTO TEST_ENAME VALUES('가라다나마');

SELECT * FROM test_ename;


SELECT ename, REPLACE(ename, 'D', '*') FROM test_ename;

-- 영문은 대소문자 구분함
SELECT ename, REGEXP_REPLACE(ename, '[D-H]', '*') FROM test_ename;

-- 영어 알파뱃순으로 변경됨
SELECT ename, REGEXP_REPLACE(ename, '[d-h]', '*') FROM test_ename;

-- 한글은 가나다순으로 변경됨
SELECT ename, REGEXP_REPLACE(ename, '[가-다]', '*') FROM test_ename;

-- 특정위치의 글자 변경
SELECT REPLACE(ename, SUBSTR(ename, 3, 1), '*') FROM test_ename;

-- 좌우에 그래프만들기
SELECT ename, LPAD(sal, 10, '*'), RPAD(sal, 10, '*') FROM emp;
-- 기존 데이터값을 이용하여 그래프 만들기
SELECT ename, sal, LPAD('*', round(sal/100), '*') as bar_chart FROM emp;






-- 17. 특정 문자 빼기 공백 제거
-- TRIM
SELECT 'SMITH', LTRIM('SMITH', 'S'), RTRIM('SMITH', 'H')
    , TRIM('S' FROM 'SMITHS') FROM dual;
    

INSERT INTO emp(empno, ename, sal, job, deptno) 
        VALUES(8291, 'JACK     ', 3000, 'SALESMAN', 30);

SELECT ename, sal FROM emp;
SELECT ename, sal FROM emp WHERE ename = 'JACK';
SELECT ename, sal FROM emp WHERE RTRIM(ename) = 'JACK';





-- 18. JACK 삭제
DELETE FROM EMP WHERE TRIM(ename) = 'JACK';
-- 반영
commit;
SELECT * FROM EMP;





-- 19. 반올림
SELECT '876.567' FROM DUAL;
SELECT '876.567' AS 숫자, ROUND(876.567, 1) FROM DUAL;
SELECT '876.567' AS 숫자, ROUND(876.567, -1) FROM DUAL;

SELECT '876.567' AS 숫자, TRUNC(876.567, 1) FROM DUAL;
SELECT '876.567' AS 숫자, TRUNC(876.567, -1) FROM DUAL;







-- 20. 날짜간 개월 수 출력하기
SELECT ename, hiredate FROM emp;

SELECT TO_DATE('2021-07-27', 'RRRR-MM-DD') - TO_DATE('2021-05-27', 'RRRR-MM-DD') FROM emp;
SELECT ROUND(TO_DATE('2021-07-27', 'RRRR-MM-DD') - TO_DATE('2021-05-27', 'RRRR-MM-DD')) FROM emp;


-- 개월 수 더한 날짜 구하기
-- ADD_MONTHS
-- 50개월뒤의 날짜 출력
SELECT ADD_MONTHS(TO_DATE('2021-07-27', 'RRRR-MM-DD'), 50) FROM DUAL;

-- 100일 후의 날짜 출력
SELECT TO_DATE('2021-07-27', 'RRRR-MM-DD') + 100 FROM DUAL;

-- 1년 3개월 후의 날짜 출력
SELECT TO_DATE('2021-07-27', 'RRRR-MM-DD') + interval '1-3' YEAR(1) TO MONTH FROM DUAL;


-- scott의 입사 년월을 출력
-- scott의 급여, 7777 -> ',7,777'
SELECT ename , hiredate 
    , TO_CHAR(hiredate, 'RRRR')
    , TO_CHAR(hiredate, 'MM')
    , TO_CHAR(hiredate, 'DD')
    , TO_CHAR(hiredate, 'DAY')
    , TO_CHAR(sal, '999,999')
FROM emp;







-- 21. 천단위와 백만단위 표시
SELECT ename as 이름
    , TO_CHAR(sal * 200, '999,999,999') as 월급
FROM emp;


-- 원화표시
SELECT ename as 이름
    , TO_CHAR(sal * 200, 'L999,999,999') as 월급
FROM emp;







-- 22. 임시 테이블 생성
CREATE TABLE EMP32
(ENAME VARCHAR2(10), SAL VARCHAR2(10)); 
INSERT INTO EMP32 VALUES('SCOTT', '3000');
INSERT INTO EMP32 VALUES('SMITH', '1200');
COMMIT;

SELECT * FROM EMP32;

-- 문자를 숫자로 변환 TO_NUMBER 해서 출력
SELECT ename, sal FROM EMP32 WHERE TO_NUMBER(sal) = 1200;








-- 23. 테이블 확인
SELECT * FROM EMP;
SELECT * FROM DEPT;
SELECT * FROM SALGRADE;


-- 24. 여러 테이블의 데이터를 조인하서 출력
-- INNER JOIN   두개의 테이블의 키값이 같은것이 있는것만 출력
SELECT ename, loc FROM emp, dept
WHERE emp.deptno = dept.deptno;






-- 25. 직업이 Analyst인 사원들만 출력
SELECT ename, loc, job FROM emp, dept 
Where emp.deptno = dept.deptno 
    AND emp.job = 'ANALYST';




-- 26. EMP. SALGRADE 두개 조인
-- ENAME, SAL, GRADE 등급 출력
SELECT E.ENAME, E.SAL, S.GRADE 
FROM EMP E, SALGRADE S
WHERE E.SAL BETWEEN S.LOSAL AND S.HISAL;



-- 27. OUTER JOIN
SELECT E.ENAME, D.LOC FROM EMP E, DEPT D
WHERE E.DEPTNO (+) = D.DEPTNO;



-- 28. 셀프 조인
-- EMP 테이블이 이름, 직업, 관리자의 이름, 관리자의 직업
SELECT E.ENAME AS 사원, E.JOB, M.ENAME AS 관리자, M.JOB 
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO AND E.JOB = 'SALESMAN';



-- 29. LEFT JOIN
SELECT E.ENAME, D.LOC FROM EMP E, DEPT D
WHERE E.DEPTNO  = D.DEPTNO (+);



-- 30. FULL JOIN
SELECT E.ENAME, E.JOB, E.SAL, D.LOC
FROM EMP E FULL OUTER JOIN DEPT D ON (E.DEPTNO = D.DEPTNO);










-- 31. 조건문
-- 부서 번호가 10이면 300, 부서 번호가 20이면 400, 둘다 아니면 0
SELECT ENAME, DEPTNO, DECODE(DEPTNO, 10, 300, 20, 400, 0) AS 보너스
FROM EMP;





-- 32. 가원 번호가 짝수인지, 홀수 인지 출력하는 쿼리
SELECT EMPNO, MOD(EMPNO, 2), DECODE(MOD(EMPNO, 2), 0, '짝수', 1, '홀수') 
FROM EMP;






-- 33. CASE WHEN
-- SAL 급여 따라서 보너스를 차등으로 지급
-- SAL >= 3000, 500 / 2000 <= SAL <= 3000, 300, SAL >= 1000, 100, 0
SELECT ENAME, JOB, SAL, 
    CASE WHEN SAL >= 3000 THEN 500
        WHEN SAL >= 2000 THEN 300
        WHEN SAL >= 1000 THEN 200
        ELSE 0 END AS 보너스
FROM EMP;




34. 
SELECT ENAME, COMM FROM EMP;
-- IS NULL, 500
SELECT ENAME, JOB, COMM, 
    CASE WHEN COMM IS NULL THEN 500 ELSE 0 END BONUS
FROM EMP;






-- 35. JOB, SALESMAN, ANALYST 500 보너스
-- JOB, CLARK, MANAGER 300 보너스
SELECT ENAME, JOB, 
    CASE WHEN JOB IN ('SALESMAN', 'ANALYST') THEN 500
        WHEN JOB IN ('CLARK', 'MANAGER') THEN 300
        ELSE 0 END AS BONUS
FROM EMP;









-- 36. 집계 함수 / 분석 함수 = sum(), avg(), min() max()
-- 윈도우 함수 = RANK()
SELECT ENAME, JOB, SAL, RANK() OVER (ORDER BY SAL DESC) 순위
FROM EMP
WHERE JOB IN ('ANALYST', 'MANAGER');

-- DENSE_RANK()
SELECT ENAME, JOB, SAL
    , RANK() OVER (ORDER BY SAL DESC)순위
    , DENSE_RANK() OVER (ORDER BY SAL DESC) AS DENSE_RANK_NUM
FROM EMP
WHERE JOB IN ('ANALYST', 'MANAGER');






-- 37. 월급이 2975인 사람의 순위
-- WITHIN GROUP
SELECT DENSE_RANK(2975) WITHIN GROUP (ORDER BY SAL DESC) 순위
FROM EMP;





-- 38. 입사일이 1981년 11월 18일인 사람이 전체사원중 몇번째 입사한 사람인가
SELECT DENSE_RANK('81/11/17') WITHIN GROUP (ORDER BY HIREDATE DESC) 순위
FROM EMP;






-- 39. 등급 출력하기
-- NTILE(5) = 전체데이터를 5개의 등급으로 분할
SELECT ENAME, JOB, SAL, NTILE(4) OVER (ORDER BY SAL DESC NULLS LAST) 등급
FROM EMP;






-- 40. 순위의 비율(상위 몇퍼센트인가)
-- CDME_DIST
SELECT ENAME, JOB, SAL, CUME_DIST() OVER (ORDER BY SAL DESC)
FROM EMP;






-- 41. 전 행, 다음행 출력하기
-- LAG(), LEAD()
SELECT EMPNO, ENAME, SAL, LAG(SAL, 1) OVER(ORDER BY SAL ASC) AS "전 행"
    , LEAD(SAL, 1) OVER(ORDER BY SAL ASC) AS "다음행"
FROM EMP
WHERE job in ('ANALYST', 'MANAGER');







-- 43. 부서 번호, 사원 번호, 이름, 입사일, 직전 입사직원의 입사일
-- 직후 입사직원의 입사일, 부서번호로 구분
SELECT DEPTNO, EMPNO, ENAME, HIREDATE
    , LAG(HIREDATE, 1) OVER(PARTITION BY DEPTNO ORDER BY HIREDATE ASC)
    , LEAD(HIREDATE, 1) OVER(PARTITION BY DEPTNO ORDER BY HIREDATE ASC)
FROM EMP







-- 071. 서브 쿼리 사용하기
-- JONES보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력한다. 
-- 서브쿼리: JONES의 급여
-- 메인쿼리: JONES보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력한다. 
SELECT sal FROM emp WHERE ename='JONES';
-- 2975
SELECT 
    ename
    , sal
FROM emp
WHERE sal > (SELECT sal FROM emp WHERE ename='JONES');




-- SCOTT과 같은 월급을 받는 사원들의 이름과 월급을 출력하는 쿼리
-- 서브쿼리: SCOTT의 급여
SELECT sal FROM emp WHERE ename = 'SCOTT';
-- 메인쿼리 SCOTT과 같은 월급을 받는 사원들의 이름과 월급 출력
SELECT
    ename
    , sal
FROM emp
WHERE sal = (SELECT sal FROM emp WHERE ename = 'SCOTT');
-- 그런데, SCOTT을 제외하고 싶다면, 위 쿼리에서 SCOTT을 제외하는 쿼리를 작성한다. 
SELECT
    ename
    , sal
FROM emp
WHERE sal = (SELECT sal FROM emp WHERE ename = 'SCOTT')
      AND ename !='SCOTT';
-- 072. 서브 쿼리 사용하기 (다중 행 서브쿼리)
-- 직업이 SALESMAN인 사원들과 같은 월급을 받는 사원들의 이름과 월급 출력
SELECT 
    ename
    , sal
FROM emp
WHERE sal in (SELECT sal FROM emp WHERE job='SALESMAN');
-- IN이 아니라 = 대입 시, 에러 발생
-- SALESMAN인 사원들이 한 명이 아니라 여러 명이기 때문
-- 073. 서브 쿼리 사용하기 (NOT IN)
-- 관리자가 아닌 사원들의 이름과 월급과 직업을 출력함. 
SELECT 
    ename
    , sal
    , job
FROM emp
WHERE empno not in (SELECT mgr 
                    FROM emp 
                    WHERE mgr is not null);
-- 만약 mgr is not null을 사용하지 않고 실행하면 아무것도 출력되지 않음
-- 선택된 레코드가 없다고 나오는 이유는 mgr 컬럼에 NULL값이 있기 때문
SELECT 
    ename
    , sal
    , job
FROM emp
WHERE empno not in (SELECT mgr from emp);
-- 074. 서브 쿼리 사용하기 (EXISTS와 NOT EXISTS)
-- 부서 테이블에 있는 부서 번호 중, 사원 테이블에도 존재하는 부서 번호, 부서명 부서 위치 출력
SELECT 
    *
FROM dept d
WHERE EXISTS (SELECT * FROM emp e WHERE e.deptno = d.deptno);
-- DEPT 테이블에는 존재하는 부서 번호
-- 그러나, EMP 테이블에 존재하지 않는 데이터 검색 시, NOT EXISTS 사용
SELECT 
    * 
FROM dept d 
WHERE NOT EXISTS (SELECT * FROM emp e WHERE e.deptno = d.deptno);
-- 075. 서브 쿼리 사용하기 (HAVING절의 서브 쿼리)
SELECT
    job
    , sum(sal)
FROM emp
GROUP BY job
HAVING sum(sal) > (SELECT sum(sal) FROM emp WHERE job='SALESMAN');
--
SELECT
    job
    , sum(sal)
FROM emp
WHERE JOB != 'SALESMAN'
GROUP BY job
HAVING sum(sal) >= (SELECT sum(sal) FROM emp WHERE job='SALESMAN')
ORDER BY sum(sal) DESC;
-- 그룹 함수 이용한 데이터 검색은 WHERE이 아닌 HAVING절 작성
-- 076. 서브 쿼리 사용하기 (FROM절의 서브 쿼리)
SELECT 
    v.ename
    , v.sal
    , v.순위
FROM (SELECT ename, sal, rank() OVER(order by sal desc) 순위 FROM emp) v
WHERE v.순위 = 1;
-- 077. 서브 쿼리 사용하기 (SELECT절의 서브 쿼리)
SELECT 
    ename
    , sal
    , (SELECT max(sal) from emp where job='SALESMAN') as 최대월급
    , (SELECT min(sal) from emp where job='SALESMAN') as 최소월급
FROM emp
WHERE job='SALESMAN';





-- populations 데이터 가져오기
-- 서브쿼리 맛보기
-- 질문 1. 먼저 2015년 전체 국가의 평균 수명을 계산하십시오.
SELECT 
    AVG(life_expectancy)
FROM populations
WHERE year = 2015;
-- 질문 2. 
-- 조건 1. 모든 데이터를 조회한다. 
-- 조건 2. 2015년 평균 기대수명의 1.15배보다 높도록 설정한다. (life_expectancy > 1.15 * )
SELECT 
    *
FROM populations
WHERE life_expectancy > 1.15 * (SELECT AVG(life_expectancy) FROM populations WHERE year = 2015) 
	  AND year = 2015
FETCH FIRST 5 ROWS ONLY;
-- 질문 3
-- 조건 1. 서브 쿼리의 국가 테이블에 있는 capital 필드를 사용합니다.
-- 조건 2. cities 테이블에서 name, country code, urban area population 필드를 조회한다.
SELECT name, country_code, urbanarea_pop
  FROM cities
WHERE name IN
  (SELECT capital
   FROM countries)
ORDER BY urbanarea_pop DESC;
-- 질문 4. 
-- economies 데이터셋 불러오기
-- 조건 1. economies data에서 country code, inflation rate, unemployment rate를 조회한다. 
-- 조건 2. inflation rate 오름차순으로 정렬한다. 
-- 조건 3. Alias 사용하지 않는다. 
-- 조건 4. countries 테이블내 gov_form 컬럼에서 Constitutional Monarchy 또는 `Republic`이 들어간 국가는 제외한다. 
-- Select fields
SELECT code, inflation_rate, unemployment_rate
  FROM economies
  WHERE year = 2015 AND code NOT IN
  	(SELECT code
  	 FROM countries
  	 WHERE (gov_form = 'Constitutional Monarchy' OR gov_form LIKE '%Republic%'))
ORDER BY inflation_rate;
-- 질문 5. 
-- 조건 1. 첫번째 주석을 풀고 실행합니다. 
SELECT * FROM countries;
SELECT countries.name as country, COUNT(*) as cities_num
  FROM cities
	  INNER JOIN countries
	  ON countries.code = cities.country_code
GROUP BY countries.name
ORDER BY cities_num DESC, country;
/* 
SELECT ___ AS ___,
  (SELECT ___
   FROM ___
   WHERE countries.code = cities.country_code) AS cities_num
FROM ___
ORDER BY ___ ___, ___
LIMIT 9;
*/
SELECT countries.name AS country, COUNT(*) AS cities_num
  FROM cities
	  INNER JOIN countries
	  ON countries.code = cities.country_code
GROUP BY countries.name
ORDER BY cities_num DESC, country;
-- 조건 2. GROUP BY 코드를 변환하여 SELECT 내부의 하위 쿼리를 사용하도록 한다. 
-- 즉, 첫 번째 쿼리에서 GROUP BY 코드를 사용하여 주어진 결과와 일치하는 결과를 얻으려면 빈칸을 채운다.
-- 조건 3. 다시 city_num 내림차순으로 결과를 정렬한 다음 국가 오름차순으로 정렬합니다.
SELECT countries.name AS country,
  (SELECT COUNT(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country;
-- 질문 6. 
-- 조건 1. 아래 쿼리 실행
SELECT name, continent, inflation_rate
  FROM countries
  	INNER JOIN economies
    USING (code)
WHERE year = 2015;
-- 조건 2. 위 쿼리를 FROM 이내의 서브쿼리를 활용한다. 
-- 조건 3. 2015년의 continent 그룹별로 하여 continent, inflation_rate의 최댓값을 조회한다.
-- Select the maximum inflation rate as max_inf
SELECT 
    continent
    , MAX(inflation_rate) AS max_inf
  FROM (
      SELECT 
        name
        , continent
        , inflation_rate
      FROM countries
      INNER JOIN economies
      USING (code)
      WHERE year = 2015)
GROUP BY continent
ORDER BY MAX_INF;
-- 조건 4. 각 대륙별 inflation_rate가 가장 높은 나라를 추출하는 코드를 작성하도록 합니다. 
-- 조건 5. 위 쿼리에서 continent 필드 조회하는 것만 제외합니다. 그리고, 해당 쿼리를 다음 쿼리에서 IN 이하절로 활용합니다.
SELECT name, continent, inflation_rate
  FROM countries
	INNER JOIN economies
	ON countries.code = economies.code
  WHERE year = 2015
    AND inflation_rate IN (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
             SELECT name, continent, inflation_rate
             FROM countries
             INNER JOIN economies
             -- Using(code) 대신 ON 쿼리를 작성합니다. 
             ON countries.code = economies.code
             WHERE year = 2015)
        GROUP BY continent);