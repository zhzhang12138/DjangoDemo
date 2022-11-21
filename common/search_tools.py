# -*- coding:utf-8 -*-
# @FileName  :search_tools.py
# @Time      :2022/11/17 16:42
# @Author    :John Doe
def is_search_param(item):
    """
    Filter search params
    """
    if item[0].startswith("search_"):
        return True
    return False


def get_search_param(item):
    return (item[0][7:], item[1])


def search_decorator(f):
    """
    decorate get_queryset method
    do further filtering
    URL carries param: search_QUERY
    QUERY is a string follows query rule of Django model
    """

    def wrapper(*args, **kwargs):
        queryset = f(*args, **kwargs)

        items = args[0].request.query_params.items()
        items = filter(is_search_param, items)
        search_items = map(get_search_param, items)
        search_dict = {key: value for key, value in search_items}

        try:
            if len(search_dict) > 0:
                queryset = queryset.filter(**search_dict)
        except Exception as e:
            print(e)
        return queryset

    return wrapper
