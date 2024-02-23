-- 코드를 입력하세요
select DR_NAME,	DR_ID,	MCDP_CD,	date_format(HIRE_YMD, '%Y-%m-%d') from doctor where MCDP_CD = 'CS' or MCDP_CD ="GS"
order by hire_ymd desc, dr_name