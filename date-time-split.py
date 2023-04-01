import datetime
input_pattern = 'http://proba2.oma.be/swap/data/bsd/%Y/%m/%d/swap_lv1_%Y%m%d_%H%M%S.fits'
input_url =     'http://proba2.oma.be/swap/data/bsd/2000/04/10/swap_lv1_20041224_120743.fits'
supported_date_formats = [
    '%Y/%m/%d',
    '%Y%m%d_%H%M%S',
    '%Y-%m-%d',
    '%Y-%m-%dT%H:%M:%S.%f',
    '%Y%m%dT%H%M%S.%f',
    #can add more formats if needed
]
pattern_lst = []
input_lst = []
start_index = 0
end_index = 0
# split the pattern based on supported patterns
for format_date in supported_date_formats:
    if(format_date in input_pattern):
        end_index = input_pattern.find(format_date) + len(format_date)
        pattern_lst.append(input_pattern[start_index : end_index])
        current_pattern = input_pattern[start_index : end_index]
        start_index = end_index
# split the input url based on pattern_lst
start_index = 0
end_index = 0
for pattern in pattern_lst:
    end_index = start_index+len(pattern)
    if('%Y' in pattern):
        end_index+=2     
    input_lst.append(input_url[start_index:end_index])
    start_index = end_index
# for each pattern_lst, check if input_list contains valid format
for x in range(0,len(pattern_lst)):
    try:
        datetime_obj = datetime.datetime.strptime(input_lst[x],pattern_lst[x])
    except ValueError:
        print('Input URL doesnt match')
    else:
        print('Input URL matches')
