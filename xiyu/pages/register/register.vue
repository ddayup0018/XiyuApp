<template>
	<view class="outer">
		<h1>用户注册</h1>
		<view class="box">
			<view class="item">
				<uni-easyinput prefixIcon="person" v-model="FormData.username" placeholder="请输入用户名" />
			</view>
			<view class="item">
				<uni-easyinput  prefixIcon="locked" v-model="FormData.password" placeholder="请输入密码" type="password"/>
			</view>
			<view class="item">
				<uni-easyinput  prefixIcon="locked" v-model="FormData.re_password" placeholder="请再次输入密码" type="password"/>
			</view>
			<view class="item">
				<uni-easyinput prefixIcon="phone" v-model="FormData.telphone" placeholder="手机号码可以为空" />
			</view>
			<view class="item">
				<button type="primary" @click="userRegister">注册</button>
			</view>
			<view class="item">
				<button type="primary" @click="toLogin">返回</button>
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
					password:'',
					re_password:'',
					telphone:''
				},
				
			}
		},
		methods: {
			async userRegister(){
				if (!this.FormData.username || !this.FormData.password){
					uni.showToast({
						title: '用户名密码不能为空',
						icon:'none'
					});
					return
				}
				if (!this.FormData.password || !this.FormData.re_password){
					uni.showToast({
						title: '两次输入密码不一致',
						icon:'none'
					});
					return
				}
				const res = await this.$http({
					url:'/register/',
					method:'POST',
					data:this.FormData
				})
				console.log(res.data)
				if (res.data.code == 1){
					uni.showToast({
						title:res.data.msg,
						icon:'none',
						duration:2000
					})
				}else if (res.data.code == 0) {
					uni.showToast({
						title:res.data.msg,
						icon:'none',
						duration:2000
					})
				}
			},
			toLogin(){
				uni.navigateBack()
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


