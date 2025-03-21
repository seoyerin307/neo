SELECT 'SUCCESSE' FROM DUAL;

SELECT COUNT(*) FROM HR.BIGEMPLOYEES BE ;

CREATE USER "USER1" IDENTIFIED BY "1234"

GRANT ALL ON SHOP.MEMBERTBL TO "USER1";

GRANT ALL ON SHOP.PRODUCTTBL TO "USER1";

GRANT SELECT ON HR.BIGEMPLOYEES TO "USER1";




CREATE USER   IDENTIFIED BY "1234";

ALTER USER "DIRECTOR" ACCOUNT UNLOCK;

GRANT ALL ON SHOP.MEMBERTBL TO "DIRECTOR";

GRANT ALL ON SHOP.PRODUCTTBL TO "DIRECTOR";

GRANT SELECT ON HR.BIGEMPLOYEES TO "DIRECTOR";

GRANT SELECT ON HR.BIGEMPLOYEES TO "DIRECTOR";

SELECT * FROM usertbl;

SELECT * FROM buytbl;

CREATE TABLE buytbl2 AS (SELECT * FROM buytbl);

SELECT * FROM buytbl2;

CREATE TABLE buytbl3 AS (SELECT userid, prodname FROM buytbl);

SELECT * FROM buytbl3;

SELECT userid AS "사용자명", sum(amount) AS "총구매량"
FROM buytbl GROUP BY userid;

SELECT userid AS "사용자명", sum(amount * price) AS "총구매역"
FROM buytbl GROUP BY userid;

SELECT CAST(AVG(AMOUNT) AS NUMBER(5,3)) AS "평균 구매 수량"
FROM buytbl;

SELECT CAST(avg(amount) AS number(5,3)) "평균 구매 수량"
FROM buytbl GROUP BY userid;

SELECT username, max(height), min(height)
FROM usertbl GROUP BY username;

SELECT username, height FROM USERTBL
WHERE height = (SELECT max(height) FROM usertbl)
or height = (SELECT min(height) FROM usertbl);

SELECT count(*) FROM usertbl;

SELECT count(mobile1) AS "휴대폰 소유자" FROM usertbl;

SELECT userid AS "사용자명", sum(amount * price) AS "총구매역" 
FROM buytbl GROUP BY userid
HAVING sum(price * amount) > 1000
ORDER BY sum(price * amount);

SELECT idnum, groupname, sum(price * amount)
AS "비용"
FROM BUYTBL
GROUP by rollup(groupname, idnum);

SELECT groupname, sum(price * amount)
AS "비용"
FROM BUYTBL
GROUP by rollup(groupname);

SELECT groupname, sum(price * amount)
AS "비용",
grouping_ID(groupname) AS "추가행 여부"
FROM BUYTBL
GROUP by rollup(groupname);

CREATE TABLE cubetbl(prodname nchar(3), color nchar(2), amount int);

INSERT INTO cubetbl values('컴퓨터', '검정', 11);

INSERT INTO cubetbl values('컴퓨터', '파랑', 22);

INSERT INTO cubetbl values('컴퓨터', '검정', 33);

INSERT INTO cubetbl values('컴퓨터', '파랑', 44);

SELECT prodname, color, sum(amount) AS "수량 합계"
FROM cubetbl
GROUP BY cube(color, prodname)
ORDER BY prodname, color;

CREATE TABLE emptbl (emp nchar(3), manager nchar(3), department nchar(3));

INSERT INTO emptbl VALUES ('나사장', '없음', '없음');
INSERT INTO emptbl VALUES ('김재무', '나사장', '재무부');
INSERT INTO emptbl VALUES ('김부장', '김재무', '재무부');
INSERT INTO emptbl VALUES ('이부장', '김재무', '재무부');
INSERT INTO emptbl VALUES ('우대리', '이부장', '재무부');
INSERT INTO emptbl VALUES ('지사원', '이부장', '재무부');
INSERT INTO emptbl VALUES ('이영업', '나사장', '영업부');
INSERT INTO emptbl VALUES ('한과장', '이영업', '영업부');
INSERT INTO emptbl VALUES ('최정보', '나사장', '정보부');
INSERT INTO emptbl values ('윤차장', '최정보', '정보부');
INSERT INTO emptbl values ('이주임', '윤차장', '정보부');

SELECT *  FROM emptbl;


-- cte1

WITH empcte(empname, mgrname, dept, emplevel)
AS
(
	(SELECT emp, manager, department, 0
	FROM emptbl
	WHERE manager='없음')
	UNION ALL
	(SELECT emptbl.emp, emptbl.manager, 
	emptbl.department, empcte.emplevel+1
	FROM emptbl INNER JOIN empcte
	ON emptbl.manager = empcte.empname)
)
SELECT * FROM empcte ORDER BY dept, emplevel;


-- cte2

WITH empcte(empname, mgrname, dept, emplevel)
AS
(
	(SELECT emp, manager, department, 0
	FROM emptbl
	WHERE manager='없음')
	UNION ALL
	(SELECT emptbl.emp, emptbl.manager, 
	emptbl.department, empcte.emplevel+1
	FROM emptbl INNER JOIN empcte
	ON emptbl.manager = empcte.empname)
)
SELECT concat(rpad('ㄴ', emplevel * 2 + 1 , 'ㄴ'), 
empname) AS "직원이름",
dept AS "직원부서"
FROM empcte ORDER BY dept, emplevel; 


-- cte3

WITH empcte(empname, mgrname, dept, emplevel)
AS
(
	(SELECT emp, manager, department, 0
	FROM emptbl
	WHERE manager='없음')
	UNION ALL
	(SELECT emptbl.emp, emptbl.manager, 
	emptbl.department, empcte.emplevel+1
	FROM emptbl INNER JOIN empcte
	ON emptbl.manager = empcte.empname
	WHERE emplevel < 2)
)
SELECT concat(rpad('ㄴ', emplevel * 2 + 1 , 'ㄴ'), 
empname) AS "직원이름",
dept AS "직원부서"
FROM empcte ORDER BY dept, emplevel;

CREATE TABLE testtbl1 (id NUMBER(4), username nchar(3), age number(2));

INSERT INTO testtbl1 values(1, '홍길동', 25);

SELECT * FROM testtbl1;

INSERT INTO testtbl1 (id, username) VALUES(2, '설현');

SELECT * from testtbl1;

INSERT INTO testtbl1 (username, id, age) VALUES ('지민', 3, 26);

SELECT * FROM testtbl1;

--error
INSERT INTO testtbl1 values(4, 36, '공유');

CREATE TABLE tasttbl2 (
	id NUMBER(4),
	username nchar(3),
	age NUMBER(2),
	nation nchar(4) DEFAULT '대한민국'
);

CREATE SEQUENCE idseq2
START WITH 1
INCREMENT BY 1;

INSERT INTO testtbl2 VALUES (idseq2.nextval, '유나', 25, default);

SELECT * FROM testtbl2;

ALTER SEQUENCE idseq2
INCREMENT BY 10; 

INSERT into testtbl2 VALUES (idseq2.nextval, '미나', 21, '일본');

SELECT * FROM testtbl2;

ALTER SEQUENCE idseq2
INCREMENT BY 1;

INSERT into testtbl2 VALUES (idseq2.nextval, '사나', 21, '일본');

SELECT * FROM testtbl2;

ALTER SEQUENCE idseq2
INCREMENT BY 5;

INSERT into testtbl2 VALUES (idseq2.nextval, '채영', 23, default);

SELECT * FROM testtbl2;

SELECT idseq2.currval FROM testtbl2;


COMMIT;

DELETE FROM TESTTBL2 WHERE username='나';

SELECT * FROM testtbl2 WHERE username='나';

SELECT * FROM testtbl2;









CREATE TABLE testtbl3 (id NUMBER(3));

CREATE SEQUENCE cycleseq
START WITH 100
INCREMENT BY 100
MINVALUE 100
MAXVALUE 300
CYCLE
nocache;

INSERT INTO testtbl3 VALUES (cycleseq.nextval);

INSERT INTO testtbl3 VALUES (cycleseq.nextval);

INSERT INTO testtbl3 VALUES (cycleseq.nextval);

INSERT INTO testtbl3 VALUES (cycleseq.nextval);

SELECT * FROM testtbl3;




--

CREATE TABLE testtbl4(
	empid  NUMBER(6),
	firstname varchar2(20),
	lastname varchar2(25),
	phone varchar2(20)
);

INSERT INTO testtbl4
SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, PHONE_NUMBER
FROM EMPLOYEES;

SELECT * FROM TESTTBL4;



UPDATE TESTTBL4
SET firstname='David'
where empid=100;

SELECT * FROM TESTTBL4
WHERE empid=100;







SELECT * FROM testtbl4 WHERE lastname='King';


COMMIT;

DELETE FROM TESTTBL4

WHERE firstname='David' AND lastname='King';

SELECT * FROM testtbl4 WHERE lastname='King';

ROLLBACK;

SELECT * FROM testtbl4 WHERE lastname='King';

CREATE TABLE bigtbl1
AS
	SELECT LEVEL AS bigid,
	round(dbms_random.value(1,500000), 0)
AS numdata
	FROM dual
	CONNECT BY LEVEL <= 500000;

CREATE TABLE bigtbl2
AS
	SELECT LEVEL AS bigid,
	round(dbms_random.value(1,500000), 0)
AS numdata
	FROM dual
	CONNECT BY LEVEL <= 500000;

CREATE TABLE bigtbl3
AS
	SELECT LEVEL AS bigid,
	round(dbms_random.value(1,500000), 0)
AS numdata
	FROM dual
	CONNECT BY LEVEL <= 500000;

CREATE TABLE member1
AS (SELECT userid, username, addr FROM usertbl);

SELECT * FROM member1;

CREATE TABLE changetbl (
	userid char(8),
	username nvarchar2(10),
	addr nchar(2),
	changetype nchar(4)
);

INSERT INTO changetbl values('TKV', '태권브이','한국','신규가입');
INSERT INTO changetbl values('LGG', NULL,'제주','주소변경');
INSERT INTO changetbl values('LJB', NULL,'한국','주소변경');
INSERT INTO changetbl values('BBK', NULL,'탈퇴','회원탈퇴');
INSERT INTO changetbl values('SSK', NULL,'탈퇴','회원탈퇴');


SELECT * FROM MEMBER1;

MERGE INTO MEMBER1 M
USING (SELECT CHANGEtype, userid, username, addr FROM changetbl) C
ON (M.userid = C.userid)
WHEN MATCHED THEN 
	UPDATE SET M.addr = C.addr
	DELETE WHERE C.changetype = '회원탈퇴'
WHEN NOT MATCHED THEN
	INSERT (userid, username, addr) VALUES
	(C.userid, C.username, C.addr)
	
	SELECT * FROM changetbl;
	
	SELECT * FROM usertbl;
	
	SELECT * FROM member1;
	
	
	



























SELECT '100' + '200' FROM dual;

SELECT concat('100', '200') FROM dual;

SELECT 100 || '200' FROM dual;

SELECT price FROM buytbl WHERE price >= '500';

SELECT ascii('A'), chr(65), asciistr('한'), unistr('\D55C') FROM dual;

SELECT length('한글'), length('AB'), lengthb('한글'), lengthb('AB') FROM dual;

SELECT concat('이것이', 'ORACLE이다'), '이것이' || 'ORACLE이다' FROM DUAL;

SELECT INSTR('이것이 ORACLE이다. 이것도 ORACLE이다', '이것', 2) FROM DUAL;

SELECT LOWER('abcdEFGH'), UPPER('abcdEFGH'), INITCAP('THIS SI ORACLE') FROM DUAL;

SELECT REPLACE('이것이 ORACLE이다', '이것이', 'THIS IS') FROM DUAL;

SELECT TRANSLATE('이것이 ORACLE이다', '이것이', 'AB') FROM DUAL;

SELECT SUBSTR('대한민국만세', 3, 2) FROM DUAL;

SELECT REVERSE('Oracle') FROM dual;

SELECT lpad('이것이', 10, '##'), rpad('이것이', 10, '##') FROM dual;

SELECT ltrim(' 이것이'), rtrim('이것$$$$', '$') FROM dual;

SELECT trim(' 이것이 '), trim(BOTH 'ㅋ' FROM 'ㅋㅋ재밌어요.ㅋㅋㅋㅋㅋㅋㅋㅋ') FROM dual;

SELECT regexp_count('이것이 오라클이다', '이') FROM dual;

SELECT abs(-100) FROM dual;

SELECT ceil(4.4), FLOOR(4.4), round(4.4) FROM dual;

SELECT mod(13,4) FROM dual;

SELECT POWER(2,3) FROM DUAL;

SELECT SIGN(100), SIGN(0), SIGN(-100.123) FROM DUAL;

SELECT TRUNC(12345.12345, 2), TRUNC(12345.12345, -2) FROM DUAL;

SELECT ADD_MONTHS('2025-01-01', 5), ADD_MONTHS(SYSDATE, -5) FROM DUAL;

SELECT TO_DATE('2025-01-01') + 5, SYSDATE -5 FROM DUAL;

SELECT EXTRACT(YEAR FROM DATE '2025-01-01'), EXTRACT(DAY FROM SYSDATE) FROM DUAL;

SELECT LAST_DAY('2025-02-01') FROM DUAL;

SELECT NEXT_DAY('2025-03-16', '금요일'), NEXT_DAY(SYSDATE, '토요일') FROM DUAL;

SELECT MONTHS_BETWEEN(SYSDATE, '2004-11-22') FROM DUAL;

SELECT BIN_TO_NUM(1,0), BIN_TO_NUM(1,1,1,1) FROM DUAL;

SELECT BIN_TO_NUM(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1) FROM DUAL;

SELECT NUMTODSINTERVAL(48, 'HOUR'), NUMTODSINTERVAL(360000, 'SECOND') FROM DUAL;

SELECT NUMTOYMINTERVAL(37, 'MONTH'), NUMTOYMINTERVAL(1.5, 'YEAR') FROM DUAL;

SELECT ROW_NUMBER() OVER (ORDER BY HEIGHT DESC) "키 큰 순위", USERNAME, ADDR, HEIGHT
FROM USERTBL;

SELECT ROW_NUMBER() OVER (ORDER BY HEIGHT ASC) "키 큰 순위", USERNAME, ADDR, HEIGHT
FROM USERTBL;

SELECT ADDR, ROW_NUMBER()
OVER (PARTITION BY ADDR ORDER BY HEIGHT DESC, USERNAME ASC)
"키 큰 순위", USERNAME, ADDR, HEIGHT
FROM USERTBL;

SELECT DENSE_RANK()
OVER (ORDER BY HEIGHT DESC)
"키 큰 순위", USERNAME, ADDR, HEIGHT
FROM USERTBL;

SELECT RANK()
OVER (ORDER BY HEIGHT DESC)
"키 큰 순위", USERNAME, ADDR, HEIGHT
FROM USERTBL;

SELECT NTILE(3) OVER(ORDER BY HEIGHT DESC)
"반번호", USERNAME, ADDR, HEIGHT FROM USERTBL U ;

SELECT USERNAME, ADDR, HEIGHT AS "키",
HEIGHT - (LEAD(HEIGHT, 1, 0)
OVER(PARTITION BY ADDR ORDER BY HEIGHT DESC))
AS  "다음 사람과의 키 차이"
FROM USERTBL U ;

SELECT USERNAME, ADDR, HEIGHT AS "키",
HEIGHT - (FIRST_VALUE(HEIGHT)
OVER(PARTITION BY ADDR ORDER BY HEIGHT DESC))
AS  "지역별 최대 키와 차이"
FROM USERTBL U ;

SELECT USERNAME, ADDR, HEIGHT AS "키",
( CUME_DIST() 
OVER (PARTITION BY ADDR ORDER BY HEIGHT DESC)) * 100
AS "누적 인원 백분율 (%)"
FROM USERTBL;

drop TABLE pivotTest;

CREATE TABLE pivotTest(
	uname nchar(3),
	season nchar(2),
	amount number(3)
);

INSERT INTO PIVOTTEST VALUES ('김범수', '겨울', 10);
INSERT INTO PIVOTTEST VALUES ('윤종신', '여름', 15);
INSERT INTO PIVOTTEST VALUES ('김범수', '가을', 25);
INSERT INTO PIVOTTEST VALUES ('김범수', '봄', 3);
INSERT INTO PIVOTTEST VALUES ('김범수', '봄', 37);
INSERT INTO PIVOTTEST VALUES ('윤종신', '겨울', 40);
INSERT INTO PIVOTTEST VALUES ('김범수', '여름', 14);
INSERT INTO PIVOTTEST VALUES ('김범수', '겨울', 22);
INSERT INTO PIVOTTEST VALUES ('윤종신', '여름', 64);


SELECT * FROM pivotTest;



SELECT * FROM pivotTest
	pivot(sum(amount)
		FOR season
		IN('봄','여름','가을', '겨울'));














































































