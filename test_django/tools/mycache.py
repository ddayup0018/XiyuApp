from django.core.cache import cache

def cache_set(expire):
    def _cache_set(func):
        def wrapper(request,*args,**kwargs):
            # print(request.path)
            cache_key = request.GET.get("username")
            print(cache_key)
            if cache_key == None:
                cache_key = request.path
            res = cache.get(cache_key)
            if res:
                print('缓存调用数据')
                return res

            res = func(request,* args, ** kwargs)
            print('数据库查询数据')
            cache.set(cache_key,res,expire)
            return res
        return wrapper
    return _cache_set