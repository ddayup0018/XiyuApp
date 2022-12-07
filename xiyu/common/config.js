const user = {
	uid:'',
	username:'',
	token:'',
	set_user(uid,username,token){
		this.uid = uid
		this.username = username
		this.token = token 
		try{
			uni.setStorageSync("user",JSON.stringify({uid,username,token}))
		}catch(e){
			console.log(e.message)
		}
	},
	get_user(){
		if (!this.username){
			try{
				let user_storage = uni.getStorageSync("user")
				let u = JSON.parse(user_storage)
				this.uid = u.uid
				this.username = u.username
				this.token = u.token
			}catch(e){
				console.log(e.message)
			}
		}
		return{uid:this.uid,username:this.username,token:this.token}
	},
	clear_user(){
		this.uid = ''
		this.username=''
		this.token = ''
		try{
			uni.removeStorageSync('user')
		}catch(e){
			console.log(e.message)
		}
	}
}
export default {user}