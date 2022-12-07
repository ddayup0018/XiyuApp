// const BASE_URL = "http://生产环境地址"
// const BASE_URL = "http://127.0.0.1:8000/api"
const BASE_URL = "http://192.168.3.8:8000/api"

export const http = (options)=>{
	return new Promise((resolve, reject)=>{
		// 封装主体：网络请求
		uni.request({				
			url: BASE_URL+options.url,
			data: options.data || {},		
      // 默认值GET，如果有需要改动，在options中设定其他的method值
			method: options.method || 'GET',      
			success: (res) => {
				resolve(res)
			},
			fail: (err) =>{
				// 页面中弹框显示失败
				uni.showToast({
					title: '请求接口失败'
				})
				// 返回错误消息
				reject(err)
			},
			catch:(e)=>{
				console.log(e);
			}
		})
	}
	)
}