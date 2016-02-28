-- exec sp_databases;
-- use jingdong;

--SELECT TABLE_NAME FROM jingdong.INFORMATION_SCHEMA.Tables;

--select * from fir;				--count = 19
--select * from sec;				--count = 124
--select * from thr;				--count = 1190
--select * from category;			--count = 839502		-- pid,fir,sec,thr
--select * from customer;			--count = 342451		-- uid, age, recency, frequency, monetary, sd
--select * from product_new;		--count = 829672		-- pid, pdate, pname, price, previewnum, pposnum, pnegnum, pneunum
--select * from brand_new;			--count = 15501			-- id, bname
--select * from product_brand;		--count = 839502		-- pid, bid
--select * from rating;				--count = 14634054		-- id, pid, uid, score, rdate