import axios from "axios"

// 接口通用地址
const BASEURL = 'http://127.0.0.1:8000/api_backadmin'

//  拦截器，这个内容多了可以单搞一个js文件
//  请求异常拦截
axios.interceptors.request.use(config => {
    // 请求拦截方法，如是否获取到token
    return config;
}, err => {
    // 错误处理 
    alert(err)
    return Promise.resolve(err);
});
 
//  响应异常拦截
axios.interceptors.response.use(result => {
    // 响应拦截方法
    return result;
}, err => {
    // 错误处理
    alert('请求接口失败！')
    return Promise.resolve(err);
})

// 方法封装

// POST方法封装
export const postRequest = (url, params) => {
    return axios({
        method: 'post',
        url: BASEURL+url,
        data: params
    });
}
 
 
//  GET方法封装
export const getRequest = (url, params) => {
    return  axios({
            method: 'get',
            url: BASEURL+url,
            params: params
        }) 
}
 
//  PUT 方法封装
export const putRequest = (url, params) => {
    return axios({
        method: 'put',
        url: BASEURL+url,
        data: params
    });
}
 
//  DELETE 方法封装
export const deleteRequest = (url, params) => {
    return axios({
        method: 'delete',
        url: BASEURL+url,
        data: params
    });
}

 