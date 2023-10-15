# TODO Найдите количество книг, которое можно разместить на дискете
v_mb = 1.44
v_b = v_mb*1024*1024
pages = 100
strs = 50
count_el = 25
one_el = 4
book = one_el*count_el*strs*pages

res_count = int(v_b // book)

print("Количество книг, помещающихся на дискету:", res_count)
