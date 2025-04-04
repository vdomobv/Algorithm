-- 코드를 입력하세요
select flavor
from icecream_info
where ingredient_type = 'fruit_based'
and flavor in 
(
    select flavor
    from first_half
    where total_order >= 3000
);
