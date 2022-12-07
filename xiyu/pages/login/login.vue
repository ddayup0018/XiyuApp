<template>
	<view class="outer">
		<h1>用户登录</h1>
		<view class="box">
			<view class="item">
				<uni-easyinput prefixIcon="person" v-model="FormData.username" placeholder="请输入用户名" />
			</view>
			<view class="item">
				<uni-easyinput  prefixIcon="locked" v-model="FormData.password" placeholder="请输入密码" type="password"/>
			</view>
			<view class="item">
				<button type="primary" @click="userLogin">提交</button>
			</view>
			<view class="item">
				<button type="primary" @click="toRegister">注册</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				FormData:{
					username:'',
					password:''
				}
			}
		},
		methods: {
			async userLogin(){
				if (!this.FormData.username || !this.FormData.password){
					uni.showToast({
						title: '用户名密码不能为空',
						icon:'none'
					});
					return
				}
				const res = await this.$http({
					url:'/login/',
					method:'POST',
					data:this.FormData
				})
				if (res.data.code == 1){
					console.log(res.data.msg)
					
					this.$config.user.set_user(res.data.msg.uid,res.data.msg.username,res.data.msg.token)
					uni.switchTab({
						url:'/pages/home/home'
					})
					
				}else {
					uni.showToast({
						title:res.data.msg,
						icon:'none',
						duration:2000
					})
				}
			},
			toRegister(){
				uni.navigateTo({
					url:'/pages/register/register'
				})
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

