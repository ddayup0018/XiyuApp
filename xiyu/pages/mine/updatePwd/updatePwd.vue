<template>
	<view class="outer">
		<h1>修改密码</h1>
		<view class="box">
			<view class="item">
				<uni-easyinput  prefixIcon="close" v-model="FormData.old_password" placeholder="请输入旧密码" type="password"/>
			</view>
			<view class="item">
				<uni-easyinput  prefixIcon="locked" v-model="FormData.new_password" placeholder="请输入新密码" type="password"/>
			</view>
			<view class="item">
				<uni-easyinput  prefixIcon="locked" v-model="FormData.re_new_password" placeholder="请再次输入新密码" type="password"/>
			</view>
			<view class="item">
				<button type="primary" @click="updatePwd">修改</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				FormData:{
					old_password:'',
					new_password:'',
					re_new_password:''
				}
			}
		},
		methods: {
			async updatePwd(){
				if (!this.FormData.old_password || !this.FormData.new_password){
					uni.showToast({
						title: '新旧密码不能为空',
						icon:'none'
					});
					return
				}
				if (this.FormData.re_new_password != this.FormData.new_password){
					uni.showToast({
						title: '新密码两次输入不一致',
						icon:'none'
					});
					return
				}
				// const res = await this.$http({
				// 	url:'/login/',
				// 	method:'POST',
				// 	data:this.FormData
				// })
				// if (res.data.code == 1){
				// 	console.log(res.data.msg)
					
				// 	this.$config.user.set_user(res.data.msg.username,res.data.msg.token)
				// 	uni.switchTab({
				// 		url:'/pages/home/home'
				// 	})
					
				// }else {
				// 	uni.showToast({
				// 		title:res.data.msg,
				// 		icon:'none',
				// 		duration:2000
				// 	})
				// }
			}
		}
	}
</script>

<style lang="scss">
	.outer{
		padding: 0;
		margin: 0;
		box-sizing: border-box;
		h1{
			text-align: center;
			margin: 80rpx;
		}
		.box{
			width: 80%;
			margin: 0 auto;
			.item{
				margin-top: 50rpx;
			}
		}
	}
</style>


